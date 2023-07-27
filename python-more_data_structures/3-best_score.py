def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    best_keys = [key for key, score in a_dictionary.items() if score == max_score]
    return best_keys, max_score

# Test case
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_keys, best_value = best_score(a_dictionary)
print(best_keys,":",best_value)
