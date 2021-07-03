"""
Tower of hanoi solution
"""


def move_tower(disks, from_pole, to_pole, with_pole):
    """
    side note, I hate the tower of hanoi and anyone who thinks this should be used
    to teach recursion should not be allowed to teach recursion.
    if I ever see someone had a pr to do recursion by using itself I would reject it immediately
    """
    if disks >= 1:
        # Move discs from from_tower of height-1 to an intermediate pole
        # you'll notice the disks quantity go down twice here
        # this is because when calling the function within the function,
        # So this will occur until the disks count is 0
        move_tower(disks - 1, from_pole, with_pole, to_pole)

        print(f"moving disk from {from_pole} to {to_pole}")

        # once we get to this call, the disks should 0
        move_tower(disks - 1, with_pole, to_pole, from_pole)


move_tower(3, "A", "B", "C")
