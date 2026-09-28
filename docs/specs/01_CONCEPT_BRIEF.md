# Models Today Magazine

**Implementation direction — 28 September 2026:** The architecture assigns editorial writing to a GPT-6-family model, with exact model selection following harness completion. The acceptance criteria below govern autonomous operation. Local-only writing requires a separately evaluated writer.

**Document:** Concept & Editorial Operating Brief  
**Maintainer:** Andrew M. Ihnativ  
**Status:** Approved Engineering Baseline  
**Version:** 1.3  
**Date:** 28 September 2026

This baseline defines the product, editorial operation, visual asset governance, and engineering objectives. The companion [Business Requirements Document](02_BUSINESS_REQUIREMENTS.md) defines functional requirements and release gates. Baseline approval applies to these requirements; implementation and operational maturity require the specified evidence.

Names, visual treatments, sample content, and product variants remain subject to their documented approval processes. Concept images establish visual direction only; their records, headlines, and arrangements are not authoritative model data, benchmark results, or fixed implementation requirements. Trademark availability, product permissions, and current rankings require separate verification.

**Revision 1.3:** Establishes the public engineering baseline with standardized ownership metadata, general application contexts, and formal product and engineering language. Source provenance, exact-release identity, original and external experiments, typed workflows, and staged acceptance remain part of the baseline.

> **Models Today is a daily guide to generative AI, presented with the confidence, beauty, wit, and cultural range of a fashion magazine.**
>
> Readers come to discover what changed, choose what to use, learn something useful, and enjoy the intelligence and style of the publication. A recurring cast of original AI fashion personas gives it a recognizable face. A continuously maintained model ledger gives it substance.

## 1. The idea

“Models” carries two meanings deliberately: the generative systems changing daily life, and the fashion personas appearing throughout the magazine. The publication brings them together through art direction, editorial judgment, useful technical coverage, and pleasure in reading.

The central promise is straightforward:

**Know what matters in generative AI, use it well, and make room for a more interesting life.**

The visual references are the editorial confidence of GQ and Esquire, the recognizable illustration tradition of O’Reilly, and the usefulness of a well-maintained technical reference. Develop an original masthead, layout system, cast, and photographic language from those broad traditions.

The site should work at three speeds:

| Reader’s time | What the magazine delivers |
|---|---|
| One minute | What changed today and why it matters. |
| Ten minutes | A useful comparison, practical technique, showcase, or short cultural piece. |
| A longer visit | A feature, thoughtful essay, model investigation, story, poem, or visual editorial worth returning to. |

**Publication naming:** use **MODELS TODAY** on the masthead, **Models Today Magazine** as the full publication name, and **Models Today Mag** as informal shorthand. Naming, domain, and trademark checks come before committing to a public identity.

**Publication descriptor:** “Generative AI, life, and style.”

**Editorial and operating requirements:** professional and hobbyist AI engineers are the core audience; the voice is polished, playful, and entertaining, without sarcasm; the AI fashion personas should look like people from southern British Columbia and the Pacific Northwest; the first wardrobe collection features a few Patagonia products; daily production should eventually run through a choreographed automated workflow; commerce begins with outbound referrals.

The ledger foregrounds **hot and upcoming individual models and harness releases**, their capabilities, safety evidence, and suitability for enterprise use. The maintainer shall curate the initial data sources. Original measurements and well-attributed external experiments are intended to become substantial editorial assets.

### A publication with inspectable engineering

Models Today has two complementary goals: deliver a useful publication and provide an inspectable reference for the design, implementation, evaluation, and operation of reliable AI software. Engineering evidence shall include working code, explicit contracts, recorded runs, failure recovery, measured trade-offs, and documented implementation decisions and contributions.

The engineering descriptor is **“An evidence-backed discovery and publishing system with schema-constrained agent workflows.”** Use “multi-agent” when distinct model-driven workers actually collaborate under the coordinator. Use “deterministic” for the specific validation, state transitions, transformations, and rendering that warrant it. Fresh model generation, image synthesis, external services, and mutable sources do not become deterministic because their outputs fit a schema.

An engineering case study may accompany the reader-facing publication. It shall provide architecture, execution traces, contracts, evaluations, recovery evidence, and the resulting edition. Product documentation shall connect reader tasks and interface behaviour to the underlying discovery and publishing capabilities. The magazine retains its editorial identity and purpose.

## 2. Audience and point of view

The core audience is **professional and hobbyist AI engineers**: people who build with models, experiment with harnesses, run local systems, and enjoy learning what the tools can do. IT leaders, data leaders, developers, analysts, designers, and independent builders are adjacent readers. Curious, technically literate readers should also feel welcome.

The magazine respects expertise while explaining unfamiliar ideas. A newcomer should understand a recommendation; an experienced reader should be able to inspect its evidence.

Life and style are a substantial part of the editorial identity. Cover personal projects, learning, creativity, travel, work environments, objects, clothing, leisure, and the experience of living with increasingly capable software. Some cultural pieces can stand entirely on their own.

The voice is **polished, playful, and entertaining**, informed by the curiosity and competence of its audience. Playfulness can be bold, theatrical, or delightfully unexpected when the piece benefits from it. Use wordplay, imaginative scenes, elegant surprises, and recognizable moments from building with AI. The tone has no sarcastic edge; humour should create enjoyment and recognition without belittling readers or their enthusiasm.

Possible cover lines include “Small model. Full calendar.”, “Good agents need good briefs.”, and “Off-duty. On-device.” These are tone examples, not a requirement to turn every headline into a joke. Findings, limitations, and instructions stay precise. Technical writing should answer what the reader can do, what it takes, and where the result stops being dependable.

The magazine’s advantage should accumulate through **a trusted history of changes, useful tested guidance, original experimental data, intelligent coverage of others’ experiments and viewpoints, recognizable visual characters, and editorial taste**.

## 3. Editorial departments

