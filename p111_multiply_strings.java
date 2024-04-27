// Multiply Strings

// Problem Description
// Given two numbers represented as strings, return the multiplication of the numbers as a string.
// Note: 
// The numbers can be arbitrarily large and are non-negative.
// Your answer should not have leading zeroes. For example, 00 is not a valid answer.
// DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ). We will retroactively disqualify such submissions and the submissions will incur penalties.

public class p111_multiply_strings {
    public String multiply(String A, String B) {
		if (A.equals("0") || B.equals("0")) return "0";
		
		int m = A.length();
		int n = B.length();
		int [] result = new int [m+n];
		
		for (int i=m-1; i>=0; i--){
			for (int j=n-1; j>=0; j--){
				int mul = (A.charAt(i) - '0') * (B.charAt(j) - '0');
				int sum = mul + result[i+j+1];
				result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
			}
		}
		StringBuilder sb = new StringBuilder();
        for (int digit : result) {
            if (!(sb.length() == 0 && digit == 0)) {
                sb.append(digit);
            }
        }
        
        return sb.toString();
		
    }
    public static void main (String [] args){
        p111_multiply_strings sol = new p111_multiply_strings();
        String A = "13";
        String B = "10";

        String result = sol.multiply(A, B);
        System.out.println(result);
    }
}
