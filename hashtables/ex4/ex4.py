
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    length = len(a)
    table = [None] * length

    for i in a:
        index = hash(i) % length
        table[index] = i

    for i in a:
        if i < 0:
            if hash(abs(i)) in table:
                result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
