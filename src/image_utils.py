from scipy import ndimage


def getMainColor(fileName):
    testFile = fileName

    image = ndimage.imread(testFile)

    rgb = {}

    for h in range(0, image.shape[0]):
        for w in range(0, image.shape[1]):
            key = str("%03d" % (image[h][w][0])) + str("%03d" % (image[h][w][1])) + str("%03d" % (image[h][w][2]))
            if key in rgb.keys():
                rgb[key] += 1
            else:
                rgb[key] = 1
    first = {"key": "", "count": 0}
    second = {"key": "", "count": 0}
    for key in rgb.keys():
        if rgb[key] > first["count"]:
            second = first.copy()
            first["count"] = rgb[key]
            first["key"] = key
        else:
            if rgb[key] > second["count"]:
                second["count"] = rgb[key]
                second["key"] = key
    return first["key"], second["key"]