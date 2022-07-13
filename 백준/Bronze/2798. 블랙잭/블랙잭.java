import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int cardNum = scan.nextInt();
		int sumNum = scan.nextInt();
		int sum = 0;
		int i, j, k;
		int temp = 0;
		int[] cards = new int[cardNum];

		for (i = 0; i < cardNum; i++) {
			cards[i] = scan.nextInt();
		}

		for (i = 0; i < cardNum; i++) {
			for (j = i + 1; j < cardNum; j++) {
				for (k = j + 1; k < cardNum; k++) {
					temp = cards[i] + cards[j] + cards[k];
					if(sum > sumNum)	sum = 0;
					sum = (temp <= sumNum &&
						temp > sum) ? temp : sum;
				}
			}
		}
		System.out.println(sum);
	}
}