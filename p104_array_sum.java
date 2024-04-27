// Array Sum

// Problem Description
// You are given two numbers represented as integer arrays A and B, where each digit is an element.
// You have to return an array which representing the sum of the two given numbers.
// The last element denotes the least significant bit, and the first element denotes the most significant bit.
// Note : Array A and Array B can be of different size. ( i.e. length of Array A may not be equal to length of Array B ).

public class p104_array_sum {
    public int[] addArrays(int[] A, int[] B) {
        int n = Math.max(A.length, B.length);
        int[] result = new int[n + 1];
        int carry = 0;

        for (int i = 0; i < n; i++) {
            int sum = carry;
            if (i < A.length) sum += A[A.length - 1 - i];
            if (i < B.length) sum += B[B.length - 1 - i];

            result[n - i] = sum % 10;
            carry = sum / 10;
        }
        if (carry > 0) {
            result[0] = carry;
        } else {
            int[] trimmedResult = new int[n];
            System.arraycopy(result, 1, trimmedResult, 0, n);
            result = trimmedResult;
        }

        return result;
    }
    public static void main(String[] args) {
        p104_array_sum solution = new p104_array_sum();

        int[] A = {2, 1, 8, 9, 5};
        int[] B = {6, 7, 6, 7, 4, 1, 3, 0, 1, 8};
        int[] result = solution.addArrays(A, B);

        System.out.print("Result: ");
        for (int digit : result) {
            System.out.print(digit + " ");
        }
        System.out.println();
    }
}
