nested_list = [['Hello', 'World'], ['Goodbye', 'World']]
nested_list = [[s.upper() for s in xs] for xs in nested_list]
print(nested_list)
