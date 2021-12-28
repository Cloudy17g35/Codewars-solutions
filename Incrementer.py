
'''codewars.com/kata/590e03aef55cab099a0002e8'''

def incrementer(nums):
    return [(nums[i] + (i + 1)) % 10 for i in range(len(nums))]
