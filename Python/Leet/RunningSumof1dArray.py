
class Solution(object):
    nums = [1,2,3,4]
    def runningSum( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = []
        for x in nums :
            if ( len(n) > 0 ):
                n.append(((x) + n[len(n)-1]))            
            else :
                n.append(x)
        return(n)
        
    print( runningSum(nums))