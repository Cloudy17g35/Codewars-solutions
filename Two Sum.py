def two_sum(numbers, target):
	
    hashMap = {}
    
    for i,number in enumerate(numbers):
        difference = target - number
        
        if difference in hashMap:
            return hashMap[difference], i
        else:
            hashMap[number] = i
