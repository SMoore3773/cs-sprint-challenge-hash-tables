
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # initialize result array, hash table, and length variable
    result = []
    length = len(a)
    table = [None] * length

    # populate hash table with all values from array
    for i in a:
        index = hash(i) % length
        table[index] = i

    # loop through all values in array
    for i in a:
        # check for negative number
        if i < 0:
            # hash the absolute value of the negative number and check it against the keys in the hash table
            if hash(abs(i)) in table:
                # if hash of the absolute value of the negative is in the hash table, then append the absolute value of the negative to the result array
                result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
