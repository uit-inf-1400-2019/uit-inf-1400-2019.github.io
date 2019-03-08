def len_simple(lst):
    """Returns the length of a list."""
    return len(lst)

# TODO: change this to recursively find the length of a list
def len_recursive(lst):
    pass

def max_simple(lst):
    """Returns the largest item of a list."""
    return max(lst)

# TODO: change this to recursively find the largest item in a list.
def max_recursive(lst):
    pass

# TODO: similar to the above, but stop examining the list if the number 4 is reached.
def max_recursive_unless_4(lst):
    pass


def test_functions():
    lst = [1, 3, 6, 4, 9, 3]
    print("lst is ", lst)
    print("Len  (simple)              ", len_simple(lst))
    print("Len  (recursive)           ", len_recursive(lst))
    print("Max  (simple)              ", max_simple(lst))
    print("Max  (recursive)           ", max_recursive(lst))
    print("Max  (recursive, unless 4) ", max_recursive_unless_4(lst))

test_functions()