| Department | Purpose | Typical formats |
|---|---|---|
| **The Daily Ledger** | Help readers discover and choose individual model and harness releases. | Hot and upcoming releases; capability, safety, and enterprise-readiness views; access and pricing changes; deprecations, withdrawals, and corrections. |
| **The Edit** | Explain what deserves attention today, this week, and this month. | Shortlists of specific releases, overlooked discoveries, cover stories, showcases, and editor’s selections. |
| **The Test Bench** | Give readers experimental evidence for choosing tools and configurations. | Original local/cloud/API tests, speed measurements, task-specific comparisons, external experiments, replications, and useful negative results. |
| **Field Notes** | Make readers more capable. | Technical writing tips, prompting, coding, research, local models, workflows, harness configuration, and practical tricks. |
| **Life & Style** | Explore the human setting in which these tools are used. | Workwear, devices, desks, travel kits, creative practice, personal routines, and useful objects. |
| **Point of View** | Publish arguments with an accountable editorial voice and bring useful outside perspectives into the conversation. | Editorials, interviews, attributed viewpoints, evidence-linked commentary, and letters. |
| **The Salon** | Give the publication literary and cultural depth. | Short fiction, poetry, visual essays, humour, and conversations about art and technology. |

“Shop the scene” is an optional component within suitable stories. It does not need to become a major department at launch.

Technical scope includes large and small language models, image, audio, video, multimodal systems, local deployment, APIs, and agent harnesses. Begin with the parts the publication can cover well, then expand using the same evidence standards.

**Useful distinction:** “Hot” describes current attention or editorial interest. “Best for this task” requires an explicit comparison. “New” describes a dated event. These labels should never silently substitute for one another.

## 4. Publication rhythm

The ledger changes daily. The magazine has a steadier visual rhythm so its best work remains visible.

| Rhythm | Recommended initial output | Eventual operation |
|---|---|---|
| Daily | Refresh exact-release records, publish meaningful changes, and provide a concise editor’s selection when warranted. | Scheduled scanning of registered sources, separate experiment and viewpoint queues, and a clearly dated daily digest. |
| Weekly | Refresh the cover package; publish a substantial practical piece and an editorial or cultural piece. Include a test report or external-experiment digest when worthwhile evidence is ready. | Coordinate stories, completed experiments, imagery, distribution, and the weekly digest as a planned edition. |
| Monthly | Publish an overview of consequential changes, persistent recommendations, and selected highlights. | Produce an archived issue that captures the period while linking to current records. |
| Event-driven | Respond to significant releases, withdrawals, access changes, or corrections. | Prioritize exceptional events and update affected recommendations. |

These are starting targets, subject to the actual production effort. A quiet day can say that no material changes were verified. Keep the last successful check visible if a scheduled refresh fails. Daily freshness does not require a new cover image every morning.

Archive editions as historical publications. A story’s original publication date, later revisions, and linked model’s current status should remain distinguishable.

## 5. The website experience

### The cover and first pages

The homepage opens like a magazine cover and becomes a usable web publication as the reader scrolls. Headlines, links, dates, and navigation are real page elements, so they remain readable, accessible, and editable.

| Position | Experience | Example treatment |
|---|---|---|
| **The cover** | A commanding portrait or scene, large masthead, one main story, and a few disciplined cover lines. | An original persona in sculptural outerwear at a quiet desk. Working headline: “SMALL MODELS. BIG DAYS.” |
| **Today’s changes** | A compact, readable briefing with links into the ledger. | “What changed,” “Who it affects,” and “What to do next,” with verification times. |
| **The lead feature** | A beautifully paced feature with one clear argument. | “What can a local model actually do for your working day?” |
| **The Edit** | A few strongly differentiated selections for current needs. | Writing, coding, private local use, image-making, and an unexpected discovery. |
| **The Test Bench** | A compact result readers can inspect and reproduce where practical. | An exact-release speed comparison with configuration, sample count, methods, and a link to the underlying runs. |
| **Field Notes and Life & Style** | A practical lesson alongside a human-scale story. | “Give a coding agent a useful brief” beside “A desk for deep work.” |
| **The Salon** | A quieter reading space. | A short story, a poem, or a visual essay, presented with the same care as a feature. |
| **The optional shopping module** | A compact, clearly labelled product list connected to the scene. | Actual item names, appropriate source images, retailer links, and disclosure where commission applies. |

All titles above are illustrative editorial ideas, not claims about current products or test results.

Recommended primary navigation: **Today · Models · Field Notes · Life & Style · Culture**, plus search. Rankings live within Models; editorials and literature are easy to reach through Culture and homepage features. Readers can go directly to the ledger without passing through a long cover experience.

Model-release pages should connect back to features, tests, guides, and change history. Family pages support browsing and version history; the hot lists and comparisons link to individual releases. Harnesses receive the same treatment. Persona pages connect their appearances and approved looks. Articles link to the exact model version, harness, and run record where relevant.

Mobile deserves its own cover crop and headline arrangement. Keep disclosures, verification dates, comparison labels, and main actions visible at ordinary reading sizes. Avoid making an essential interaction depend on hover.

### Art direction

The visual language is **editorial photography, precise typography, tactile materials, and generous space**. Use natural skin texture, plausible fabrics, controlled lighting, meaningful locations, and strong composition. Let computing appear through credible objects and situations. Ground the casting and atmosphere in southern British Columbia and the Pacific Northwest: people who feel familiar in Vancouver, Surrey, Langley, Victoria, Seattle, or Portland, photographed with exceptional editorial care.

Start with a paper-white or warm ivory background, ink-black typography, and one seasonal accent such as oxblood, cobalt, or chartreuse. Large expressive serif headlines can sit beside a restrained sans serif for reading and navigation. Use a compact monospace face sparingly for model versions and technical values. Final font choices require suitable web licences and readable rendering.

Design contrast and reading size deliberately; technical tables need clarity as much as the cover needs drama. Keep charts and factual diagrams derived from actual data and drawn with appropriate software. Generate photographic and imaginative illustration separately.

## 6. The model ledger and rankings

### Individual releases are the unit of attention

The front-facing ledger is a living selection guide to **specific models and harness releases**. Each row needs enough identity for a reader to find, use, or investigate that exact release. Broad family names such as Qwen, Gemma, or Llama are useful grouping labels, but cannot stand in for an individual model on a hot list or in a test result. All production hot-list and comparison entries must resolve to individual release records.

Use the official model ID and version or checkpoint revision when available. Record size and variant, relevant fine-tuning, quantization or precision, and the provider endpoint used in a test. A hosted service alias can change underneath the same name: resolve a snapshot where possible, otherwise retain the alias, observation date, and reproducibility limitation. Never invent an immutable version that the provider does not expose.

