"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    phrase = phrase.split()
    letter_counts = {}

    # loops through phrase and adds word name to key with the length of the word. If no such key exists, it is created
    for word in phrase:
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] = letter_counts[letter] + 1
            else:
                letter_counts[letter] = 1

    most_used = []
    # loops through each key in the dictionary of usage counts and checks if it has the highest usage count.
    # if it does, it replaces the old elements in the list. If it is used as much as the currently most-used letter,
    # it is appended to the list.
    for key in letter_counts:
        if most_used == []:
            most_used.append(key)
        elif letter_counts[key] > letter_counts[most_used[0]]:
            most_used = [key]
        elif letter_counts[key] == letter_counts[most_used[0]]:
            most_used.append(key)

    return sorted(most_used)





def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    word_length = {}
    # checks if the length of the word is in the dictionary as a key, if so, appends the word to the value list,
    # if not, creates a key with the word as a single element of a list as a value. Sorts the value list each word.
    for word in words:
        key = len(word)
        if key in word_length:
            word_length[key].append(word)
        else:
            word_length[key] = [word]
        word_length[key].sort()

    # returns a sorted list of tuples taken from the key-value pairs in 'word_length'
    return sorted(word_length.items())


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
