import java.util.Random;

public class Test {

	private int[] deck = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21};
	
	public int getRandom(int[] array) {

	    int rnd = new Random().nextInt(array.length);
	    System.out.println(array[rnd]);
	    return array[rnd];
	
	}// end getRandom


	public static void main(String[] args) {

		Test draw = new Test();
		draw.getRandom(draw.deck);

	}//end main
}//end class

for (int i = cards.Length - 1; i > 0; i--)
{
int n = rand.Next(i + 1);
Swap(ref cards[i], ref cards[n]);
}