import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int testCount = scan.nextInt();
		int[] roomNum = new int[testCount];
		int[][] apt = new int[15][15];
		int a, b;
		int i, j, k;

		for (i = 0; i <= 14; i++) {
			apt[0][i] = i + 1;
			apt[i][0] = 1;
		}

		for (i = 1; i <= 14; i++) {
			for (j = 1; j <= 14; j++) {
				apt[i][j] += apt[i][j - 1] + apt[i - 1][j];
			}
		}

		for (i = 0; i < testCount; i++) {
			a = scan.nextInt();
			b = scan.nextInt();

			roomNum[i] = apt[a][b - 1];
		}

		for (i = 0; i < testCount; i++) {
			System.out.println(roomNum[i]);
		}

	}
}