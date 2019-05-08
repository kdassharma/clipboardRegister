import java.math.*;
import java.util.*;
import java.awt.HeadlessException;
import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.IOException;
public class clipboardScript{

    //global dictionary declaration
    static Dictionary<String, Integer> d = new Hashtable<String, Integer>();

    public static void main(String[] args){
    	//prints out the clipboard, but goes really slow for some reason??
  		System.out.println(readClipboard());
        

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
        }  
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


	public static void addToDictionary(String s){
        //check if already in dictionary
        if(d.get(s)!=null){
            //add 1 to counter
            d.put(s, ((int) d.get(s)) + 1);
        }
        //otherwise put it into the dictionary
        else{
            d.put(s, 1);
        }    
	}


}