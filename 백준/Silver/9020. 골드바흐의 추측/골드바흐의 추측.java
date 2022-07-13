import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int testCase = scan.nextInt();
		int i = 0;
		int[] input = new int[testCase];
		int[] minNum;
		int[][] res = new int[testCase][2];
		
		for (i = 0; i < testCase; i++) {
			input[i] = scan.nextInt();
			minNum = eratos(input[i]);

			for (int j = 0; minNum[j] != 0; j++) {
				for (int k = j; minNum[k] != 0; k++) {
					if (minNum[j] + minNum[k] == input[i]) {
						if (res[i][0] == 0 && res[i][1] == 0) {
							res[i][0] = minNum[j];
							res[i][1] = minNum[k];
						}
						else if (res[i][1] - res[i][0] > minNum[k] - minNum[j]) {
							res[i][0] = minNum[j];
							res[i][1] = minNum[k];
						}
					}
				}
			}
		}

		for (i = 0; i < testCase; i++) {
			System.out.println(res[i][0] + " " + res[i][1]);
		}
		
		
	}
	static int[] eratos(int n) {
		int num = 0;
		boolean[] arr = new boolean[n + 1];
		int[] res = new int[n];
		int j = 0;
		int k = 0;

		for(int i = 0; i < arr.length; i++) {
			arr[i] = true;
		}
		arr[0] = false;
		arr[1] = false;
		
		for(int i = 2; i <= Math.sqrt(n); i++) {
			if(arr[i]) {
				for(j = 2 * i; j <= n; j+=i) {
					arr[j] = false;
				}
			}
		}

		for (j = 0; j < arr.length; j++) {
			if (arr[j]) {
				res[k++] = j;
			}
		}
		
		return res;
	}
}