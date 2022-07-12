import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int upper, lower;
		int sum = 0;
		int temp;
		int i;

		for(i = 0; sum + (i + 1) <= n; i++){
			sum += i;
		}
		
		temp = n - sum;

		if(i % 2 == 0){
			upper = temp;
			lower = i - temp + 1;
		}
		else{
			upper = i - temp + 1;
			lower = temp;
		}

		System.out.println(upper + "/" + lower);
	}
}