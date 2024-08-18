times = [
    ("year", 365 * 24 * 60 * 60),
    ("day", 24 * 60 * 60),
    ("hour", 60 * 60),
    ("minute", 60),
    ("second", 1),
]


def format_duration(seconds):
    if not seconds:
        return "now"

    time_chunks = []
    for time_name, time_units in times:
        time_quantity = seconds // time_units
        if time_quantity:
            if time_quantity > 1:
                time_name += "s"
            time_chunks.append(str(time_quantity) + " " + time_name)

        seconds = seconds % time_units

    if len(time_chunks) > 1:
        return ", ".join(time_chunks[:-1]) + " and " + time_chunks[-1]
    else:
        return time_chunks[0]


if __name__ == "__main__":
    print(format_duration(22222))
    print(format_duration(1))
    print(format_duration(231))
    print(format_duration(222225555222))
