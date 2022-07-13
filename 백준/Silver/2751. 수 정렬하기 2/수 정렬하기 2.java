import java.util.*;
import java.io.*;

class Main{
	static int[] sorted = new int[1000000];

	public static void main(String[] args) throws Exception{
		Scanner scan = new Scanner(System.in);

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int input = Integer.parseInt(bf.readLine());
		int[] arr = new int[input];

		for (int i = 0; i < input; i++) {
			arr[i] = Integer.parseInt(bf.readLine());
		}

		mergeSort(arr, 0, input - 1);

		for (int i = 0; i < input; i++) {
			bw.write(arr[i] + "\n");
		}

		bw.flush();
		bw.close();
		bf.close();
	}
	static void mergeSort(int[] arr, int left, int right){
		int mid;
		if (left < right) {
			mid = (left + right) / 2;

			mergeSort(arr, left, mid);
			mergeSort(arr, mid + 1, right);

			merge(arr, left, mid, right);
		}
	}
	static void merge(int[] arr, int left, int mid, int right){
		int i = left;
		int j = mid + 1;
		int k = left;
		int l;

		while (i <= mid && j <= right) {
			if (arr[i] <= arr[j]) {
				sorted[k++] = arr[i++];
			}
			else {
				sorted[k++] = arr[j++];
			}
		}

		if (i > mid) {
			for (l = j; l <= right; l++) {
				sorted[k++] = arr[l];
			}
		}
		else {
			for (l = i; l <= mid; l++) {
				sorted[k++] = arr[l];
			}
		}

		for (l = left; l <= right; l++) {
			arr[l] = sorted[l];
		}
	}
}