package EClass.Presentation.LayerObject;

import java.util.Collection;

/**
 * The FreeLine will represent a combination of Points to be presented 
 * onto the screen. Uses can include things such as free drawing, 
 * writing, or any other thing onto the whiteboard.
 * 
 * points is a collection of points that will represent all points in the 
 * FreeLine. All lines in points will be presented to the Presentation.
 */
abstract public class FreeLine extends LayerObject {
    //A collection of points that represent the free line drawing.
    Collection<Point> points;

    /**
     * Modify the FreeLine at a selected point on the FreeLine so that points
     * near the FreeLine move in the intended direction as well.
     */ 
    /*@ requires
     *    points != null;
     * ensures
     *    \old(points) != points;
     */
    abstract void wiggle();
}
