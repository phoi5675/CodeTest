import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int testCase = scan.nextInt();
		int x1, y1, r1;
		int x2, y2, r2;
		int bx, by, br, sx, sy, sr;
		for (int i = 0; i < testCase; i++) {
			x1 = scan.nextInt();
			y1 = scan.nextInt();
			r1 = scan.nextInt();
			
			x2 = scan.nextInt();
			y2 = scan.nextInt();
			r2 = scan.nextInt();

			double dist = getDist(x1, y1, x2 ,y2);
			
			if (r1 > r2) {
				bx = x1;
				by = y1;
				br = r1;

				sx = x2;
				sy = y2;
				sr = r2;
			}
			else {
				bx = x2;
				by = y2;
				br = r2;

				sx = x1;
				sy = y1;
				sr = r1;
			}

			if (x1 == x2 && y1 == y2) {
				if (r1 == r2) {
					System.out.println(-1);
				}
				else {
					System.out.println(0);
				}
			}
			else if (br - sr >= dist) {
				if (br - sr > dist) {
					System.out.println(0);
				}
				else {
					System.out.println(1);
				}
			}
			else if (br + sr > dist) {
				System.out.println(2);
			}
			else if (br + sr <= dist) {
				if (br + sr == dist) {
					System.out.println(1);
				}
				else {
					System.out.println(0);
				}
			}
			


		}
	}
	static double getDist(int x1, int y1, int x2, int y2){
		return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
	}
}