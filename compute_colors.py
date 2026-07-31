SCHOOL_PALETTE = [
    "#0072B2", # blue
    "#D55E00", # vermillion
    "#009E73", # green
    "#CC79A7", # pink
    "#E69F00", # orange
    "#F0E442", # yellow
    "#7570B3", # purple
    "#A6761D", # brown/ochre
    "#E7298A", # magenta
    "#66A61E", # lime
    "#8C564B", # muted brown
    "#E6AB02", # gold
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
        return "#0072B2"
    if "彰化" in key:
        return "#D55E00"
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return SCHOOL_PALETTE[h % len(SCHOOL_PALETTE)]

labels = ["台中市", "彰化縣", "市立高雄高商"]
for lbl in labels:
    print(lbl + " -> " + stableColor(lbl))
