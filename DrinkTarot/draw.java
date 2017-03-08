import java.sql.*;
import java.util.Random;

public class Draw {
	
	private int []deck = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21};
	
	public int getRandom(int[] array) {

	    int rndCard = new Random().nextInt(array.length);
	    System.out.println(array[rndCard]);
	    return array[rndCard];
		
		}// end get random

	public static void main(String[] args) {
		
		Draw nextCard = new Draw();
		nextCard.getRandom(nextCard.deck);
		
		try {

			//Have to first call getRandom.
			

			//Then Draw a card by pulling the card's data from the database via primary key


			//Then save the card data to a card object


			//Then have the system prsent the card


		} // end try
		
		catch (Exception e) {
      
      	System.err.println("Got an exception!");
      	System.err.println(e.getMessage());
    
    	} // end catch

	}// end main

}// end class