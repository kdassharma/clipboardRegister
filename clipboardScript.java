import java.math.*;
import java.util.*;
import java.awt.*;
import java.awt.datatransfer.*;


public class clipboardScript{

    //global dictionary declaration
    static Dictionary<String,Integer> list = new Hashtable<String, Integer>();
    static Toolkit toolkit = Toolkit.getDefaultToolkit();
    static Clipboard clipboard = toolkit.getSystemClipboard();
    static int counter = 1;

    public static void main(String[] args){
        list.put(readClipboard(),counter);
        System.out.println(list.get(readClipboard()));
        counter++;
        while(true) {
            if (clipboard.isDataFlavorAvailable(DataFlavor.stringFlavor) && list.get(readClipboard()) == null) {
                list.put(readClipboard(),counter);
                System.out.println(list.get(readClipboard()));
                counter++;

            }
        }


    }

    public static String readClipboard(){
        String content = "";
        try{
            content = (String) clipboard.getData(DataFlavor.stringFlavor);
        }
        catch(Exception e) {
            e.printStackTrace();
        }

        return content;
    }


}