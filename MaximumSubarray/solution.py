class Solution:
    def max_sub_array(self, nums):
        if not nums:
            return None

        current_sum = nums[0]
        max_sum = current_sum
        for i in range(1, len(nums)):
            if current_sum + nums[i] < nums[i]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum