def solution(time):
    hour, minutes = time.split(':')[0], time.split(':')[1]
    if (0 <= int(hour) < 24) and (0 <= int(minutes) < 60):
        return True
    return False
