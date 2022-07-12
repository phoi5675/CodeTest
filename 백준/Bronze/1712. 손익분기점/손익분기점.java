import java.io.*;
import java.util.Scanner;
class Main{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int fixedPrice = 0, varprice = 0;
		int lapPrice = 0;
		
		int bep = -1;
		int n = 0;

		fixedPrice = scan.nextInt();
		varprice = scan.nextInt();
		lapPrice = scan.nextInt();

		/*
		 * 총 비용 = 고정 비용 + 대당 생산 비용 * 생산 대수
		 * 총 수입 = 노트북 가격 * 생산 대수
		 */
		if(lapPrice <= varprice)	bep = -1;
		else{
			n = fixedPrice / (lapPrice - varprice);
			while(fixedPrice + varprice * n >= lapPrice * n){
				n++;
			}

			bep = n;
		}

		System.out.println(bep);
	}
}