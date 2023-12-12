def best_score(a_dictionary):
    # Check if the dictionary is not empty
    if a_dictionary:
        # Find the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        # Return None if the dictionary is empty
        return None
    
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))


