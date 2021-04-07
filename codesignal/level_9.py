# 38
import math


def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight-downSpeed) / (upSpeed-downSpeed))


# 39
