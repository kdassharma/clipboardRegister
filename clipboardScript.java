import java.math.*;
import java.util.*;
import java.awt.*;
import java.awt.datatransfer.*;


public class clipboardScript{

    //global dictionary declaration
    static Dictionary<String,Integer> dict = new Hashtable<String, Integer>();

    public static void main(String[] args){
        int numberOfInputs = 1;
        dict.put(readClipboard(),numberOfInputs);
        System.out.println(readClipboard());
        while(true) {
            if(dict.get(readClipboard()) == null) {
                numberOfInputs++;
                dict.put(readClipboard(), numberOfInputs);
                System.out.println(readClipboard());
            }
        }
        /*
        //tests for the dictionary
        addToDictionary("hi");
        addToDictionary("hello");
        addToDictionary("hi");
        addToDictionary("hi");
        //this prints the dictionary
        Enumeration<Integer> i = d.elements();
        for (Enumeration<String> k = d.keys(); k.hasMoreElements();) 
        { 
            System.out.println("Key: " + k.nextElement() + " Value: " + i.nextElement()); 
        }  */
    }

    public static String readClipboard(){
      	String content = "";
      	try {
      		content += (String)(Toolkit.getDefaultToolkit().getSystemClipboard().getData(DataFlavor.stringFlavor));
  		}
        catch(Exception e) {
      		e.printStackTrace();
  		}
  		return content;
	}


}