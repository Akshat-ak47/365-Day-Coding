// Check If two Line segments Intersect

// Given the coordinates of the endpoints(p1,q1, and p2,q2) of the two line segments. Check if they intersect or not. If the Line intersects return true otherwise return false.
// Examples

// Input: p1=(1,1), q1=(10,1), p2=(1,2), q2=(10,2)
// Output: false
// Explanation:The two line segments formed by p1-q1 and p2-q2 do not intersect.

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string doIntersect(int p1[], int q1[], int p2[], int q2[]) {
        // Calculating the Slopes
        double m1 = (double)(q1[1] - p1[1]) / (double)(q1[0] - p1[0]);
        double m2 = (double)(q2[1] - p2[1]) / (double)(q2[0] - p2[0]);
        // If slopes are equal, means lines are parallel
        if(m1 == m2)
            return "false";

//      chk211 and chk212 check if the points p2 and q2 are above or below the line segment (p1, q1).
//      chk121 and chk122 check if the points p1 and q1 are above or below the line segment (p2, q2).
        bool chk211 = p2[1]-p1[1] - m1*(p2[0]-p1[0]) >0 ? true:false;
        bool chk212 = q2[1]-p1[1] - m1*(q2[0]-p1[0]) >0 ? true:false;
        bool chk121 = p1[1]-p2[1] - m2*(p1[0]-p2[0]) >0 ? true:false;
        bool chk122 = q1[1]-p2[1] - m2*(q1[0]-p2[0]) >0 ? true:false;

//      If both points of one segment lie on the same side of the other segment, the segments do not intersect.
//      The condition (chk211 == true && chk212 == true) checks if both p2 and q2 are on the same side (above) of the line p1q1.
//      Similarly, (chk211 == false && chk212 == false) checks if both p2 and q2 are on the same side (below) of the line p1q1.
        if((chk211==true and chk212 == true) or (chk211==false and chk212 == false) or 
        (chk121 == true and chk122 == true) or (chk121 == false and chk122 == false)){
            return "false";
        }
        return "true";
    }
};