For harnesses, identify the project, release or commit, model configuration, tools, and relevant settings. A useful product display may group related runs; the underlying evidence preserves the actual configuration. Maintain links between families, releases, deployments, harnesses, experiments, and lifecycle events.

### Discovery and selection views

| View | Reader’s question | Required basis |
|---|---|---|
| **Hot today / this week / this month** | Which individual releases deserve attention now? | A stated time window and reason for inclusion: new capabilities, credible evaluations, adoption signals, or editorial discovery. Label editorial selection and measured popularity distinctly. |
| **Upcoming** | What should I watch or prepare for? | An identifiable announcement or preview, source date, expected availability if stated, and clear distinction between a roadmap, restricted preview, and available release. |
| **Strong and powerful** | Which options perform well on my task? | Task-specific capability evidence, failure behaviour, relevant comparison group, settings, and practical limits. Model size alone is insufficient. |
| **Safety and reliability** | What do we know about failures and the controls around them? | Scoped tests or documented evidence on factual errors, prompt injection, tool actions, data handling, or other relevant risks; identify what was and was not assessed. |
| **Enterprise readiness** | Is this a credible candidate for a particular organisational use? | A named deployment scenario and evidence on licensing, data terms, identity/access controls, auditability, operational reliability, support, versioning, and lifecycle commitments as applicable. |

Apply all five views to both models and harnesses. A harness assessment can additionally inspect sandboxing, permission boundaries, secret handling, dependency maintenance, retries, observability, and support for repeatable work. Hosted service controls belong to the relevant service and plan; they are not automatically properties of the underlying model weights.

These views can lead to different shortlists. A release can be exciting and capable while its enterprise evidence is incomplete. Use explicit states such as **documented**, **tested under stated conditions**, **partially assessed**, and **not assessed**, with dates and links. “Safe” or “enterprise-ready” must have a visible scope and basis; a badge is not a universal guarantee or certification.

### A record of what actually changed

| Record group | Information |
|---|---|
| Identity | Exact official model ID/version or harness release/commit; provider or maintainer; family; aliases; relevant variant and configuration. |
| Capability and access | Modalities, tasks, API/local access, preview restrictions, supported deployment routes, and regional limits where material. |
| Lifecycle | Announcement, availability, last verification, deprecation, withdrawal, and supersession dates, with evidence for each event. |
| Practical requirements | Model size where known, tested hardware/runtime, memory needs, context limits, and dependencies. Unknown values remain unknown. |
| Terms and cost | Linked licence or terms, restrictions, price with currency and billing unit, and when checked. Distinguish open weights from open source. |
| Evidence | Primary links, author/publisher, published and retrieved times, evidence type, relevant version, test IDs, and conflicting findings. |
| Selection and readiness | Reason for attention, use-case capability, safety and enterprise evidence, limitations, recommendation date, and review trigger. |

Keep lifecycle status separate from evidence status. “Available” describes access; “provider-reported” describes the basis for a claim. An upcoming announcement need not have benchmark results. An unverified rumour stays in the scout queue until there is a publishable basis. Preserve previous observations when a release changes or disappears.

### Sources first, scanning later

**The maintainer shall curate the initial sources of model and harness data.** Begin with a small curated source register, assess its coverage and gaps, and then build the scanning mechanism around it. Candidate sources may include official release notes, repositories, model cards, documentation, evaluation sites, research publications, and selected practitioner feeds.

Each source record carries its owner, URL, scope, source type, available access method, update cadence, last successful check, attribution/reuse conditions, and verification rules. Confirm whether RSS, an API, permitted page retrieval, or manual review is actually available; do not assume every publication or social account has a usable feed.

Authority depends on the claim. An official announcement establishes what its publisher announced; a performance claim still needs its methodology examined. A commentator’s post can point to a release, report an experiment, or offer an opinion. Follow it to the underlying evidence and deduplicate reposts. The eventual scanner classifies individual items and preserves their source trail.

### Original experiments as a publication asset

Models Today can publish **real experimental data from tests it actually runs**, locally, on GCP, through hosted APIs, or on other suitable infrastructure. Small, well-documented investigations can be valuable to readers without becoming a comprehensive benchmarking organisation. Start with a question readers care about and choose an affordable experiment that can answer it.

| Example experiment | Useful measurements | What the report must distinguish |
|---|---|---|
| **Speed and responsiveness** | Time to first token where streaming applies, output generation rate, and total completion time. | Client-observed latency versus server measurements; warm versus cold starts; input/output lengths; cache state; quality of the answer. |
| **Concurrent work** | Requests or tasks completed per unit time, latency distribution, errors, and timeouts at stated load. | Single-request responsiveness versus aggregate throughput, offered load versus successful work, and sufficiently sampled tail latency. |
| **Local versus cloud** | Completion quality, elapsed time, memory use, and observed cost for the same workload. | Hardware, runtime, region/network path, precision, configuration differences, and which costs are included. |
| **Harness comparison** | Task success, time to a correct result, tool calls, retries, and cost per successful task. | The same model and task set with different harnesses, including each harness version and permission configuration. |
| **Model trade-offs** | Task accuracy, structured-output validity, failure rates, latency, and memory across exact variants. | Size, quantization, prompt, context, and runtime effects; faster output is useful only with adequate task performance. |
| **Reliability in a stated scenario** | Repeated-run consistency, recovery, and outcomes on selected adversarial or failure cases. | Tested behaviours and deployment boundaries; a limited experiment cannot establish general safety. |

Speed reports should keep **time to first token**, **generation speed**, and **end-to-end task time** separate. For decision models such as Jev,[10] request latency and decision throughput may be the appropriate measures instead of generated tokens per second. Comparisons across tokenizers should include output length or task-level measures so a token-rate figure does not imply equivalent useful work.

For every published experiment, preserve a run ID and date; exact model and harness identities; hardware, OS, runtime, and dependencies; endpoint and region where applicable; workload and dataset provenance; prompts and generation settings; warm-up/cache/concurrency conditions; repetitions and failures; scoring rules; raw timing and output records; and the analysis or script used. Report sample counts and appropriate distributions or uncertainty. Mark small trials as exploratory rather than presenting fragile tail percentiles or universal rankings.

