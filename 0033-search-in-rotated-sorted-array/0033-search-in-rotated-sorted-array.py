class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # If target is outside this sorted left half, search the right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # Otherwise, search the left half
                else:
                    r = mid - 1

            # Otherwise, the right half must be sorted
            else:
                # If target is outside this sorted right half, search the left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # Otherwise, search the right half
                else:
                    l = mid + 1
                    
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna