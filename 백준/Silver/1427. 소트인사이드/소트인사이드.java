import java.util.*;
import java.io.*;

class Main{
	static int[] arr = new int[11];
	public static void main(String[] args) throws Exception{
		Scanner scan = new Scanner(System.in);

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String input = new String();
		input = bf.readLine();		
		
		for (int i = 0; i < input.length(); i++) {
			arr[i] = (int)input.charAt(i) - 48;
		}

		selSort(arr);

		for (int i = 0; i < input.length(); i++) {
			bw.write(arr[i] + "");
			bw.flush();
		}
		bw.write("\n");

		bw.flush();
		bw.close();
		bf.close();
	}
	static void selSort(int[] arr){
		int temp;
		for (int i = 0; i < arr.length; i++) {
			for (int j = i; j < arr.length; j++) {
				if (arr[j] > arr[i]) {
					temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
	}
}