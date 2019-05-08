import java.math.*;
import java.util.*;
import java.awt.HeadlessException;
import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.IOException;
public class clipboardScript{


    public static void main(String[] args){
    		//prints out the clipboard, but goes really slow for some reason??
  			System.out.println(readClipboard());
 
    }

    public static String readClipboard(){
    	String clipboard = "";
    	try {
  			clipboard = (String) Toolkit.getDefaultToolkit().getSystemClipboard().getData(DataFlavor.stringFlavor);
		}
    	catch(UnsupportedFlavorException e) {
  			e.printStackTrace();
		}
		catch(IOException e) {
  			e.printStackTrace();
		}
		return clipboard;
	}


	public static void addToDictionary(){

	}


}