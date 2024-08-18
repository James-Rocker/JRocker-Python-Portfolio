def digital_root(n):
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n


if __name__ == "__main__":
    print(digital_root(27895))
