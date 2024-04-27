// Count Element Occurence

// Given a sorted array of integers, find the number of occurrences of a given target value.
// Your algorithm’s runtime complexity must be in the order of O(log n).
// If the target is not found in the array, return 0

// **Example : *
// Given [5, 7, 7, 8, 8, 10] and target value 8,
// return 2.

public class p113_cout_element_occurence {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int findCount(final int[] A, int B) {
        int n = A.length;
        int count = 0;
        int low = 0;
        int high = n - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2; 
            
            if (A[mid] == B) {
                count++;
                
                int left = mid - 1;
                while (left >= 0 && A[left] == B) {
                    count++;
                    left--;
                }
                
                int right = mid + 1;
                while (right < n && A[right] == B) {
                    count++;
                    right++;
                }
                return count;
            } else if (A[mid] < B) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        p113_cout_element_occurence solution = new p113_cout_element_occurence();
        int[] array = {5, 7, 7, 8, 8, 10};
        int target = 8;
        int result = solution.findCount(array, target);
        System.out.println("Number of occurrences of " + target + " is: " + result);
    }
}
