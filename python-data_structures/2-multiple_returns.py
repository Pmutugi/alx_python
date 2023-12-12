def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first
if __name__=="__main__":
         
    sentence = "At Holberton school, I learnt C!"
    l, f = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(l, f))

