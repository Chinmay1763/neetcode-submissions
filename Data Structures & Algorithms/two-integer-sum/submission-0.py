class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #declare a hasmap
        hashmap = {}

        #iterate through array
        for i, n in enumerate(nums):
            #calculate the complement
            diff = target - n
            #check if complement exists in hashmap
            if diff in hashmap:
                #if yes, return the index
                return [hashmap[diff], i]
            #if no add it to the hashmap
            hashmap[n] = i