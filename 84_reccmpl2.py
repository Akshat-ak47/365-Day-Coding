'''
REC_CMPL2

What is the worst case time complexity of the following code:

int findMinPath(vector<vector<int> > &V, int r, int c) {
  int R = V.size();
  int C = V[0].size();
  if (r >= R || c >= C) return 100000000; // Infinity
  if (r == R - 1 && c == C - 1) return 0;
  return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
}
Assume R = V.size() and C = V[0].size().
'''

print("O(2^(R+C))")
print('''
The worst-case time complexity of the given code can be analyzed by considering the recursive calls made to the function findMinPath.

At each recursive call, the function either moves down (r + 1, c) or moves right (r, c + 1). Since it explores all possible paths until it reaches the bottom-right corner (R - 1, C - 1), it will explore a total of 
2 R+C paths.
However, we can optimize this by observing that once we reach the last row or the last column, further exploration is unnecessary, as there's only one direction to move. Therefore, the maximum number of recursive 
calls made in this scenario will be R+C.

Hence, the worst-case time complexity of this code is O(2^(R+C))
 ''')