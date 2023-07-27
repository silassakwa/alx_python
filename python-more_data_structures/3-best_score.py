def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    best_keys = [key for key, score in a_dictionary.items() if score == max_score]
    return best_keys[0]
#!/usr/bin/python3
best_score = __import__('3-best_score').best_score
# Test case
my_dict = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
best_key = best_score(my_dict)
print("Best:", best_key)