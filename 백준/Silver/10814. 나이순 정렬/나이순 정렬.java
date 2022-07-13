import java.util.*;
import java.io.*;
import java.lang.*;

class Main{
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Scanner scan = new Scanner(System.in);
		
		int inputInt = scan.nextInt();
		ArrayList<Reg> arr = new ArrayList<Reg>(inputInt);
		int age;
		String name;
		for(int i = 0; i < inputInt; i++) {
			age = scan.nextInt();
			name = scan.next();
			arr.add(new Reg(age, name));
		}
		Collections.sort(arr);
		
		for(int i = 0; i < arr.size(); i++) {
			System.out.println(arr.get(i).getAge() + " " + arr.get(i).getName());
		}
	}
}
class Reg implements Comparable<Reg>{
	private int age;
	private String name;
	
	// constructor
	public Reg(int _age, String _name) {
		this.age = _age;
		this.name = _name;
	}
	// getter
	public int getAge() { return this.age; }
	public String getName() { return this.name; }
	
	@Override
	public int compareTo(Reg reg) {
		// TODO Auto-generated method stub
		Integer i = new Integer(reg.getAge());
		Integer thisAge = new Integer(this.age);
		return thisAge.compareTo(i);
	}

	// omit setter

}