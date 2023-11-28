word = "Holberton"
print("First 3 letters: {}".format(word[0:3]))
print("Last 2 letters: {}".format(word[7:]))
print("Middle word: {}".format(word[1:8]))
print("First 3 letters: {}".format(word[0:3].replace('Hol',"Sch")))
print("Last 2 letters: {}".format(word[7:].replace('on',"ol")))
print("Middle word: {}".format(word[1:8].replace('olberto',"choo")))
