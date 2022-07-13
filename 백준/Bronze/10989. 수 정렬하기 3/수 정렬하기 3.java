import java.util.*;
import java.io.*;

class Main{
	static int[] count = new int[10001];

	public static void main(String[] args) throws Exception{
		Scanner scan = new Scanner(System.in);

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int input = Integer.parseInt(bf.readLine());
		int[] arr = new int[input];
		int sum = 0;

		for (int i = 0; i < input; i++) {
			arr[i] = Integer.parseInt(bf.readLine());
		}

		countSort(arr);

		for (int i = 1; sum < input; i++) {
			if (count[i] == 0) {
				continue;
			}
			else {
				for (int j = 0; j < count[i]; j++) {
					bw.write(i + "\n");
					sum++;
				}
			}
		}

		bw.flush();
		bw.close();
		bf.close();
	}
	static void countSort(int[] arr){
		for (int i = 0; i < arr.length; i++) {
			count[arr[i]]++;
		}
	}
}