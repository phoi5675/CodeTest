import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int input;
		int i = 0;
		ArrayList arr = new ArrayList();
		
		boolean isMinor = true;

		while((input = scan.nextInt()) != 0) {
			arr.add(input);
		}
		
		for (i = 0; i < arr.size(); i++) {
			System.out.println(eratos((int)arr.get(i), (int)arr.get(i) * 2));
		}
		
	}
	static int eratos(int m, int n) {
		int num = 0;
		boolean[] arr = new boolean[n + 1];
		for(int i = 0; i < arr.length; i++) {
			arr[i] = true;
		}
		arr[0] = false;
		arr[1] = false;
		
		for(int i = 2; i <= Math.sqrt(n); i++) {
			if(arr[i]) {
				for(int j = 2 * i; j <= n; j+=i) {
					arr[j] = false;
				}
			}
		}
		for(int i = 0; i < arr.length; i++) {
			if(arr[i] && (m < i && i <= n))	num++;
		}
		return num;
	}
}