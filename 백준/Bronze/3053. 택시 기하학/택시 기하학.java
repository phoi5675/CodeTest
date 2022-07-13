import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int r = scan.nextInt();
		
		double circ = Math.PI * r * r;
		double taxi = Math.pow((double) r, 2) * 2;
		System.out.printf("%.6f\n", circ);
		System.out.printf("%.6f", taxi);
	}
}