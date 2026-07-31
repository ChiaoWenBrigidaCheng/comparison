SCHOOL_PALETTE = [
    "#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#E6E6FA",
    "#FDEBD0", "#D5E8D4", "#F4C2C2", "#C9C9FF", "#B2F0E6", "#FADADD",
    "#FFE4E1", "#F0FFF0", "#FFF5EE", "#E0FFFF", "#FFEFD5", "#E8EAF6",
    "#F6E6FF", "#E3F2FD",
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
