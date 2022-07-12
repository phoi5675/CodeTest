import java.util.*;
import java.io.*;
/*
 * 산술평균 및 최빈값 수정 필요
 */
class Main{
	static int[] count = new int[8001];
	static int[] sorted = new int[500000];


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

		mergeSort(arr, 0, input - 1);

		bw.write(findArith() + "\n");
		bw.write(arr[input / 2] + "\n");
		bw.write(findFreq() + "\n");
		bw.write(arr[input - 1] - arr[0] + "\n");

		bw.flush();
		bw.close();
		bf.close();
	}
	static void countSort(int[] arr){
		for (int i = 0; i < arr.length; i++) {
			count[arr[i] + 4000]++;
		}
	}
	static int findArith(){
		int num = 0;
		int sum = 0;

		for (int i = 0; i < count.length; i++) {
			if (count[i] == 0) {
				continue;
			}
			else {
				sum += (-4000 + i) * count[i];
				num += count[i];
			}
		}
		// 반올림 하는 부분

		if (sum > 0) {
			sum = (int)Math.round((double)sum / num);
		}
		else {
			sum = -(int)Math.round(Math.abs((double)sum / num));
		}
		

		return sum;
	}
	static int findFreq(){
		int max = 0;
		int index = 0;

		// 이 과정에서 제일 작은 값의 index 를 구함
		for (int i = 0; i < count.length; i++) {
			if (count[i] > max) {
				max = count[i];
				index = -4000 + i;
			}
		}
		for (int i = 0; i < count.length; i++) {
			if (count[i] < max) {
				continue;
			}
			else if ((-4000 + i) != index && count[i] == max) {
				index = -4000 + i;
				break;
			}
		}
		return index;
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