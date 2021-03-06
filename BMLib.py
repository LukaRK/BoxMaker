
#: Multiple of notch height
IDEAL_NOTCH_WIDTH = 4


def genFrontPoints(w, h, d, t):
    PList=list()
    PList.extend(genHorizontalLinePoints(0, 0, w, t, 0))
    PList.extend(genVerticalLinePoints(w, 0, h, -t, 0))
    PList.extend(genHorizontalLinePoints(w, h, -w, -t, 0))
    PList.extend(genVerticalLinePoints(0, h, -h, t, 0))
    return PList


def genBackPoints(w, h, d, t):
    return genFrontPoints(w, h, d, t)


def genLeftPoints(w, h, d, t):
    PList=list()
    PList.extend(genHorizontalLinePoints(0, 0, -d, t, -t))
    PList.extend(genVerticalLinePoints(-d + t, 0, h, -t, 0))
    PList.extend(genHorizontalLinePoints(-d, h, d, -t, t))
    PList.extend(genVerticalLinePoints(-t, h, -h, t, 0))
    return PList



def genRightPoints(w, h, d, t):
    return genLeftPoints(w, h, d, t)


def genBottomPoints(w, h, d, t):
    PList=list()
    PList.extend(genHorizontalLinePoints(0, -t, w, t, t))
    PList.extend(genVerticalLinePoints(w - t, 0, -d, t, -t))
    PList.extend(genHorizontalLinePoints(w, -d + t, -w, -t, -t))
    PList.extend(genVerticalLinePoints(t, -d, d, -t, t))
    return PList


def genTopPoints(w, h, d, t):
    return genBottomPoints(w, h, d, t)
    


def genHorizontalLinePoints(x, y, length, notchHeight, offset):
    idealNotch = abs(notchHeight) * IDEAL_NOTCH_WIDTH
    notchCount = int(abs(length) / idealNotch)

    if notchCount % 2 == 0:
        notchCount += 1

    notchWidth = length / notchCount

    # First point
    yield (x + offset, y)

    # Two points for every side of a notch
    for i in range(1, notchCount):
        x = x + notchWidth
        yield (x, y if ((i % 2) == 1) else y + notchHeight)
        yield (x, y if ((i % 2) == 0) else y + notchHeight)

    # Last point is omitted (because it will be the first point of the next side)


def genVerticalLinePoints(x, y, length, notchHeight, offset):
    # Symmetrical with the horizontal version, but with x & y swapped
    points = genHorizontalLinePoints(y, x, length, notchHeight, offset)
    for y, x in points:
        yield (x, y)
