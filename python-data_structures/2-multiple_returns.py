def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        sentence = ''
        length = len(sentence)
        first = sentence([0][0])
        for i in sentence:
            print("Length: {:d} - First character: {}".format(length, first))
        