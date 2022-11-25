def likes(names):
    name_count = len(names)
    if name_count == 0:
        return "no one likes this"
    elif name_count == 1:
        return f"{names[0]} likes this"
    elif name_count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif name_count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    pass


print(likes([]))
print(likes(["Sarah", "Ryan", "Jeff"]))
print(likes(["Sarah", "Ryan", "Jeff", "Katie", "Max"]))
