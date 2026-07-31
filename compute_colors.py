SCHOOL_PALETTE = [
    "#FFB3BA", # pastel pink
    "#FFDFBA", # pastel peach
    "#FFFFBA", # pastel yellow
    "#BAFFC9", # pastel mint
    "#BAE1FF", # pastel baby blue
    "#E6E6FA", # lavender
    "#FDEBD0", # cream
    "#D5E8D4", # pale green
    "#F4C2C2", # rose
    "#C9C9FF", # pale purple
    "#B2F0E6", # aqua
    "#FADADD", # light rose
    "#FFE4E1", # misty rose
    "#F0FFF0", # honeydew
    "#FFF5EE", # seashell
    "#E0FFFF", # light cyan
    "#FFEFD5", # papaya
    "#E8EAF6", # very light indigo
    "#F6E6FF", # light magenta
    "#E3F2FD", # soft sky
]


def stableColor(label):
    if not label:
        return "#94A3B8"
    key = str(label)
    if key == "未填":
        return "#94A3B8"
    if key == "其他":
        return "#A855F7"
    if "台中" in key:
        return "#BAE1FF"
    if "彰化" in key:
        return "#C9C9FF"
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return SCHOOL_PALETTE[h % len(SCHOOL_PALETTE)]

labels = ["台中市", "彰化縣", "市立高雄高商"]
for lbl in labels:
    print(lbl + " -> " + stableColor(lbl))
