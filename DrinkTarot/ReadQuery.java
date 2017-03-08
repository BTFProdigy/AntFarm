import java.sql.ResultSet
import java.util.Properties


public class ReadQuery{

	private Connection conn;
	private ResultSet results;

	public ReadQuery(){

		Properties props = new Properties(); //MWC
		InputStream instr = getClass().getResourceAsStream("dbConn.Properties");
		
		try {
			props.load(instr);
		} 
		catch (IOException ex) {
			Logger.getLogger(ReadQuery.class.getName()).log(Level.SEVERE, null, ex); 
		}// try catch end
		
		try {
			instr.close();
		} 
		catch (IOException ex) {
			Logger.getLogger(ReadQuery.class.getName()).log(Level.SEVERE, null, ex); 
		}// try catch end

		String driver = props.getProperty("driver.name");
		String url = props.getProperty("server.name");
		String username = props.getProperty("user.name");
		String passwd = props.getProperty("user.password");
		

		try {
			Class.forName(driver);
		}
		catch (ClassNotFoundException ex) {
			Logger.getLogger(ReadQuery.class.getName()).log(Level.SEVERE, null, ex); 
		}// try catch end
		
		try {
			conn = DriverManager.getConnection(url, username, passwd);
		}
		catch (SQLException ex) {
			Logger.getLogger(ReadQuery.class.getName()).log(Level.SEVERE, null, ex); 
		}// try catch end

	} // ReadQuery method end

	public void doRead(){

		try{
		String query = " SELECT * from MajorArchana WHERE Card ID = 0"

		PreparedStatement ps = conn.prepareStatement(query);
		this.results = ps.executeQuery();
		}
		catch (SQLException ex){
			Logger.getLogger(ReadQuery.class.getName()).log(Level.SEVERE, null, ex);
		}// try catch end

	}// doRead method end

} // end ReadQuery