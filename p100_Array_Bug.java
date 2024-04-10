// ARRAY_BUG

// The following code is supposed to rotate the array A by B positions.

// So, for example,


// A : [1 2 3 4 5 6]
// B : 1

// The output :

// [2 3 4 5 6 1]
// However, there is a small bug in the problem. Fix the bug and submit the problem.
import java.util.ArrayList;

public class p100_Array_Bug {
    public ArrayList<Integer> rotateArray(ArrayList<Integer> A, int B) {
		ArrayList<Integer> ret = new ArrayList<Integer>();
        B = B % A.size();
		for (int i = 0; i < A.size(); i++) {
            int newIndex = (i+B)%A.size();
			ret.add(A.get(newIndex));
		}
		return ret;
	}
    public static void main(String[] args) {
        p100_Array_Bug solution = new p100_Array_Bug();

        // Test case
        ArrayList<Integer> A = new ArrayList<>();
        A.add(1);
        A.add(2);
        A.add(3);
        A.add(4);
        A.add(5);
        A.add(6);
        int B = 1;

        ArrayList<Integer> rotatedArray = solution.rotateArray(A, B);
        System.out.println(rotatedArray);
    }
}
