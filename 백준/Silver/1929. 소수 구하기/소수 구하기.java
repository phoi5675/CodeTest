import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int m = scan.nextInt();
		int n = scan.nextInt();


		boolean isMinor = true;

		for (int i = m; i <= n; i++) {
			if(i == 1)	continue;
			isMinor = true;
			if (i != 2 && i % 2 == 0) {
				isMinor = false;
				continue;
			}
			for (int j = 3; j <= Math.sqrt(i); j+=2) {
				if (i % j == 0) {
					isMinor = false;
					break;
				}
			}
			if (isMinor) {
				System.out.println(i);
			}

		}
		
	}
}