import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int testCount = scan.nextInt();
		int[] arr = new int[testCount];
		int res = 0;
		int i, j;
		int k = 0;
		boolean isMinor = true;

		for (i = 0; i < testCount; i++) {
			arr[i] = scan.nextInt();
			isMinor = true;
			if (arr[i] == 1)	continue;
			for (j = 2; j < arr[i]; j++) {
				if (arr[i] % j == 0) {
					isMinor = false;
					break;
				}
			}
			if (isMinor) {
				res++;
			}
		}
		System.out.println(res);
	}
}