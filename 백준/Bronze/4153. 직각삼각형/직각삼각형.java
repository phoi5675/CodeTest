import java.util.*;
import java.io.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		double a, b, c;
		double w, h, temp;
		do {
			a = scan.nextLong();
			b = scan.nextLong();
			c = scan.nextLong();
			
			if (a == 0 && b == 0 && c == 0)	break;
			
			if (a > b && a > c) {
				temp = a;
				w = b;
				h = c;
			}
			else if (b > a && b > c) {
				temp = b;
				w = a;
				h = c;
			}
			else {
				temp = c;
				w = a;
				h = b;
			}

			if (temp == Math.sqrt(w * w + h * h)) {
				System.out.println("right");
			}
			else{
				System.out.println("wrong");
			}

		} while(a != 0 && b != 0 && c != 0);
	}
}