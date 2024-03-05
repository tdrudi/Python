def two_oldest_ages(ages):
    ages_list = set(ages)
    oldest_age = None
    second_oldest = None

    for age in ages_list:
        if oldest_age is None or age > oldest_age:
            second_oldest = oldest_age
            oldest_age = age
        elif second_oldest is None or age > second_oldest:
            second_oldest = age
    return (second_oldest, oldest_age)


    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.