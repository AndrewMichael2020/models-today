"""Synthetic contract checks; these do not exercise a publishing engine."""
import copy
import unittest

from pydantic import ValidationError

from src.contracts.publication_candidate import PublicationCandidate, candidate_sha256


def payload():
    return {
        "schema_version": "1.0", "run_id": "run-001", "subject_release_id": "release-001",
        "model_parameters": {"model_id": "fixture-worker", "temperature": 0.0,
                             "max_output_tokens": 1200},
        "evidence": [{"claim_source_id": "source-001", "snapshot_sha256": "0" * 64}],
        "claims": [{"claim_id": "claim-001", "subject_release_id": "release-001",
                    "text": "Fixture claim", "confidence_score": 0.5,
                    "evidence_ids": ["source-001"]}],
        "content_ast": [{"node_id": "block-001", "kind": "paragraph",
                         "text": "Fixture claim", "claim_ids": ["claim-001"]}],
    }


class ContractTests(unittest.TestCase):
    def test_valid_round_trip(self):
        candidate = PublicationCandidate.model_validate(payload())
        self.assertEqual(candidate, PublicationCandidate.model_validate_json(candidate.model_dump_json()))

    def test_unsupported_authority(self):
        data = payload()
        data["approved"] = True
        with self.assertRaises(ValidationError):
            PublicationCandidate.model_validate(data)

    def test_invalid_boundaries(self):
        mutations = {
            "coercion": lambda d: d["model_parameters"].update(max_output_tokens="1200"),
            "token_cap": lambda d: d["model_parameters"].update(max_output_tokens=1201),
            "nested_extra": lambda d: d["model_parameters"].update(api_key="synthetic"),
            "confidence": lambda d: d["claims"][0].update(confidence_score=1.1),
            "nonfinite": lambda d: d["claims"][0].update(confidence_score=float("nan")),
            "version": lambda d: d.update(schema_version="2.0"),
            "missing": lambda d: d.pop("run_id"),
            "hash": lambda d: d["evidence"][0].update(snapshot_sha256="bad"),
            "empty": lambda d: d.update(evidence=[]),
            "block_cap": lambda d: d.update(content_ast=d["content_ast"] * 129),
            "text_cap": lambda d: d["content_ast"][0].update(text="x" * 8001),
            "executable": lambda d: d["content_ast"][0].update(kind="script"),
            "image_asset": lambda d: d["content_ast"][0].update(kind="image"),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                data = payload()
                mutate(data)
                with self.assertRaises(ValidationError):
                    PublicationCandidate.model_validate(data)

    def test_reference_integrity(self):
        mutations = {
            "release": lambda d: d["claims"][0].update(subject_release_id="other"),
            "evidence": lambda d: d["claims"][0].update(evidence_ids=["absent"]),
            "claim": lambda d: d["content_ast"][0].update(claim_ids=["absent"]),
            "duplicate_evidence": lambda d: d["evidence"].append(copy.deepcopy(d["evidence"][0])),
            "duplicate_claim": lambda d: d["claims"].append(copy.deepcopy(d["claims"][0])),
            "duplicate_node": lambda d: d["content_ast"].append(copy.deepcopy(d["content_ast"][0])),
            "duplicate_reference": lambda d: d["claims"][0].update(evidence_ids=["source-001"] * 2),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                data = payload()
                mutate(data)
                with self.assertRaises(ValidationError):
                    PublicationCandidate.model_validate(data)

    def test_hash_is_order_independent_for_object_keys(self):
        data = payload()
        reordered = dict(reversed(list(data.items())))
        self.assertEqual(candidate_sha256(PublicationCandidate.model_validate(data)),
                         candidate_sha256(PublicationCandidate.model_validate(reordered)))

    def test_hash_changes_with_revision(self):
        data = payload()
        before = candidate_sha256(PublicationCandidate.model_validate(data))
        data["content_ast"][0]["text"] = "Revised content"
        self.assertNotEqual(before, candidate_sha256(PublicationCandidate.model_validate(data)))

    def test_hash_revalidates_mutation(self):
        candidate = PublicationCandidate.model_validate(payload())
        candidate.claims[0].evidence_ids.append("missing")
        with self.assertRaises(ValidationError):
            candidate_sha256(candidate)


if __name__ == "__main__":
    unittest.main()
