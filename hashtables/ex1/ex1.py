def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # set weights to a dictionary of weights with the value as the index of the list
    dictWeights = {val: ind for ind, val in enumerate(weights)}
    print(dictWeights)
    print('limit', limit)
    for item in dictWeights:
        print('item', item)
        second = limit - item
        print('second', second)
        if len(dictWeights) < length:
            return (dictWeights[item], 0)
        if second in dictWeights:
            if dictWeights[item] >= dictWeights[second]:
                print(dictWeights[item], dictWeights[second])
                return(dictWeights[item], dictWeights[second])
            else:
                return (dictWeights[second], dictWeights[item])
    return None
