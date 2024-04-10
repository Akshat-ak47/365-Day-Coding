// Jump Game Array

// Given an array of non-negative integers, A, you are initially positioned at the 0th index of the array.
// Each element in the array represents your maximum jump length at that position.
// Determine if you are able to reach the last index.

// Input Format:
// The first and the only argument of input will be an integer array A.

// Output Format:
// Return an integer, representing the answer as described in the problem statement.
//     => 0 : If you cannot reach the last index.
//     => 1 : If you can reach the last index.

// Input 1:
//     A = [2,3,1,1,4]
// Output 1:
//     1
// Explanation 1:
//     Index 0 -> Index 2 -> Index 3 -> Index 4

// Input 2:
//     A = [3,2,1,0,4]
// Output 2:
//     0
// Explanation 2:
//     There is no possible path to reach the last index.
import java.util.ArrayList;

public class p98_jump_game_array {
    public int canJump(ArrayList<Integer> A) {
        int furthestIndex = 0;
        int n = A.size();
        
        for (int i = 0; i < n; i++) {
            if (i > furthestIndex) {
                return 0;
            }
            furthestIndex = Math.max(furthestIndex, i + A.get(i));
            
            if (furthestIndex >= n - 1) {
                return 1;
            }
        }
        
        return 0;
    }

    public static void main(String[] args) {
        p98_jump_game_array solution = new p98_jump_game_array();
        
        ArrayList<Integer> A1 = new ArrayList<>();
        A1.add(2);
        A1.add(3);
        A1.add(1);
        A1.add(1);
        A1.add(4);
        System.out.println(solution.canJump(A1));
        
        ArrayList<Integer> A2 = new ArrayList<>();
        A2.add(3);
        A2.add(2);
        A2.add(1);
        A2.add(0);
        A2.add(4);
        System.out.println(solution.canJump(A2));
    }
}