Publish a readable verdict with a compact methods panel and downloadable code/data where permitted. Include limitations, failed runs, negative findings, and changes on retest. Label locally run results, GCP results, and hosted-API results accurately. Record measured cloud/API spending and stated local cost assumptions; report original billing currency and any CAD conversion basis separately.

Choose an explicit time and spending budget before cloud work, set job limits, and clean up temporary compute. Run selected experiments when they can resolve a useful question; daily scanning does not require an expensive daily benchmark suite. No local-versus-cloud performance outcome is assumed in advance.

### External experiments are experiments too

Cover experiments conducted by others, including **Ethan Mollick’s documented trials and research**, as a distinct and valuable stream. A one-off exploratory experiment can be interesting; describe its limits and method. It does not have to originate with Models Today to qualify as experimental evidence.

Each report identifies who conducted the experiment, the original publication and date, the task, known model versions and conditions, the observed result, and what detail is missing. Distinguish a single-run demonstration, an exploratory test, a controlled comparison, and a larger study without dismissing the smaller formats. A summary of someone else’s test is an **external experiment**; rerunning its protocol is **our replication attempt**; analysing its existing dataset is **our reanalysis**.

### Evidence and rankings readers can understand

Use explicit labels for **provider-reported result**, **external experiment**, **Models Today experiment**, **replication/reanalysis**, **commentary**, and **editorial selection**. Record who conducted the work separately from its methodological quality. An independent test can be weak; a vendor test can be informative within its disclosed scope. A familiar author’s name does not turn every post into the same kind of evidence.

Rank by use case and comparable conditions. Preserve both model and harness identities, link every finding to its test or source, and avoid combining incompatible scores into a universal league table. If a composite score becomes useful, publish its weights and underlying results. One good-looking output can support a showcase; broader performance claims require broader evidence.

## 7. Original fashion personas

The cast is an original editorial property of Models Today. Each persona should be recognizable across outfits, stories, and image-generation tools. Its identity remains independent of a particular model provider, fashion label, or commercial partner.

Personas have **brand-like names**, not conventional human names. They are fictional adult characters presented openly as AI-generated. Start with two developed personas; expand to a small cast after the visual workflow works consistently.

### Regional casting direction

**The AI fashion models should look like people who live in southern BC and the Pacific Northwest.** This is a casting brief for their faces, hair, bodies, grooming, and everyday presence, as well as their wardrobe and setting.

Build a visually varied cast, with room for East Asian, South Asian, European, Indigenous, and mixed-heritage appearances. Develop individual faces with recognizable features and natural skin texture. Include a believable range of adult ages and body types; some characters can be in their forties or fifties. Heritage and appearance do not determine a persona’s technical interests or voice.

Use locally familiar styling cues: practical layers, understated grooming, comfortable movement, and a considered mix of technical clothing and ordinary city clothes. Fashion-magazine polish comes through tailoring, composition, lighting, and confident presence. Give the cast enough range for a café, workshop, office, apartment, waterfront, or evening out. Regional character should remain visible when the background contains no mountains, forest, or rain.

For the first two personas, explore an East Asian casting direction for VELUM and a European or mixed-heritage direction for PARALLAX; these are provisional options within the regional brief. Settle the actual faces through reference sheets before production. The names remain brand-like, and the characters remain original fictional individuals.

The following names and treatments are exploratory creative directions, **not cleared marks or final casting decisions**.

| Working persona | Editorial territory | Visual and styling direction | Voice |
|---|---|---|---|
| **VELUM** | Writing, language, taste, and reflective work. | An adult feminine-presenting figure with a distinctive blunt dark bob, stable facial proportions, and a composed gaze. Ivory, ink, soft tailoring, textured knits, and one recurring original accessory. | Precise, literary, observant. |
| **PARALLAX** | Systems, coding, evaluation, and tools. | An adult masculine-presenting figure with close-cropped hair, a recognizable silver streak, and an established face and silhouette. Charcoal, cobalt, functional layers, and architectural outerwear. | Direct, curious, playfully inventive. |
| **AERIFORM** | Mobility, local computing, travel, and everyday life. | An adult androgynous figure with short textured hair, an immediately recognizable profile, and a fluid silhouette. Stone, moss, technical fabrics, and considered travel accessories. | Practical, open, adventurous. |
| **CHROMA** | Images, sound, culture, and creative experiments. | An adult figure whose face and signature hair silhouette remain fixed while garments carry bold colour and playful volume. Strong compositions and expressive gestures. | Playful, articulate, culturally alert. |

These territories are editorial lenses, not assumptions about gender or appearance. Define a cast with distinct ages, skin tones, body types, and ways of carrying clothing. Build original faces rather than replicas of recognizable people.

Personas can front columns, covers, scene collections, and recurring series. Real editorial responsibility belongs to identified human editors. A persona’s profile states that it is fictional; it should not acquire invented employment credentials, human biography, or first-hand product experiences presented as fact.

### The persona bible

For each approved persona, maintain:

- A stable ID, name, pronunciation, short identity statement, editorial role, voice examples, and boundaries.
- Approved front, profile, three-quarter, and full-body references; neutral expressions and a limited expression set; stable age appearance, face, skin, hair, and proportions; a casting note explaining the intended southern BC / Pacific Northwest presence.
- Signature styling rules, silhouette preferences, palette, recurring accessories, and approved variation.
- Reference assets, creation provenance, relevant tool terms, prompt templates, and a version history.
- A record of final appearances, including which identity version and wardrobe pieces were used.

Use reference-conditioned generation and careful editing. A repeated text prompt or seed alone is not an identity guarantee. A change to the core face or body is a deliberate new version requiring editorial approval.

Commercially, the durable assets include the names, human-authored character descriptions, visual direction, edited work, publication identity, and audience relationship. Do not assume every raw AI image has exclusive copyright protection. The US Copyright Office distinguishes human expressive contributions from purely generated material.[3]

## 8. Wardrobe, accessories, and objects

Treat clothes, jewellery, bags, computers, headphones, cameras, furniture, and other recurring objects as reusable editorial assets. Software interfaces can also be governed assets when shown on a device.

Every asset needs **a visual specification** and **a separate record of permitted uses**. A convincing image does not establish permission. Permission does not establish that the rendering is accurate.

