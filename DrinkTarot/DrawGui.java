import javax.swing.JOptionPane;
import javax.swing.JButton;

class DrawGui{
	
	public static void main ( String[] args) {

	String fn = JOptionPane.showInputDialog("Enter first-name");
	//String sn = JOptionPane.showInputDialog("Enter last-name");
	String outMsg = ("Hello " + fn + " would you like to draw a card?");
	//System.out.println(outMsg);

	JOptionPane.showMessageDialog(null, outMsg);

	/*buttonDraw = new JButton
	b1 = new JButton("Draw a Card", leftButtonIcon);
    b1.setVerticalTextPosition(AbstractButton.CENTER);
    b1.setHorizontalTextPosition(AbstractButton.LEADING); //aka LEFT, for left-to-right locales
    b1.setMnemonic(KeyEvent.VK_D);
    b1.setActionCommand("disable");*/


	}// end main

}// end DrawGUI class
