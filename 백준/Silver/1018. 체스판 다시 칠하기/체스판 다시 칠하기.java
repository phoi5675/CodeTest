import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int h = scan.nextInt();
		int w = scan.nextInt();
		String input = new String();
		boolean[][] chess = new boolean[51][51];
		int paint = 0;
		int temp = 0;
		boolean isBlack;

		for (int i = 0; i < h; i++) {
			input = scan.next();
			for (int j = 0; j < w; j++) {
				chess[i][j] = (input.charAt(j) == 'B') ? true : false;
			}
		}

		// 제일 처음을 하얀색으로 칠함
		for (int i = 0; i <= h - 8; i++) {
			for (int j = 0; j <= w - 8; j++) {
				temp = paintFunc(chess, w, h, j, i, false);

				if ((paint == 0 && i == 0 && j == 0) || paint > temp) {
					paint = temp;
				}
			}
		}
		// 검은색으로도 칠함
		for (int i = 0; i <= h - 8; i++) {
			for (int j = 0; j <= w - 8; j++) {
				temp = paintFunc(chess, w, h, j, i, true);

				if (paint > temp) {
					paint = temp;
				}
			}
		}
		System.out.println(paint);
	}
	static int paintFunc(boolean[][] ary, int w, int h, int startX, int startY, boolean startBlack){
		boolean isBlack;
		int temp = 0;
		int paint = 0;
		boolean[][] tempChess = new boolean[51][51];
		
		for (int l = 0; l < h; l++) {
			for (int m = 0; m < w; m++) {
				tempChess[l][m] = ary[l][m];
			}
		}

		isBlack = startBlack;
		for (int j = startY; j < startY + 8; j++) {
			for (int k = startX; k < startX + 8; k++) {
				if (tempChess[j][k] != isBlack) {
					tempChess[j][k] = isBlack;
					paint++;
				}

				isBlack = (isBlack) ? false : true;
			}
			isBlack = (isBlack) ? false : true;
		}
		
		if (paint == 0) {
			temp = 0;
		}
		
		return paint;
	}
}