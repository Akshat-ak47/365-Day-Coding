// Sort 0s, 1s and 2s

// Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

// Example 1:
// Input: 
// N = 5
// arr[]= {0 2 1 2 0}
// Output:
// 0 0 1 2 2
// Explanation:
// 0s 1s and 2s are segregated 
// into ascending order.

//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;



// } Driver Code Ends
class Solution
{
    public:
    void sort012(int a[], int n)
    {
        int low = 0;
        int high = n-1;
        int mid = 0;
        
        while (mid <= high){
            switch (a[mid]) {
                case 0:
                    swap(a[low++], a[mid++]);
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    swap(a[mid], a[high--]);
                    break;
            }
        }
    }
    
};

//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >>n;
        int a[n];
        for(int i=0;i<n;i++){
            cin >> a[i];
        }

        Solution ob;
        ob.sort012(a, n);

        for(int i=0;i<n;i++){
            cout << a[i]  << " ";
        }

        cout << endl;
        
        
    }
    return 0;
}


// } Driver Code Ends