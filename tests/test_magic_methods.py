from technical_exercises import magic_methods


def test_distance_class():
    magic_methods.Distance()
    d1 = magic_methods.Distance(3, 10)
    d2 = magic_methods.Distance(4, 4)
    assert str(d1 + d2) == "8ft 2in"


def test_get_random_val_class():
    list_of_numbers = list(range(1))

    a = magic_methods.GiveRandomVal(list_of_numbers)
    assert a[0] == 0


def test_set_item_class():
    setitem_instance = magic_methods.SetItem([1, 2, 3])
    assert setitem_instance.item == [1, 2, 3]
    setitem_instance[1] = 5
    assert setitem_instance.item == [1, 5, 3]


def testing_vectors():
    foo = magic_methods.Vector2D(3, 4)
    bar = magic_methods.Vector2D(-9, 7)
    assert (foo - bar) == magic_methods.Vector2D(x=12, y=-3)
    assert (foo + bar) == magic_methods.Vector2D(x=-6, y=11)
    assert (foo * bar) == magic_methods.Vector2D(x=magic_methods.Vector2D(x=-27, y=21), y=magic_methods.Vector2D(x=-36, y=28))
