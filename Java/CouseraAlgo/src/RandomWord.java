import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
	public static void main(String[] args) {
		String selStr = "";
		int cnt = 0;
		while(!StdIn.isEmpty()) {
			cnt++;
			String rand = StdIn.readString();
			if(StdRandom.bernoulli(1/cnt)) {
				selStr = rand;
			}
		}
		
		StdOut.println(selStr);
	}
}
