'''
Snake Ladder Problem!

Problem Description
Rishabh takes out his Snakes and Ladders Game, stares the board and wonders: 
"If I can always roll the die to whatever number I want, what would be the least number of rolls 
to reach the destination?"


RULES:

The game is played with cubic dice of 6 faces numbered from 1 to 6.
Starting from 1 , land on square 100 with the exact roll of the die. If moving the number rolled would place the player beyond square 100, no move is made.
If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.
If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.
BOARD DESCRIPTION:

The board is always 10 x 10 with squares numbered from 1 to 100.
The board contains N ladders given in a form of 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].
The board contains M snakes given in a form of 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].

Problem Constraints
1 <= N, M <= 15
1 <= A[i][0], A[i][1], B[i][0], B[i][1] <= 100
A[i][0] < A[i][1] and B[i][0] > B[i][1]
Neither square 1 nor square 100 will be the starting point of a ladder or snake.
A square will have at most one endpoint from either a snake or a ladder.

Input Format
First argument is a 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].
Second argument is a 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].

Output Format
Return the least number of rolls to move from start to finish on a separate line. If there is no solution, return -1.

Example Input
Input 1:
 A = [  [32, 62]
        [42, 68]
        [12, 98]
     ]
 B = [  [95, 13]
        [97, 25]
        [93, 37]
        [79, 27]
        [75, 19]
        [49, 47]
        [67, 17]

Output 1:
3

Explaination:
The player can roll a 5 and a 6 to land at square 12. There is a ladder to square 98. A roll of 2 ends the traverse in 3 rolls.
'''
from collections import deque

class Solution:
    def snakeLadder(self, A, B):
        m = {}
        N = len(A)
        M = len(B)

        for i in range(N):
            m[A[i][0]] = A[i][1]
        for j in range(M):
            m[B[j][0]] = B[j][1]

        q = deque()
        q.append(1)

        visited = set()
        visited.add(1)

        moves = 0
        while q:
            size = len(q)
            moves += 1

            for _ in range(size):
                temp = q.popleft()
                if temp == 100:
                    moves -= 1
                    return moves

                for j in range(temp + 1, min(temp + 7, 101)):
                    if j in m:
                        if m[j] not in visited:
                            q.append(m[j])
                            visited.add(m[j])
                    elif j not in visited:
                        q.append(j)
                        visited.add(j)
        return -1

solution = Solution()

A = [[3, 54], [37, 100]]
B = [[56, 33]]

print(solution.snakeLadder(A, B))  # output = 6
