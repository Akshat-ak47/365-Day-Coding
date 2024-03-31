// '''
// Add Binary Strings

// Problem Description
// Given two binary strings A and B. Return their sum (also a binary string).

// Input Format
// The two argument A and B are binary strings.
// Output Format
// Return a binary string denoting the sum of A and B

// Example Input
// Input 1:
// A = "100"
// B = "11"
// Input 2:
// A = "110"
// B = "10"

// Example Output
// Output 1:
// "111"
// Output 2:
// "1000"

public class p91_add_binary_string {
    public String addBinary(String A, String B) {
        int i = A.length() - 1;
        int j = B.length() - 1;
        int carry = 0;
        StringBuilder result = new StringBuilder();

        while (i >= 0 || j >= 0 || carry == 1) {
            int sum = carry;
            if (i >= 0) {
                sum += A.charAt(i--) - '0';
            }
            if (j >= 0) {
                sum += B.charAt(j--) - '0';
            }

            result.insert(0, sum % 2);
            carry = sum / 2;
        }

        return result.toString();
    }

    public static void main(String[] args) {
        p91_add_binary_string solution = new p91_add_binary_string();
        System.out.println(solution.addBinary("100", "11"));
        System.out.println(solution.addBinary("110", "10"));
    }
}
