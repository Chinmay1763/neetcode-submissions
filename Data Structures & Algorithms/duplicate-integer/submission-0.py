class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #declare a hashset
        hashset = set()

        #iterate through the list of integers
        for i in nums:
            #Check if the integer pre-exists in the hashset
            if i in hashset:
                #if yes, then return true
                return True
            #if not then add that distinct integer into the hashset
            hashset.add(i)
        #After traversing all the integers list, if none found then return false
        return False