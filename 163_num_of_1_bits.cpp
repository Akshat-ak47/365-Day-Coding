// Number of 1 Bits

// Write a function that takes the binary representation of a positive integer and returns the number of 
// set bits
//  it has (also known as the Hamming weight).

// Example 1:
// Input: n = 11
// Output: 3

// Explanation:
// The input binary string 1011 has a total of three set bits.

#include <bitset>

class Solution {
public:
    int hammingWeight(int n) {
        std::bitset<sizeof(int) * 8> bits(n);
        
        return bits.count();
    }
};