| Asset field | What it controls |
|---|---|
| Stable ID and revision | Which exact garment or object appears in a scene. |
| Identity | Original house design, generic item, or a specific third-party product with brand, model, variant, and SKU where known. |
| References and provenance | Approved views, detail images, their sources, and the documented basis for using each reference. |
| Visual specification | Colour, material, construction, seams, closures, pockets, logos, proportions, device ports, and other identifying features. |
| Fit and interaction | How a garment falls on each persona; object dimensions, grip, weight cues, hinge position, contact points, and plausible use. |
| Rights and usage | Who owns the source material; relevant licence or permission; whether modification, AI processing, editorial use, commercial use, and distribution are covered; unresolved questions. |
| Commerce | Official product URL, retailer URL, geographic availability, affiliate status, price source, and last check where applicable. |
| Publication record | Which scenes use the asset, any product deviations, required attribution, and the approved caption. |

### Three useful production paths

1. **Specific real products, starting with Patagonia.** Use a product brief, reliable references with an established basis for use, and a fidelity check. Record editorial depiction, use of source photographs, and later promotional placements separately. Any permission or licence should cover the actual planned use.
2. **Generic editorial styling.** Use ordinary categories such as neutral trousers or a silver laptop when the exact brand is irrelevant. Avoid describing a fictional item as a purchasable SKU.
3. **Original house wardrobe, as a later extension.** Develop distinctive garments and accessories belonging to the magazine’s creative world when editorial or commercial interest justifies them. Record human design contributions and generation terms.

Third-party product depiction can be legally permissible without an agreement in some circumstances, but this concept does not grant blanket clearance. US trademark law addresses misleading implications of affiliation or sponsorship.[2] **“AI-generated,” “inspired by,” and “not sponsored” are descriptions, not permission or automatic legal protection.** Source-photo rights and brand identification are separate questions.

### The first Patagonia collection

**Start with a small Patagonia collection.** The following three products provide concrete candidates for two garments and one recurring accessory. The cited official product pages provide identity and design references; colours, fit, availability, and final asset references must be verified during visual production.[4][5][6]

| Candidate | Proposed editorial use | Visual details to govern |
|---|---|---|
| **Women's Nano Puff Jacket, style 84218** | A VELUM look for a working day that moves between indoors and outdoors. | Quilting layout, collar, zip, pockets, hem, chosen colour, and the exact garment silhouette. |
| **Men's Torrentshell 3L Rain Jacket, style 85241** | A PARALLAX or AERIFORM look for a rainy commute, travel, or a field-work scene. | Hood structure, cuffs, front closure, pockets, fabric appearance, and chosen colour. |
| **Black Hole Pack 25L, style 49298** | A recurring bag in arrival, departure, and laptop-carrying scenes. | Size, material finish, straps, openings, branding, and plausible object interaction. |

These are editorial selections, with no Patagonia partnership, permission, or affiliate approval claimed. Record the exact variant used in each scene; product families and old style numbers must not be blended into an invented hybrid. The linked product pages are information sources, not an image-reuse licence.

For a checked depiction, a working caption is: **“AI-generated styling concept depicting Patagonia’s [exact product and variant]. Patagonia did not create or sponsor this image.”** If a rendering materially changes the product, correct it before presenting it as that exact item. Adding “inspired by” does not resolve fidelity or rights questions. Later affiliate participation requires its own accurate disclosure.

## 9. Illustration production and quality

“Impeccable” is a release standard, not a promise that every generated candidate is usable. Publish fewer illustrations if that is what consistent quality requires.

The production sequence is **brief → select approved references → compose → generate or composite → inspect → correct → approve → export**.

Each scene brief names the story, persona version, wardrobe and object IDs, location, action, camera position, lighting, crop, headline space, and intended use. Include an explicit interaction: adjusting a jacket cuff, lifting a laptop from a bag, typing with plausible hand placement, or reading beside an accurately scaled object.

| Review area | Acceptance standard |
|---|---|
| Identity | The persona is recognizable against its approved references, including face and proportions, and retains its intended regional casting and natural appearance. |
| Anatomy and physics | Hands, joints, gaze, contact, shadows, reflections, and object support are plausible. |
| Wardrobe | Material, seams, closures, logos where appropriate, layering, and fit match the brief. |
| Product fidelity | Named items match the intended variant; invented ports, packaging, controls, or features are corrected. |
| Composition | The scene has a focal point, good pacing, intentional empty space, and useful desktop and mobile crops. |
| Factual separation | Generated scenes do not impersonate product photographs, actual test evidence, or documentary events. |
| Finish | Inspect both at publication size and enlarged; remove generation defects and unsuitable crops. |
| Publication package | Caption, disclosure, alt text, credit, source record, and associated product links are complete. |

Use image generation where it helps create the scene. When an exact product or interface is essential, use a suitable approved asset or controlled compositing rather than relying on the generator to reproduce every detail. Render typography, product specifications, charts, and meaningful interface text through normal design or web tools.

Keep visual identity approval initially human-led. Automated comparison and quality checks can assist, but recurring defects should change the production recipe rather than become an accepted part of the aesthetic.

### Example scene brief

> **Story:** A quieter way to work.  
> **Cast:** Approved VELUM identity, version 1.  
> **Wardrobe:** Approved Patagonia Women's Nano Puff Jacket asset, style 84218, in one recorded colour, with neutral supporting garments.  
> **Action:** Seated at a walnut desk, opening an approved laptop with one hand while the other rests naturally beside a notebook.  
> **Image:** Editorial realism, late-afternoon side light, visible fabric texture, restrained expression, credible scale and contact.  
> **Layout:** Space above and left for editable cover text; alternative mobile crop preserving face and laptop.  
> **Checks:** Identity, hands, hinge geometry, quilting, fabric, shadows, visible interface, and object accuracy.  
> **Caption:** AI-generated styling concept featuring the fictional persona VELUM and depicting Patagonia’s Women's Nano Puff Jacket in [approved colour]. Patagonia did not create or sponsor this image. Final text must match the actual scene and commercial relationship.

## 10. Literature, viewpoints, and authorship

### Literature and original culture

The Salon provides editorial range and a reason to visit beyond product decisions. Publish short fiction, poetry, playful speculative pieces, visual essays, and criticism with actual literary ambition. Subjects can include work, desire, memory, ordinary life, technology, and the unfamiliar futures people imagine. Entertainment can be exuberant while the overall voice remains polished and free of sarcasm.

