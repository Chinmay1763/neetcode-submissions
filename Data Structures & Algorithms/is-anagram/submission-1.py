class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #If the length of both the strings is different, return false
        # if len(s) != len(t):
        #     return False

        # #Declare the hashmaps for both the strings
        # countS, countT = {}, {}

        # #Iterate through the string s and t paralely as both are of same legth 
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0) #Increment the counter for s, if not found add in the hashmap with default value 0 
        #     countT[t[i]] = 1 + countT.get(t[i], 0) #Increment the counter for t, if not found add in the hashmap with default value 0

        # #Iterate through countS hasmap and see if it matches countT hashmap, if not return false
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False

        # #if passed everything, return true
        # return True

        return Counter(s) == Counter(t)
