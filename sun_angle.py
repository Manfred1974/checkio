def sun_angle(time):
    # replace this for solution
    (h, m) = time.split(':')
    result = int(h) * 3600 + int(m) * 60
    set_zero = result - 21600
    angle = (set_zero/240)
    if angle > 180 or angle < 0:
        return 'I don\'t see the sun!'
    else:
        return angle