Human-written, AI-assisted, and intentionally AI-generated work can all appear if the production role is accurately described. Use an authorship note appropriate to the piece. Preserve a real editor’s responsibility for publication, avoid invented human bylines, and distinguish a fictional speaker from a claim about real events.

Suggested initial lengths are 500–1,500 words for short fiction, one to three poems in a small selection, and 600–1,200 words for an essay. These are editorial choices, not limits on ambition.

### A curated conversation with outside voices

Bring selected public writing, videos, interviews, and research into Point of View and The Test Bench. Initial candidate sources include **Ian Bremmer, Ethan Mollick, and Nicholas Thompson**. They are candidate sources for monitoring, not contributors or endorsers of the magazine. Exact feeds and access methods will be selected when the source register is assembled.

| Candidate source | Potential editorial value | Treatment of each item |
|---|---|---|
| **Ethan Mollick**, author of *One Useful Thing*.[7] | Practical AI use, experiments, research, work, learning, and creative applications. | Route actual tests to external-experiment coverage; distinguish observations, research findings, predictions, and opinion. Preserve his original methods and caveats where available. |
| **Ian Bremmer**, through his own GZERO writing and public channels.[8] | Geopolitical and institutional context affecting AI builders, infrastructure, markets, and adoption. | Attribute his interpretation, trace factual claims where material, and select pieces relevant to the magazine’s audience. GZERO staff articles retain their actual bylines. |
| **Nicholas Thompson**, including *The Most Interesting Thing in Tech* and linked original work.[9] | Technology, media, products, public life, and the human consequences of AI. | Link to the original item and identify whether it is commentary, reported evidence, an interview, or an experiment. |

A compact recurring feature could be **“What We’re Reading and Trying”**: the author’s point, the evidence or experiment behind it, why it matters to an AI engineer, and a question the magazine could investigate. Interesting disagreement should be represented accurately; several people repeating the same source do not establish independent confirmation.

Use original summaries, direct attribution, links, and appropriately limited excerpts or permitted embeds. Do not reproduce whole newsletters or convert a speaker’s words into an invented persona quote. Access and reuse conditions belong in the source register. Our interpretations and experiments remain distinguishable from the original author’s work.

## 11. Commerce as a small experiment

The initial commercial model is **outbound referrals and affiliate links**. The reader goes to the retailer or provider to buy. Models Today earns a commission where it has an approved arrangement and a qualifying sale. The retailer runs checkout, order processing, delivery, returns, and support.

The pilot excludes inventory, packing, order-desk operations, and customer-payment processing. Shopify and a magazine checkout are unnecessary at this stage. Affiliate participation still involves programme applications, payout details, applicable reporting, link maintenance, and observing programme terms.

Potential categories include clothing, accessories, computers, peripherals, other hardware, software, fragrances, and considered everyday objects. Begin visually with the Patagonia collection above, then select further products for audience fit and editorial interest. No commercial agreement or commission forecast is assumed by this document.

A shopping module should make the actual retailer and linked product clear. If an illustration merely suggests a look, describe linked items as alternatives rather than claiming that they are the exact objects pictured. Show actual product information from suitable sources; verify the conditions on reusing images and descriptions.

In US-facing affiliate content, disclose the financial relationship clearly and near the relevant recommendation. For example: “We earn a commission from qualifying purchases through these links.” Paid placements and material gifts need appropriate disclosure too.[1] Apply any additional programme wording and relevant Canadian requirements when designing the launch policy.

The revenue model must preserve the publication’s usefulness. Rankings and test outcomes cannot be bought. Sponsored articles and placements have visible labels; commercial relationships are recorded alongside relevant coverage.

Measure the experiment with product-link clicks, attributable approved sales, realised commission, reversals, and the work required to maintain it. These provide a better basis for expansion than assumed retail margins. Programme terms and attribution determine actual earnings.

## 12. A choreographed daily operation

**The intended end state is an automated publication workflow with defined stages, saved state, evidence, quality controls, and targeted editorial intervention.** Human review is initially useful for learning and calibration; it should not become a permanent manual step for every ordinary update.

Use one coordinating workflow at first. Each stage has named inputs, outputs, completion conditions, and failure behaviour. Some stages are deterministic code; others may use a language or image model. A stage does not require its own autonomous agent.

| Stage | Work and saved output | Automation boundary |
|---|---|---|
| **1. Scout** | Check the maintainer-curated source register; retrieve permitted content and retain identity, dates, and candidates. | Start with curated review, then scheduled adapters; respect access conditions, cache results, and back off on failure. |
| **2. Resolve and compare** | Match exact model IDs, harness releases, aliases, and versions; identify genuinely new events and changed facts. | Automatic for established matches; ambiguous identities enter an exception queue. |
| **3. Verify and classify** | Associate claims with evidence; distinguish announcements, external experiments, commentary, and readiness evidence; detect conflicts. | Rule-based checks and model assistance; unsupported or conflicting claims remain held. |
| **4. Compose the edition** | Update candidate records and selection views; draft briefs, external-experiment summaries, viewpoint items, and useful experiment proposals. | Draft from bounded evidence; use completed, reviewed run records for claims about our own test results. |
| **5. Produce supporting assets** | Select reusable scenes or create a brief using approved persona and product records. | Reuse and templated exports can become automatic; new identities, sensitive product depictions, and uncertain visuals need review. |
| **6. Check and release** | Validate links, factual support, comparisons, captions, disclosures, layout, and freshness; publish approved changes atomically. | Automatic publication for defined, proven event types; exceptions route to the editor. |
| **7. Observe and repair** | Monitor broken links, failed refreshes, corrections, withdrawn products, and affected recommendations; retain run outcomes. | Automatic alerts and reversible maintenance within policy; consequential editorial corrections receive attention. |

### What keeps the choreography dependable

