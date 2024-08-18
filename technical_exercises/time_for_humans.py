def make_readable(seconds: int):
    if seconds <= 359999:
        hours = seconds // (60 * 60)
        minutes = seconds % (60 * 60) // 60
        seconds = seconds % 60
        return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    else:
        return "99:59:59"


if __name__ == "__main__":
    print(make_readable(5))
    print(make_readable(3500))
    print(make_readable(359998))
    print(make_readable(9000000))
