def pastClock(h, m, s):
    hour = 60 * 60 * 1000
    min = 60 * 1000
    sec = 1000
    timepast = (h* hour +m* min + s*sec)
    return timepast

pastClock(0,1,1)
