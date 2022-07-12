import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int input = scan.nextInt();
		int len = 0;
		int temp = input;
		int tempsum;
		int pow;
		int res = 0;

		while (temp > 0){
			len++;
			temp /= 10;
		}

		for (int i = input - 9 * len; i < input; i++) {
			temp = i;
			tempsum = i;

			for (int j = len; j > 0; j--) {
				pow = 1;

				for (int k = 0; k < j - 1; k++) {
					pow *= 10;
				}

				tempsum += temp / pow;
				
				temp %= pow;
			}

			if (tempsum == input) {
				res = i;
				break;
			}
		}

		System.out.println(res);
	}
}