SCHOOL_PALETTE = [
    "#FF8A9A", # deeper pastel pink
    "#FFCC99", # deeper pastel peach
    "#FFFB8F", # deeper pastel yellow
    "#7FE0A8", # deeper pastel mint
    "#7FBFFB", # deeper baby blue
    "#CFCFF7", # deeper lavender
    "#F9D7B0", # deeper cream
    "#A8D2B0", # deeper pale green
    "#EA9A9A", # deeper rose
    "#9FA0FF", # deeper pale purple
    "#7EDFD1", # deeper aqua
    "#F4BFC0", # deeper light rose
    "#FFD1CC", # deeper misty rose
    "#DFFFE0", # deeper honeydew
    "#FFE8D8", # deeper seashell
    "#BEEFF0", # deeper light cyan
    "#FFD9B0", # deeper papaya
    "#CFCFF0", # deeper very light indigo
    "#E8CCFF", # deeper light magenta
    "#BFDFF9", # deeper soft sky
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
        return "#7FBFFB"
    if "彰化" in key:
        return "#9FA0FF"
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return SCHOOL_PALETTE[h % len(SCHOOL_PALETTE)]

labels = ["台中市", "彰化縣", "市立高雄高商"]
for lbl in labels:
    print(lbl + " -> " + stableColor(lbl))
