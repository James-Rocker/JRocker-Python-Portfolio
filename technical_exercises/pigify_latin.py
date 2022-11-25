def pig_it(text: str):
    new_str = ""
    for word in text.split(" "):
        if word in "!.%&?":
            new_str = f"{new_str} {word}"
        else:
            new_str = f"{new_str} {word[1:] + word[0]}ay"
    return new_str.strip(" ")


print(pig_it("hello my name is james"))
print(pig_it("We are making this into a secret code !"))
