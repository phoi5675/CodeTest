import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int up = scan.nextInt();
		int down = scan.nextInt();
		int height = scan.nextInt();
		int day = (height - down) / (up - down);
		
		if((height - down) % (up - down) != 0)	day++;
		
		System.out.println(day);
	}
}