// Missing in Array

// Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n. Return the missing element.

// Examples:
// Input: n = 5, arr[] = [1,2,3,5]
// Output: 4
// Explanation : All the numbers from 1 to 5 are present except 4.

//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:

    // Note that the size of the array is n-1
    int missingNumber(int n, vector<int>& arr) {

        // Your code goes here'
        int i = 0;
        sort(arr.rbegin(), arr.rend());
        
        while(n>0){
            if (n!=arr[i]){
                return n;
            }
            n--;
            i++;
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> arr(n - 1);
        for (int i = 0; i < n - 1; ++i)
            cin >> arr[i];
        Solution obj;
        cout << obj.missingNumber(n, arr) << "\n";
    }
    return 0;
}
// } Driver Code Ends