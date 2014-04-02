package EClass.Presentation;

/**
 * A PresentationHTML contains all of the markup info and methods needed to create
 * or open a presentation.
 */

public abstract class PresentationHTML {
   /** Contains all of the underlying HTML for a presentation */
   String HTMLcontent;

   /**
    * Draw converts the HTML into a new format and draws it in the whiteboard space.
    */
   abstract void draw();
}
