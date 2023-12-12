def update_and_print_sorted_dict(a_dictionary, key, value):
    a_dictionary[key] = value
    sorted_keys = sorted(a_dictionary.keys())
    
    for k in sorted_keys:
        print("{}: {}".format(k, a_dictionary[k]))
        
