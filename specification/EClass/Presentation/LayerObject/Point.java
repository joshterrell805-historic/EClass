package EClass.Presentation.LayerObject;

/**
 * The Point class is used to represent any individual point in a layer.
 * The point is mostly ised in the FreeLine object to represent the user
 * free drawing onto a layer.
 */
abstract public class Point {
    //x represents the position of the point along the horizontal axis
    double x;
    //y represents the position of the point along the horizontal axis
    double y;


    /**
     * Updates the Point to the new location specified by x and y.
     * @param x the new x coordinate
     * @param y the new y coordinate
     */
    /*@
     * requires
     *    this.x != x
     *    this.y != y;
     * ensures
     *    \old(x) != x
     *    \old(y) != y;
     */  
    abstract void modify(double x, double y);
}