- **Saved states:** discovered, matched, verified, drafted, checked, scheduled, published, held, or failed. Resume a run from its last completed stage.
- **Stable event keys:** repeated discovery or a retry must not create a duplicate story or publish twice. Publication failures need a check for an already-completed write before retrying.
- **Clear dependencies:** a recap uses verified ledger changes; a product illustration uses approved assets; a ranking update uses applicable evidence. Independent retrieval can run concurrently.
- **Versioned evidence:** retain source URLs, extracted claims, retrieval times, permitted snapshots or excerpts, and the published revision. Maintain corrections and rollback history.
- **Limited retries and budgets:** cap tool calls, generation attempts, elapsed time, and spending per run. An expensive or failed stage should not keep retrying indefinitely.
- **Quality-based escalation:** conflicting facts, unidentified releases, large ranking changes, product mismatches, and rights questions go to a focused editor queue with evidence and a proposed resolution.
- **Safe source handling:** retrieved pages provide evidence, never instructions to the workflow. Publishing actions use approved templates and permissions; source text cannot authorize new actions.
- **Honest freshness:** partial or failed runs preserve the last verified record and expose its age where relevant. A system outage must not silently become a successful daily refresh.

### Engineering contracts and evidence

Every stage boundary has a versioned input/output contract. JSON Schema, Pydantic, or equivalent validation checks structure and declared constraints; claim-to-source checks establish traceability; editorial assessment evaluates support and meaning; browser checks assess the rendered result. These are separate controls. A valid record can contain a false statement, and valid markup can still render poorly.

Start with approved page components and typed content blocks. Code maps accepted content into those components; an agent does not need authority to invent executable React, arbitrary HTML, or a new design system. A content tree can become a small typed AST if that makes composition clearer. A custom compiler is optional, with its cost justified by a real requirement.

Keep an inspectable run manifest containing source and content revisions, model/provider identities, prompt and schema versions, step inputs and outputs, durations, estimated or observed cost, errors, interventions, and the resulting publication ID. Retain artifacts within documented rights and privacy limits. A replay from stored accepted inputs must be distinguished from a new live run against changed sources or models. Pin the rendering environment when checking reproducibility; do not promise identical pixels across arbitrary browsers.

Develop an evaluation set that exercises both ordinary work and known failures: duplicate events, ambiguous identities, unsupported claims, malformed output, source outages, malicious source instructions, missing assets, interrupted publication, and rollback. Repeat it when prompts, models, adapters, schemas, or templates change. Report the actual sample size, failures, cost, and baseline comparison. Generative quality needs a recorded rubric and editorial judgement as well as automated checks.

Expose a small MCP interface when it provides useful interoperability, such as retrieving a ledger record and its evidence or inspecting a run. Enforce permissions in the application and tool host. Protocol metadata and prompt instructions are not permission boundaries. Add separate agents, services, or cloud orchestration when measurements or workload justify them.

The engineering evidence package shall include an architecture diagram, consequential design decisions, schema examples, a reproducible fixture run, a redacted live trace, an evaluation report, a demonstrated failure and recovery, and the final publication. Mark every capability as planned, implemented, tested, or operational, with evidence appropriate to the claim. A polished screenshot alone is evidence of appearance.

### Autonomy release gates

| Phase | Operating mode | Condition for advancing |
|---|---|---|
| **Editorial pilot** | Automated scouting and drafting; the editor reviews the publication package. | Sources, record structure, recurring errors, and actual workload are understood. |
| **Routine automation** | Publish well-defined, low-risk ledger updates and digests automatically; send exceptions to review. | A representative reviewed history shows acceptable accuracy, duplicate prevention, and reliable rollback. |
| **Coordinated editions** | Schedule ledger, editorial drafts, approved visual assets, and distribution as one edition. | Dependencies, quality checks, asset consistency, and operating cost remain dependable. |
| **Mature operation** | Automate most recurring production; the editor concentrates on taste, investigations, new creative direction, and exceptions. | Monitoring continues to support the chosen autonomy level; failed categories can return to review. |

The editor configures policy, coverage, and budgets. The workflow handles recurrence. Use correction rate, unresolved exceptions, freshness, failed runs, visual rejection rate, and minutes of editorial work per edition to decide what is ready for more autonomy.

**Experiments form a separate scheduled branch:** question selected → protocol and budget set → configuration recorded → job run → artifacts checked → analysis reviewed → result published and linked into the ledger. A failed job retains its failure record. New information may propose a test; it does not silently spend unlimited compute or manufacture a result. This branch can use local hardware, GCP, another cloud, or an API, and become increasingly automated under defined limits.

## 13. The smallest coherent launch

The first version should demonstrate the whole identity at a manageable scale:

- One responsive cover/homepage and a concise navigation system.
- A ledger covering approximately 20–30 deliberately selected individual model and harness releases, with evidence links, discovery/readiness views, and change history. This is a proposed starting scope, not a claim of comprehensive coverage.
- A source register seeded from maintainer-curated material, with explicit gaps and candidate feeds awaiting access-method checks.
- One small original experiment, such as a speed comparison, if feasible within the initial budget; a clearly attributed external-experiment digest can provide value while original testing develops.
- Two or three finished personas with reference sheets, the small Patagonia collection, and a few supporting object records. VELUM, PARALLAX, and AERIFORM are candidate identities subject to reference-sheet approval.
- Reusable page types for a feature, a practical guide, a comparison, and a cultural piece.
- One example weekly edition, including a lead feature, Field Notes article, editorial, and literary contribution.
- A compact optional referral module using ordinary outbound links until relevant affiliate approvals exist.
- A scheduled scout and draft workflow, a publication queue, and clear last-checked dates.
- An inspectable vertical slice connecting a source event to its evidence, validated record, rendered page, and saved execution trace; a repeatable fixture suite demonstrates duplicate handling and recovery.

Start with portable content, a small structured store, versioned assets, and a scheduled workflow. Avoid committing to a complex platform before the prototype demonstrates the reading experience and production effort. Preserve the ability to export the ledger, articles, character bibles, asset records, and evidence.

Newsletters and RSS are useful follow-on distribution options. Add audience accounts, personalized recommendations, comments, and a full shop when reader behaviour justifies the extra operation.

## 14. The first issue

**Working theme:** “Intelligence, worn well.”

**Cover idea:** VELUM in the selected Patagonia Nano Puff Jacket, interacting naturally with a carefully governed computing object in a warm architectural interior. Rain on a large window connects the indoor scene with the outerwear. A second scene features PARALLAX in the Torrentshell with the Black Hole Pack. The scenes are sophisticated and physically believable. The magazine’s identity comes from the faces, styling, light, layout, and editorial ideas together.

**Illustrative contents:**

