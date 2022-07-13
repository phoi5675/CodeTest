import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int num = scan.nextInt();
		int[][] table = new int[num][2];
		int rank;
		
		for (int i = 0; i < num; i++) {
			table[i][0] = scan.nextInt();
			table[i][1] = scan.nextInt();
		}
		
		for (int i = 0; i < num; i++) {
			rank = 1;
			for (int j = 0; j < num; j++) {
				if (i == j) {
					continue;
				}
				if (table[i][0] < table[j][0] && table[i][1] < table[j][1]) {
					rank++;
				}
			}

			System.out.println(rank);
		}
	}
}