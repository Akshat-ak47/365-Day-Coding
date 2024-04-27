// Convert the amount in number to words

// Problem Description
// Our company wants to create a data entry verification system. Given an amount in words and an amount indicated by data entry person in numbers, you have to detect whether the amounts are the same or not.

// Note:
// There are a lot of corner cases to be considered. The interviewer expects you to take care of them.
// Every word needs to be separated using "-" rather than a space character https://en.wikipedia.org/wiki/Indian_numbering_system
// "Use Expected Output option" to clear further doubts.

// Problem Constraints
// 1 <= |A| <= 9
// 1 <= |B| <= 100

// Input Format
// String num: Amount written in digits as a string. This string will be an integer number without having any commas in between the digits.
// String words: Amount written in words according to Indian Numbering System.

// Output Format
// An integer
// 1: Values match
// 0: Otherwise

// Example Input
// String num = "1234"
// String words = "one-thousand-two-hundred-and-thirty-four"
// Example Output
// 1

string one[] = {"", "one-", "two-", "three-", "four-", "five-", "six-", "seven-", "eight-", "nine-", "ten-", "eleven-", "twelve-", "thirteen-", "fourteen-", "fifteen-", "sixteen-", "seventeen-", "eighteen-", "nineteen-"};
string ten[] = {"", "", "twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"};

string numToWords(int n, string s)
{
    string str = "";
    if (n > 19)
        str += ten[n / 10] + one[n % 10];
    else
        str += one[n];
    if (n)
        str += s;
    return str;
}

string convertToWords(long n) {
    string out;
    out += numToWords((n / 10000000), "crore-");
    out += numToWords(((n / 100000) % 100), "lakh-");
    out += numToWords(((n / 1000) % 100), "thousand-");
    out += numToWords(((n / 100) % 10), "hundred-");

    if (n > 100 && n % 100)
        out += "and-";
    out += numToWords((n % 100), "");

    if (out == "")
        out = "zero";
    return out;
}

int Solution::solve(string A, string B) {
    string s = convertToWords(stoi(A));
    while(s.back() == '-' || s.back() == ' ')
        s.erase(s.end()-1);
        
    if(s == B)
        return 1;
    return 0;
}