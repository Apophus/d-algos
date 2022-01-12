def growingPlant(upSpeed, downSpeed, desiredHeight):

    height = 0
    days = 0
    while True:
        height += upSpeed
        days+=1
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days

print(growingPlant(6, 5, 10))