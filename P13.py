# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method) 
# [1, 2, 3, 2, 1] [1, “abc”, “abc”, 1]
def is_palindrome(lst):
    # Create a copy of the original list
    lst_copy = lst.copy()
    # Reverse the copied list
    lst_copy.reverse()
    # Check if the original list is the same as the reversed list
    return lst == lst_copy

# Test cases
print(is_palindrome([1, 2, 3, 2, 1]))  
print(is_palindrome([1, "abc", "abc", 1]))  
print(is_palindrome([1, 2, 3, 4, 5]))