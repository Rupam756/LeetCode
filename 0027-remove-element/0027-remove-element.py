class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        i = 0

        for j in range(len(nums)):

            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna