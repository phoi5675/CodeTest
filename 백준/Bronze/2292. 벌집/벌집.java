import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int i = 1;
		int seq = 2 + 6 * (i - 1);

		if(n != 1){
			while(seq <= n){
				seq += 6 * i;
				i++;
			}
		}
		
		System.out.println(i);
	}
}