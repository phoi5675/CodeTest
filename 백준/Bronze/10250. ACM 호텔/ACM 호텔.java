import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int testCount = scan.nextInt();
		int[] roomNum = new int[testCount];
		
		for(int i = 0; i < testCount; i++) {
			int h = scan.nextInt();
			int w = scan.nextInt();
			int num = scan.nextInt();
			
			roomNum[i] = (num % h == 0) ? (num / h) : (num / h + 1);
			roomNum[i] += (num - (roomNum[i] - 1) * h) * 100;
		}
		
		for(int i = 0; i < testCount; i++) {
			System.out.println(roomNum[i]);
		}
	}
}