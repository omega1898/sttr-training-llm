# sttr-training-llm

A source-cited, explainable training assistant grounded in public Navy training documents, built as a starting point for Navy STTR topic **DON27TZ02-NV012, Mission-Specialized Large Language Models for Operational Training and Knowledge Integration** (DoW FY27 Release 2).

## The problem

Workforce turnover and static training materials make it hard to keep sailors proficient. Commercial language models hallucinate and cannot point to the source of an answer about organization-specific material. The topic asks for an explainable language-model system grounded in Navy manpower, personnel, training and education (MPTE) documents, whose answers trace to their sources, adapt to the user's role, and update as materials change.

## Approach in plain terms

1. **Ingest** public training documents and split them into passages, each keeping its document and section.
2. **Retrieve** the passages most relevant to a question.
3. **Answer** only from those passages, and attach a citation to every claim.
4. **Abstain** when no passage supports an answer, instead of guessing.
5. **Measure** hallucination, citation accuracy and usefulness against a plain baseline model, as the Q&A asks.

## Phase I scope

A feasibility study on sample public corpora, covering fine-tuning and retrieval architecture and a hallucination-reduction approach, plus a working proof of concept on representative or proxy data. Phase I must use only publicly releasable (Distribution A) material and no CUI. This is an STTR, so it needs a research-institution partner. See [docs/topic-summary.md](docs/topic-summary.md).

## Status

Skeleton only. The first vertical slice (keyword retrieval with citations and abstention, no model yet) is in [docs/architecture.md](docs/architecture.md) and stubbed in `src/`.

## How to run

```bash
python -m unittest discover -s tests -v
```

## Documentation

- [docs/topic-summary.md](docs/topic-summary.md): what the public topic asks for
- [docs/topic-qa.md](docs/topic-qa.md): posted topic Q&A, summarized
- [docs/references.md](docs/references.md): the topic's references, with links
- [docs/submission-requirements.md](docs/submission-requirements.md): dates, award size, partnering, official instructions
- [docs/architecture.md](docs/architecture.md): first vertical slice and design decisions
