def validate_length(n, arr):
    return  len(arr) == n
    
def validate_numbers(arr):
    return all(abs(i) < 10**9 for i in arr)
    