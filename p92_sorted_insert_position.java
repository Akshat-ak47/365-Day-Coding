// Sorted Insert Position

// Problem Description
// Given a sorted array A and a target value B, return the index if the target is found.
// If not, return the index where it would be if it were inserted in order.
// You may assume no duplicates in the array.

// Example Input
// Input 1:
// A = [1, 3, 5, 6]
// B = 5

// Example Output
// Output 1:
// 2

import java.util.ArrayList;
import java.util.List;

public class p92_sorted_insert_position {
    public static int searchInsert(List<Integer> A, int B) {
        int l = 0, r = A.size(), mid;
        while (l < r) {
            mid = (l + r) / 2;
            if (A.get(mid) == B)
                return mid;
            if (A.get(mid) < B)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(3);
        nums.add(5);
        nums.add(6);
        int target = 5;
        System.out.println("Insert position of " + target + ": " + searchInsert(nums, target));
    }
}
