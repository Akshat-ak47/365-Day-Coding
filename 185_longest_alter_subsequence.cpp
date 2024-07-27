// Longest alternating subsequence

// You are given an array arr. Your task is to find the longest length of a good sequence. A good sequence {x1, x2, .. xn} is an alternating sequence if its elements satisfy one of the following relations :

// 1.  x1 < x2 > x3 < x4 > x5. . . . . and so on
// 2.  x1 >x2 < x3 > x4 < x5. . . . . and so on

// Examples:

// Input: arr= [1, 5, 4]
// Output: 3
// Explanation: The entire sequenece is a good sequence.

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int alternatingMaxLength(vector<int>& arr) {
        // Code here
        int max_length = 1;
        int up = 1;
        int down = 1;
        int n = arr.size();
        
        for (int i=1; i<n; ++i){
            if (arr[i] > arr[i-1]){
                up = down + 1;
            } else if (arr[i] < arr[i-1]){
                down = up + 1;
            }
            max_length = max(max_length, max(up, down));
        }
        return max_length;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    cin.ignore();
    while (tc--) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> arr;
        string temp;
        while (ss >> temp) {
            arr.push_back(stoi(temp));
        }
        Solution obj;
        int ans = obj.alternatingMaxLength(arr);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends