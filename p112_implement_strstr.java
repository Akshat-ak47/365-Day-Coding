// Implement StrStr
/*
Problem Description
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
Implement strStr().
strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
NOTE: String A is haystack, B is needle.

Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.

Example Input
Input 1:
A = "strstr"
B = "str"
Input 2:
A = "bighit"
B = "bit"

Example Output
Output 1:
0
Output 1:
-1

*/
public class p112_implement_strstr {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int strStr(final String A, final String B) {
        if (B.isEmpty()){
            return -1;
        }
        for (int i=0; i <= A.length()-B.length(); i++){
            if (A.substring(i, i+B.length()).equals(B)){
                return i;
            }
        }
        return -1;
    }
    public static void main(String [] args){
        p112_implement_strstr a = new p112_implement_strstr();
        String A = "strstr";
        String B = "str";
        int res = a.strStr(A, B);
        System.out.println(res);

        String C = "botbit";
        String D = "bit";
        int result = a.strStr(C, D);
        System.out.println(result);
    }
}
