import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int input = scan.nextInt();
		int index = 0;
		int pow = 2;
		int temp;
		int res = 0;
		int testNum;
		for (testNum = 600; index != input; testNum++) {
			temp = 1;

			// 10 의 pow 승을 temp 에 대입
			for (int i = 0; i < pow; i++) {
				temp *= 10;
			}
			if (testNum / temp > 9)	pow++;

			if(findNum(testNum, temp, pow)) {
				index = index + 1;
			}
			
			if(index == input) {
				res = testNum;
				break;
			}
		}
		
		System.out.println(res);
	}

	static boolean findNum(int testNum, int powOf10, int pow){
		int temp = powOf10;
		int count = 0;

		while(testNum > 0){
			if (testNum / powOf10 == 6) {
				count++;
			}
			else {
				count = 0;
			}

			if (count == 3) {
				return true;
			}

			testNum %= powOf10;
			powOf10 /= 10;
		}

		return false;
	}
}