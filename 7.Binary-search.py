A = [-3, -2 , -1, 0, 1, 2]

# traditional binary search - looking up if a number is in array:
# time O(log n)
# space O(1)

def binary_search(arr, target):
    n = len(arr)
    L = 0
    R = n - 1
    
    while(L <= R):
        M = L + ((R - L) // 2)
        
        if arr[M] == target:
            return True
        
        elif target < arr[M]:
            R = M - 1
        
        else:
            L = M + 1
    
    return False

binary_search(A, -3) 
        
# conditional based binary search 

B = [False, False, False, True, True, True, True]

def conditional_binary_search(arr):
    n = len(arr)
    L = 0
    R = n - 1
    
    while(L < R):
        M = (R + L) // 2
        if arr[M]:
            R = M
        else:
            L = M + 1
    
    return L # or R 

conditional_binary_search(B)