def multiple_returns(sentence):
    length = len(sentence)
    if length== 0:
        return None
    else:
        for i in sentence:
            print ("Length: {:d} - First character: {}".format(length, sentence[0]))
        