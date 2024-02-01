def count_common_elements(list_a, list_b):
    common_elements = set(list_a) & set(list_b)
    return len(common_elements)
def get_integer_list_from_user():
    return [int(x) for x in input("Enter elements (space-separated): ").split()]
# Get user input for lists
list_a = get_integer_list_from_user()
list_b = get_integer_list_from_user()
# Call the function to count common elements
common_count = count_common_elements(list_a, list_b)
# Print the result
print(f"Number of Common Elements: {common_count}")
