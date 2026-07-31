SCHOOL_PALETTE = [
    "#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#F0E442",
    "#7570B3", "#A6761D", "#E7298A", "#66A61E", "#8C564B", "#E6AB02",
]

def stableColorIndex(label):
    key = str(label)
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return h, h % len(SCHOOL_PALETTE)

labels = ["台中市", "彰化縣", "市立高雄高商"]
for lbl in labels:
    h, idx = stableColorIndex(lbl)
    print(f"{lbl} -> hash={h} index={idx} color={SCHOOL_PALETTE[idx]}")
