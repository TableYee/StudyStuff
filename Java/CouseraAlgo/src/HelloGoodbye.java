import java.util.ArrayList;
import java.util.List;

public class HelloGoodbye {
	public static void main(String[] args) {
		List<String> names = new ArrayList<String>();
		for(String name:args) {
			names.add(name);
		}
		
		String hello = String.format("Hello %s and %s.", names.get(0), names.get(1));
		String goodbye = String.format("Goodbye %s and %s.", names.get(1), names.get(0));

		System.out.println(hello);
		System.out.println(goodbye);
	}
}
