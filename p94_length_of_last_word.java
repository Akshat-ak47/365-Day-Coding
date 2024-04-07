// Length of Last Word

// Problem Description
// Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
// If the last word does not exist, return 0.
// Note: A word is defined as a character sequence consists of non-space characters only.

// Example Input
// Input 1:
// A = " hello world "'
// Output 1:
// 5

public class p94_length_of_last_word {
    public int lengthOfLastWord(final String A) {
        int length = 0;
        boolean wordstart = false;
        
        for (int i=A.length()-1; i>=0; i--){
            if(A.charAt(i) != ' '){
                wordstart = true;
                length ++;
            } else {
                if (wordstart) {
                    break;
                }
            }
        }
        return length;
    }

    public static void main (String [] args){
        p94_length_of_last_word solution = new p94_length_of_last_word();
        String input1 = " hello world ";
        int output1 = solution.lengthOfLastWord(input1);
        System.out.println("Input: " + input1);
        System.out.println("Output: " + output1);
    }
}