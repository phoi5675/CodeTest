import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int[][] point = new int[4][2];

		for (int i = 0; i < 3; i++) {
			point[i][0] = scan.nextInt();
			point[i][1] = scan.nextInt();
		}
		
		if (point[0][0] == point[1][0]) {
			point[3][0] = point[2][0];
		}
		else if (point[1][0] == point[2][0]) {
			point[3][0] = point[0][0];
		}
		else if (point[0][0] == point[2][0]) {
			point[3][0] = point[1][0];
		}

		if (point[0][1] == point[1][1]) {
			point[3][1] = point[2][1];
		}
		else if (point[1][1] == point[2][1]) {
			point[3][1] = point[0][1];
		}
		else if (point[0][1] == point[2][1]) {
			point[3][1] = point[1][1];
		}

		System.out.println(point[3][0] + " " + point[3][1]);
	}
}