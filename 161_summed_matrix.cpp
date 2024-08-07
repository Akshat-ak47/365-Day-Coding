// Summed Matrix

// A matrix is constructed of size n*n and given an integer ‘q’. The value at every cell of the matrix is given as, M(i,j) = i+j, where ‘M(i,j)' is the value of a cell, ‘i’ is the row number, and ‘j’ is the column number. Return the number of cells having value ‘q’.
// Note: Assume, the array is in 1-based indexing.

// Examples:
// Input: n = 4, q = 7
// Output: 2
// Explanation: Matrix becomes
// 2 3 4 5 
// 3 4 5 6 
// 4 5 6 7
// 5 6 7 8
// The count of 7 is 2.

//{ Driver Code Starts

#include <iostream>
#include <stdio.h>
using namespace std;

// } Driver Code Ends

class Solution {
  public:
    long long sumMatrix(long long n, long long q) {
        // code here
        if (q > n*2){
            return 0;
        }
        if(q<=n+1)
            return (q-1);
        else
            return ((n*2)-q+1);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long n,q;
        
        cin>>n>>q;

        Solution ob;
        cout << ob.sumMatrix(n,q) << endl;
    }
    return 0;
}
// } Driver Code Ends