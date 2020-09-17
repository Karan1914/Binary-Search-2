class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # index of left element
        
        for i in range(0,len(nums)):
            if nums[i] == target:
                left_idx = i
                break
                
        else:
            return [-1,-1]
        
        # find right element
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                right_idx = j
                break
                
        return [left_idx,right_idx]
    
    
    # Time Complexity :  O(n) as we are using for loop (linear time search)
    # Space Complexity : O(1) no extra space is used 
    
    # Comments: I wanted to use binary search , but stuck how to find right index after finding left index using binary search 