# Update the dictionary with the new key-value pairs, the new key-value pairs will be added to the dictionary.
# If the key already exists in the dictionary, the value will be updated.   
# if the key dose not appear in the new dictionary, it will remain unchanged in the original dictionary.
prices = {
    'apple': 0.40,
    'banana': 0.50
}

new_prices = {
    'apple': 0.41,
    'berry': 0.80
}

prices.update(new_prices)
print(prices)