// Highest Product

// Problem Description
// Given an array A, of N integers A.
// Return the highest product possible by multiplying 3 numbers from the array.
// NOTE: The solution will fit in a 32-bit signed integer.


import java.util.ArrayList;
import java.util.Collections;

public class p102_highest_product {
    public int maxp3(ArrayList<Integer> A) {
        Collections.sort(A);
        int n = A.size();
        
        // Case 1: All non-negative numbers
        int product1 = A.get(n - 1) * A.get(n - 2) * A.get(n - 3);
        
        // Case 2: Two smallest negative numbers and largest positive number
        int product2 = A.get(0) * A.get(1) * A.get(n - 1);
        
        // Return the maximum of the two products
        return Math.max(product1, product2);
    }

    public static void main(String[] args) {
        p102_highest_product solution = new p102_highest_product();
        ArrayList<Integer> testCase = new ArrayList<>();
        testCase.add(0);
        testCase.add(-1);
        testCase.add(3);
        testCase.add(100);
        testCase.add(-70);
        testCase.add(-50);
        int result = solution.maxp3(testCase);
        System.out.println("Result: " + result);
    }
}
