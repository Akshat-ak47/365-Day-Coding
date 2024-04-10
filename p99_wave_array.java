// Wave Array

// Problem Description
// Given an array of integers A, sort the array into a wave-like array and return it. 
// In other words, arrange the elements into a sequence such that

// a1 >= a2 <= a3 >= a4 <= a5.....

// NOTE: If multiple answers are possible, return the lexicographically smallest one.

import java.util.ArrayList;
import java.util.Collections;

public class p99_wave_array {
    public ArrayList<Integer> wave(ArrayList<Integer> A) {
        Collections.sort(A);
        
        for (int i = 0; i < A.size() - 1; i += 2) {
            Collections.swap(A, i, i + 1);
        }
        return A;
    }
    public static void main(String[] args) {
        p99_wave_array solution = new p99_wave_array();

        ArrayList<Integer> input = new ArrayList<>();
        input.add(1);
        input.add(3);
        input.add(2);
        input.add(4);
        input.add(5);
        
        ArrayList<Integer> result = solution.wave(input);
        System.out.println(result);
    }
}