| Piece | Purpose |
|---|---|
| “Small Models. Big Days.” | A grounded feature on choosing capability that suits a person’s actual tasks. |
| “What Changed While You Were Away” | The daily ledger digest, populated only from verified events. |
| “The Harness Changes the Result” | A practical demonstration of why a model name alone does not explain performance. |
| “A Better Brief for Your Agent” | A useful template with a worked example and limitations. |
| “A Desk for Deep Work” | A visual Life & Style story with an optional, clearly separated product list. |
| “The Right to an Unoptimized Afternoon” | An editorial about the place of convenience and choice in everyday life. |
| “The Last Prompt Before Dinner” | A short literary-fiction concept. |
| “Latency” | A poem title or small poetry commission. |

These titles are proposed commissions, not finished articles. The technical pieces require actual reporting or testing before publication. A Jev feature, an exact-release speed test, and a digest of an external experiment are additional candidate commissions. Select the first issue from evidence available at production time; factual content must be established independently of concept imagery.

## 15. What success would look like

The first experiment should answer five questions:

1. **Do readers return for the ledger?** Track repeat visits and use of model records and change history.
2. **Do they value the guidance and evidence?** Look for engaged reading, methods/data use, useful feedback, voluntary subscriptions, and evidence that experiments helped a reader choose or configure a specific model or harness.
3. **Does the visual identity become recognizable?** Test whether readers recognize the same personas across different scenes and whether the design supports reading.
4. **Can the operation stay proportionate?** Measure editor time, generation costs, correction rates, and realised affiliate income separately.
5. **Does the engineering withstand inspection?** Demonstrate an end-to-end run, a repeatable evaluation, a controlled failure and recovery, traceable publication inputs, and a reasoned account of cost, latency, limitations, and architecture choices. Track this separately from audience traction.

Set numerical targets after a pilot provides a baseline. Pilot success requires a useful, attractive publication that can be refreshed reliably within the allocated editorial capacity.

## 16. Immediate development sequence

1. **Validate the product and visual direction.** Review page concepts with representative readers. Approve the masthead, persona references, and reading experience; maintain the distinction between illustrative content and verified data.
2. **Assemble the sources and release records.** Build the initial register from maintainer-curated sources. Select exact models and harness versions for the first ledger, and document the evidence needed for each view.
3. **Build one real edition and a small evidence package.** Commission the pieces, write an external-experiment digest, and choose a feasible local or cloud speed test with a clear protocol and budget. Publish original results only after the runs exist and have been checked. Refine persona references and Patagonia asset records alongside the editorial work.
4. **Implement the repeatable workflow.** Add authoritative-source scanning, identity matching, differences, evidence classification, drafts, and the publication package; add controlled experiment runners as useful. Exercise a failed refresh, a duplicate event, and a correction before unattended publication.
5. **Run the reader test.** Publish the small edition, observe reading and return behaviour, and try a few relevant referral placements.
6. **Package the engineering evidence.** Follow the companion BRD’s release gates. Produce the architecture and decision records, validated contracts, repeatable fixtures, measured evaluations, recovery demonstration, and a case study tied to the actual delivered version. Documentation must state the demonstrated scope and operational maturity.
7. **Expand proven parts.** Add coverage, personas, or publishing autonomy when the observed result supports it. Additional agents, MCP tools, retrieval capabilities, or cloud workers must serve a demonstrated need.

Implementation dependencies include the initial curated source register, testing infrastructure, naming clearance, final casting, experiment budgets and environments, source coverage, and specific affiliate arrangements. Resolve each dependency at the applicable delivery or release gate.

## Reference notes

This is a creative and operating concept. The legal notes establish constraints for implementation and do not clear a particular image, brand use, or commercial arrangement. The US sources below were checked on 27 September 2026, Pacific time; Canadian requirements need to be considered for a Canadian-operated publication as well.

1. **US Federal Trade Commission, _The FTC’s Endorsement Guides: What People Are Asking_.** Supports clear disclosure of material connections, including affiliate relationships, and truthful representations of product experience. [FTC guidance](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking).
2. **15 USC § 1125.** Addresses, among other matters, representations likely to cause confusion about affiliation, sponsorship, or approval. This is one part of the legal analysis, not a complete test for an image’s lawfulness. [United States Code](https://uscode.house.gov/view.xhtml?req=15+usc+1125).
3. **US Copyright Office, _Copyright and Artificial Intelligence, Part 2: Copyrightability_.** Explains the role of human authorship and creative contributions in protection of work containing generated material. [Official summary](https://www.copyright.gov/newsnet/2025/1060.html) and [report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf).
4. **Patagonia, Women's Nano Puff Jacket, style 84218.** Official product identity and design information. [Product page](https://www.patagonia.com/product/womens-nano-puff-insulated-jacket/84218.html).
5. **Patagonia, Men's Torrentshell 3L Rain Jacket, style 85241.** Official product identity and design information. [Product page](https://www.patagonia.com/product/mens-torrentshell-3-layer-rain-jacket/85241.html).
6. **Patagonia, Black Hole Pack 25L, style 49298.** Official product identity and design information. [Product page](https://www.patagonia.com/product/black-hole-pack-25-liters/49298.html).
7. **Ethan Mollick, _One Useful Thing_.** Candidate source for practical AI coverage, research, experiments, and commentary. [Publication](https://www.oneusefulthing.org/) and [author’s description](https://www.oneusefulthing.org/about). Candidate status does not imply that every post reports an experiment.
8. **Ian Bremmer, GZERO Media.** Official author page and a source for his published analysis and linked channels. [Author page](https://www.gzeromedia.com/u/ianbremmer) and [his GZERO writing](https://www.gzeromedia.com/by-ian-bremmer/).
9. **Nicholas Thompson.** His official homepage identifies and links to *The Most Interesting Thing in Tech* and describes his newsletter. [Official homepage](https://www.nickthompson.com/home/).
10. **TypeSafe AI, _Introducing System One Models & Jev_, 15 September 2026.** Source for Jev’s structured-decision interface; its vendor-reported performance claims require their own assessment. [Announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

---

**Product objective:** Build Models Today as a beautiful, useful daily publication about generative AI and human life, with a ledger of specific model and harness releases, original and external experimental evidence, thoughtful viewpoints, distinctive fashion personas, governed visual assets, and an increasingly automated editorial operation.
