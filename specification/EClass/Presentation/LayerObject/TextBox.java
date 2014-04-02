package EClass.Presentation.LayerObject;


/**
 * The TextBox can be used to represent any text the user wishes
 * to present on to a layer.
 * 
 * text will contain the main text for the TextBox.
 * width will represent the width size of the TextBox.
 * height will represent the height size of the TextBox.
 * fontSize will contain the size of which text will be. 
 */
abstract public class TextBox extends LayerObject {
    //text represents the string of text contained in the text box
    String text; 
    //width represents the width of the text box
    double width;
    //height represents the height of the text box
    double height;
    //fontSize rerpesents the size of the font. i.e text
    int fontSize;


   /**
    * Edits the text in the text box.
    * @param newText the new text for the textbox
    */
   /*@
    * requires
    *    newText != null;
    * ensures
    *    \old(text) != newText
    *    text == newText;
    */
   abstract void editText(String newText);
}
