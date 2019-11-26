# https://www.codewars.com/kata/55983863da40caa2c900004e
def next_bigger(n):
    arr = list(str(n))
    if len(arr) <= 1:
        return -1
    
    for i in range(-2, -(len(arr) + 1), -1):
    
        if arr[i] < arr[i+1]:
        
            for j in range(-1, i, -1):
            
                if arr[j] > arr[i]:
                
                    arr[i], arr[j] = arr[j], arr[i]
                    break
        
            arr[i+1:] = sorted(arr[i+1:])

            return int(''.join(arr))

    return -1
