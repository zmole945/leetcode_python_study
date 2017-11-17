
nums = [3, 2, 4];
target = 6;

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)) :
            print "i=" + str(i);
            for j in range(i+1, len(nums)) :
                print "j=" + str(j);
                if nums[i] + nums[j] == target :
                    return [i, j];
a=Solution();

print a.twoSum(nums, target);

