import java.util.*;
import java.io.*;

class Main{
	static int[] sorted = new int[100001];
	static int[] sortedY = new int[100001];

	public static void main(String[] args) throws Exception{
		Scanner scan = new Scanner(System.in);

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int input = Integer.parseInt(bf.readLine());
		ArrayList<Point> arr = new ArrayList<Point>(input);
		String[] temp = new String[30];

		for (int i = 0; i < input; i++) {
			temp = bf.readLine().split(" ");
			arr.add(new Point(Integer.parseInt(temp[0]), Integer.parseInt(temp[1])));
		}

		Collections.sort(arr, new Comparator<Point>(){
			public int compare(Point p1, Point p2){
				if (p1.x < p2.x) {
					return -1;
				}
				else if (p1.x == p2.x) {
					if (p1.y < p2.y) {
						return -1;
					}
					else if (p1.y > p2.y) {
						return 1;
					}
				}
				else if (p1.x > p2.x) {
					return 1;
				}
				return 0;
			}
		});
		for (int i = 0; i < input; i++) {
			bw.write(arr.get(i).x + " " + arr.get(i).y + "\n");
		}
		
		bw.flush();
		bw.close();
		bf.close();
	}
}
class Point{
	public int x;
	public int y;

	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}