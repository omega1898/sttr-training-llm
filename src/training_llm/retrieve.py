"""Slice 1 retrieval: word-overlap scoring with citations and abstention."""
import re

WORD_PATTERN = re.compile(r"[a-z0-9]+")


def tokenize(text):
    """Lowercase words and numbers only; everything else is ignored."""
    return set(WORD_PATTERN.findall(text.lower()))


def answer_with_citations(question, passages, minimum_overlap=2, top_k=2):
    """Return the best passages with their citations, or abstain.

    passages: list of dicts with "doc_id", "section" and "text".
    """
    question_words = tokenize(question)
    scored_passages = []
    for passage in passages:
        overlap = len(question_words & tokenize(passage["text"]))
        if overlap >= minimum_overlap:
            scored_passages.append((overlap, passage))
    if not scored_passages:
        return {"abstained": True, "answer": [], "reason": "no supporting passage found"}
    scored_passages.sort(key=lambda pair: pair[0], reverse=True)
    best = [passage for _, passage in scored_passages[:top_k]]
    return {
        "abstained": False,
        "answer": [
            {"text": passage["text"], "citation": f'{passage["doc_id"]} {passage["section"]}'}
            for passage in best
        ],
    }
