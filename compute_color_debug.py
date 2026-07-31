SCHOOL_PALETTE = [
    "#FF8A9A", "#FFCC99", "#FFFB8F", "#7FE0A8", "#7FBFFB", "#CFCFF7",
    "#F9D7B0", "#A8D2B0", "#EA9A9A", "#9FA0FF", "#7EDFD1", "#F4BFC0",
    "#FFD1CC", "#DFFFE0", "#FFE8D8", "#BEEFF0", "#FFD9B0", "#CFCFF0",
    "#E8CCFF", "#BFDFF9",
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
