'''
REC_CMPL1

What is the worst case time complexity of the following code :

/* 
 * V is sorted 
 * V.size() = N
 * The function is initially called as searchNumOccurrence(V, k, 0, N-1)
 */
int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
    if (start > end) return 0;
    int mid = (start + end) / 2;
    if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
    if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
}
'''

print('''Answer is O(N)''')
print('''
Explaination - Initially, the function is called with the entire range of the vector, which is of size N.
At each recursive call, the function splits the search range into two halves and continues the search in one of the halves.
In the worst case, the function needs to explore both halves of the vector for each recursive call until it reaches the base case where 
start > end.''')