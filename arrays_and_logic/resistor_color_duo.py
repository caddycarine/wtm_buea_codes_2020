def value(colors):
    colours = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return int(''.join([str(colours.index(c)) for c in colors[:2]]))
