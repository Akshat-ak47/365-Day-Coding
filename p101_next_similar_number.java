// Next Similar Number

// Problem Description

// Given a number A in a form of string.

// You have to find the smallest number that has same set of digits as A and is greater than A.

// If A is the greatest possible number with its set of digits, then return -1.

import java.util.Arrays;

public class p101_next_similar_number {
    public String solve(String A) {
        char[] digits = A.toCharArray();
        int i = digits.length - 2;
        while(i >= 0 && digits[i] >= digits[i + 1]){
            i--;
        }
        if (i>=0) {
            int j=digits.length-1;
            while(j>i && digits[j] <= digits[i]) {
                j--;
            }
            char temp = digits[i];
            digits[i] = digits[j];
            digits[j] = temp;
            
            Arrays.sort(digits, i+1, digits.length);
            
            return new String(digits);
        } else {
            return "-1";
        }
    }
}

