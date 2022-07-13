import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int kg5 = 0, kg3 = 0;

		kg5 = n / 5;
		kg3 = (n - kg5 * 5) / 3;
		if(kg5 * 5 + kg3 * 3 != n){
			for(int i = 1; i <= 5; i++) {
				int temp = n;
				temp -= 3 * i;
				
				if(temp % 5 == 0) {
					kg5 = temp / 5;
					kg3 = i;
					break;
				}
				
				if(temp < 3)	break;
			}
		}
		else if(n % 5 == 0 && kg5 * 5 + kg3 * 3 != n){
			kg5 = n / 5;
			kg3 = 0;
		}
		else if(n % 3 == 0 && kg5 * 5 + kg3 * 3 != n){
			kg5 = 0;
			kg3 = n / 3;
		}


		if(n == kg5 * 5 + kg3 * 3){
			System.out.println(kg5 + kg3);
		}
		else{
			System.out.println(-1);
		}
	}
}