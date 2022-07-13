import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int m = scan.nextInt();
		int n = scan.nextInt();
		int sum = 0;
		int min = 0;

		boolean isMinor = true;

		for (int i = m; i <= n; i++) {
			if(i == 1)	continue;
			isMinor = true;
			for (int j = 2; j < i; j++) {
				if (i % j == 0) {
					isMinor = false;
					break;
				}
			}
			if (isMinor) {
				sum+= i;
			}
			if (isMinor && min == 0) {
				min = i;
			}
		}
		if (sum == 0) {
			sum = -1;
		}
		if (sum != -1) {
			System.out.println(sum);
			System.out.println(min);
		}
		else{
			System.out.println(sum);
		}
		
	}
}