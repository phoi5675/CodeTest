import java.util.*;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int[][] testCase = new int[n][2];
		int i;
		int left;
		int count = 0;
		long a;

		for(i = 0; i < n; i++){
			testCase[i][0] = scan.nextInt();
			testCase[i][1] = scan.nextInt();
		}
		
		
		for(int j = 0; j < n; j++){
			for(a = 1; (a + 1)*(a + 1) <= testCase[j][1] - testCase[j][0]; a++){

			}

			left = testCase[j][1] - testCase[j][0] - (int)(a * a);
			if(left % a == 0)	count = (int)(((a - 1) * 2 + 1) + left / a);
			else count = (int)(((a - 1) * 2 + 1) + (left / a) + 1);

			System.out.println(count);
		}
		

	}

}