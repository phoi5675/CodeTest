import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int x = scan.nextInt();
		int y = scan.nextInt();
		int w = scan.nextInt();
		int h = scan.nextInt();

		int left = x;
		int right = w - x;
		int top = h - y;
		int bot = y;

		int res = (left < right) ? left : right;
		res = (res < top) ? res : top;
		res = (res < bot) ? res : bot;

		System.out.println(res);
	}
}