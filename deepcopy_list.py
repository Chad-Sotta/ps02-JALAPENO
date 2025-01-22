import copy

nested_list = [[0, 1], [3, 4]]
alias_nested = nested_list
alias_nested[0][1] = 99
deep_copy = copy.deepcopy(nested_list)
deep_copy[0][1] = 2

print("Original nested list:", nested_list)
print("Aliased nested list:", alias_nested)
print("Deep copied nested list", deep_copy)