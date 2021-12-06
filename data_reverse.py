# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 11111111  00000000  00001111  10101010
# (byte1)   (byte2)   (byte3)   (byte4)

# should become:

#10101010  00001111  00000000  11111111
#(byte4)   (byte3)   (byte2)   (byte1)



def data_reverse(data):
    
    # setting first index as length of list
    # second index is list length minus 8 (because single byte is 8 bytes long)
    
    first, last = len(lst), len(lst) - 8
    
    
    # new list to store results
    new_lst = []
    
    # iterating over list
    for i in range(0, len(data), 8):
        # extending new reversed data
        new_lst.extend(data[last:first])
        
        # first becoming last and lasst is decreased by 8
        first, last = last, last - 8
    
    # returning final result
    return new_lst
