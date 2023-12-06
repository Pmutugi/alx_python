def multiple_returns(sentence):
    length = len(sentence)
    first = sentence([0][0])
    if len(sentence)=="":
        return None
    else:
        for i in sentence:
            print("Length: {:d} - First character: {}".format(length, first))
        