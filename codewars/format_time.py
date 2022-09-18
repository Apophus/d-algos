def format_duration(seconds):
    # your code here
    """
    * For seconds = 62, your function should return 
        "1 minute and 2 seconds"
    * For seconds = 3662, your function should return
        "1 hour, 1 minute and 2 seconds"

    For the purpose of this Kata, a year is 365 days and a day is 24 hours.

    """
    formatted_time = ''
    if not seconds:
        return 'now'

    time_Scale = {
        'year': 365 * 24 * 60 * 60,
        'day': 24 * 60 * 60,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    places = []
    names = []
    for name, duration in time_Scale.items():
        time_, remainder = divmod(seconds, duration)

        if time_:
            suffix = name if time_ == 1 else name + 's'
            places.append(time_)
            names.append(suffix)
            #formatted_time += f'{time_} {suffix}' if not remainder else f'{time_} {suffix} '

            seconds = remainder

    blocks = list(zip(places, names))

    if len(blocks) == 1:
        formatted_time += f'{blocks[0][0]} {blocks[0][1]}'
    elif len(blocks) == 2:
        formatted_time += f'{blocks[0][0]} {blocks[0][1]} and {blocks[1][0]} {blocks[1][1]}'
    elif len(blocks) == 3:
        formatted_time \
            += f'{blocks[0][0]} {blocks[0][1]}, {blocks[1][0]} {blocks[1][1]} and {blocks[2][0]} {blocks[2][1]}'

    elif len(blocks) == 4:
        formatted_time \
            += f'{blocks[0][0]} {blocks[0][1]}, {blocks[1][0]} {blocks[1][1]}, {blocks[2][0]} {blocks[2][1]} and {blocks[3][0]} {blocks[3][1]}'
    else:
        formatted_time = f'{blocks[0][0]} {blocks[0][1]}, {blocks[1][0]} {blocks[1][1]}, {blocks[2][0]} {blocks[2][1]}, {blocks[3][0]} {blocks[3][1]} and {blocks[4][0]} {blocks[4][1]}'

    return formatted_time


if __name__ == '__main__':
    res = format_duration(120)
    print(res)
