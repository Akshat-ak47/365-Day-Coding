// Sum of 7s Multiple

// Problem Description
// Given a range [A, B], find sum of integers divisible by 7 in this range.


public class p106_sum_of_7_mult {
    public long solve(int A, int B) {
        long start = A % 7 == 0 ? A : A + (7 - A % 7);
        long end = B - B % 7;
        long n = (end - start) / 7 + 1;

        long sum = n * (start + end) / 2;
        return sum;
    }

    public static void main(String[] args) {
        p106_sum_of_7_mult sol = new p106_sum_of_7_mult();
        int A = 1;
        int B = 7;
        System.out.println(sol.solve(A, B));
    }
}
