# Write a Python function to reverse a list at a specific location.

def reverse_list_in_location(lst, start_pos, end_pos):
    while start_pos < end_pos:
        lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        start_pos += 1
        end_pos -= 1
    return lst