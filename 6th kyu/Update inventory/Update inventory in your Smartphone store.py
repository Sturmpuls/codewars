# https://www.codewars.com/kata/57a31ce7cf1fa5a1e1000227
def update_inventory(cur_stock, new_stock):

    result = {}

    for num, item in cur_stock + new_stock:
    
        if item in result:
            result[item] += num
            
        else:
            result[item] = num
            
    return [(result[item], item) for item in sorted(result)]
