"""Sheet 01 field-summary implementation; validation never grants approval."""

import hashlib
import json
from typing import Annotated, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

Id = Annotated[str, Field(min_length=1, max_length=128, pattern=r"^[A-Za-z0-9_.:-]+$")]
Text = Annotated[str, Field(min_length=1, max_length=8000)]
Digest = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]


class Contract(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", allow_inf_nan=False)


class ModelParameters(Contract):
    model_id: Id
    temperature: float = Field(ge=0, le=2)
    max_output_tokens: int = Field(ge=1, le=1200)


class EvidenceRef(Contract):
    claim_source_id: Id
    snapshot_sha256: Digest


class Claim(Contract):
    claim_id: Id
    subject_release_id: Id
    text: Text
    confidence_score: float = Field(ge=0, le=1)
    evidence_ids: list[Id] = Field(min_length=1, max_length=16)


class Block(Contract):
    node_id: Id
    kind: Literal["heading", "paragraph", "callout", "product_sidebar", "ledger_row", "image"]
    text: Text
    claim_ids: list[Id] = Field(default_factory=list, max_length=32)
    asset_revision_id: Id | None = None

    @model_validator(mode="after")
    def image_requires_asset(self) -> Self:
        if self.kind == "image" and self.asset_revision_id is None:
            raise ValueError("image requires an asset revision; text supplies alt text")
        return self


class PublicationCandidate(Contract):
    schema_version: Literal["1.0"]
    run_id: Id
    subject_release_id: Id
    model_parameters: ModelParameters
    evidence: list[EvidenceRef] = Field(min_length=1, max_length=64)
    claims: list[Claim] = Field(min_length=1, max_length=64)
    content_ast: list[Block] = Field(min_length=1, max_length=128)

    @model_validator(mode="after")
    def resolve_references(self) -> Self:
        def unique(values: list[str]) -> set[str]:
            if len(values) != len(set(values)):
                raise ValueError("duplicate IDs")
            return set(values)

        evidence_ids = unique([e.claim_source_id for e in self.evidence])
        claim_ids = unique([c.claim_id for c in self.claims])
        unique([b.node_id for b in self.content_ast])
        for claim in self.claims:
            if claim.subject_release_id != self.subject_release_id:
                raise ValueError("claim targets a different release")
            if not unique(claim.evidence_ids) <= evidence_ids:
                raise ValueError("unresolved evidence reference")
        for block in self.content_ast:
            if not unique(block.claim_ids) <= claim_ids:
                raise ValueError("unresolved claim reference")
        return self


def candidate_sha256(candidate: PublicationCandidate) -> str:
    """Hash a revalidated revision, including run_id, using this JSON encoding."""
    validated = PublicationCandidate.model_validate(candidate.model_dump())
    payload = json.dumps(validated.model_dump(mode="json"), sort_keys=True,
                         separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
