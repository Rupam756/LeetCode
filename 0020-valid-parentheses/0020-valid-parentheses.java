import java.util.Stack;

class Solution {
    public boolean isValid(String s) {

        // Create a stack to store opening brackets
        Stack<Character> stack = new Stack<>();

        // Traverse through every character
        for (char ch : s.toCharArray()) {

            // If it is an opening bracket, push it
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }

            // Otherwise, it is a closing bracket
            else {

                // If there is no opening bracket
                if (stack.isEmpty()) {
                    return false;
                }

                // Get the most recent opening bracket
                char top = stack.pop();

                // Check matching brackets
                if (ch == ')' && top != '(') {
                    return false;
                }

                if (ch == '}' && top != '{') {
                    return false;
                }

                if (ch == ']' && top != '[') {
                    return false;
                }
            }
        }

        // Stack must be empty for a valid string
        return stack.isEmpty();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna