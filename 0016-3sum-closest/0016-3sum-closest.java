import java.util.*;

class Solution {
    public int threeSumClosest(int[] nums, int target) {

        // Step 1: Sort the array
        Arrays.sort(nums);

        // Initialize with the first possible triplet
        int closestSum = nums[0] + nums[1] + nums[2];

        // Step 2: Fix the first element
        for (int i = 0; i < nums.length - 2; i++) {

            int left = i + 1;
            int right = nums.length - 1;

            // Step 3: Two-pointer approach
            while (left < right) {

                int sum = nums[i] + nums[left] + nums[right];

                // If we found the exact target
                if (sum == target) {
                    return sum;
                }

                // Update closest sum
                if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
                    closestSum = sum;
                }

                // If sum is smaller, increase it
                if (sum < target) {
                    left++;
                }

                // If sum is larger, decrease it
                else {
                    right--;
                }
            }
        }

        return closestSum;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna