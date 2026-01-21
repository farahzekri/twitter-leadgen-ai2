GENIE_OPS_KEYWORDS = [
    "devops",
    "infrastructure",
    "automation",
    "scaling",
    "deployment",
    "cloud",
    "kubernetes",
    "manual process",
    "ops pain"
]

def compute_relevance(text: str):
    matched = []
    score = 0

    for kw in GENIE_OPS_KEYWORDS:
        if kw.lower() in text.lower():
            matched.append(kw)
            score += 20

    return score, matched