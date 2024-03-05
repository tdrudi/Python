def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    replaced = ''

    for char in phrase:
        if char.lower() == to_swap:
            char = char.swapcase()
        replaced += char
    return replaced


    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
