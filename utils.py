from constants import SIGNS

def to_absolute(sign, deg, minute, second):
    return SIGNS.index(sign)*30 + deg + minute/60 + second/3600

def normalize(angle):
    return angle % 360

def to_dms(angle):
    angle = normalize(angle)
    sign = SIGNS[int(angle // 30)]
    deg = int(angle % 30)
    minute_float = (angle % 1) * 60
    minute = int(minute_float)
    second = round((minute_float - minute) * 60, 2)
    return sign, deg, minute, second
