import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int inputInt = Integer.parseInt(bf.readLine());
		String[] arr = new String[inputInt];
		String[] res = new String[inputInt];
		
		// get array
		for(int i = 0; i < inputInt; i++) {
			arr[i] = bf.readLine();
		}
		
		insertionSort(arr, res);

		for (int i = 0; i < arr.length; i++) {
			if(i + 1 < arr.length && arr[i].compareTo(arr[i + 1]) == 0) {
				continue;
			}
			System.out.println(arr[i]);
		}
	}
	public static void insertionSort(String[] arr, String[] res) {
		String tmp;
		
		for(int index = 1; index < arr.length; index++) {
			tmp = arr[index];
			int aux = index - 1;

			while((aux >= 0) && (compareStr(arr[aux], tmp) == 1)){
				// 길이가 긴 경우 루프 탈출
				//if(arr[aux].length() < tmp.length())	break;
				arr[aux + 1] = arr[aux];
				aux--;
			}
			arr[aux + 1] = tmp;
		}
		
	}
	public static int compareStr(String arr, String cmp) {
		boolean esc = false;
		boolean dict = false;
		int len = (arr.length() < cmp.length()) ? arr.length() : cmp.length();
		// 문장의 길이가 길거나, 사전순으로 정렬 시 arr 이 cmp 보다 뒤에 있는 경우 뒤로 빼야 함
		
		// 원래 위치의 문장의 길이가 긴 경우
		if (arr.length() > cmp.length()) {
			return 1;
		}
		else if (arr.length() < cmp.length()) {
			return -1;
		}
		
		// 사전식 정렬
		for (int i = 0; i < len; i++) {
			int a = arr.charAt(i);
			int b = cmp.charAt(i);
			
			if(a == b) {
				continue;
			}
			else if(a < b) {
				return -1;
			}
			else if(a > b) {
				return 1;
			}
		}
		return -1;
	}
}