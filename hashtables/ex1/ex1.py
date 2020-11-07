def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # set weights to a dictionary of weights with the value as the index of the list
    dictWeights = {val: ind for ind, val in enumerate(weights)}

    for item in dictWeights:
        # sets value for second item to search dictionary
        second = limit - item
        # edge case for duplicate item
        if len(dictWeights) < length:
            return (dictWeights[item], 0)
        # for if matching package is found
        if second in dictWeights:
            if dictWeights[item] >= dictWeights[second]:
                # case where item index is greater than second index
                return(dictWeights[item], dictWeights[second])
            else:
                # case where second index is greater than item index
                return (dictWeights[second], dictWeights[item])
    return None
