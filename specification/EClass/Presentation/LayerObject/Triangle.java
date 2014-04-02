package EClass.Presentation.LayerObject;

/**
 * The Triangle is geometric shape for a Layer object.
 * 
 * The three edges represent the edges of the triangle.
 */
abstract public class Triangle extends LayerObject{
    //First Edge of the triangle, will represent the top right edge when first placed.
    StraightLine firstEdge;
    //Second Edge of the triangle, will represent the top left edge when first placed.
    StraightLine secondEdge;
    //Third Edge of the triangle, will represent the bottom edge when first placed.
    StraightLine thirdEdge;


    /**
     * Changes the selected edge's length to the indicated length of |p1 - p2|
     * @param edge the selected edge of the triangle
     * @param p1 the first new end point
     * @param p2 the second new end point
     */
    /*@
     * @requires
     *     edge != null
     *     && p1 != null
     *     && p2 != null;
     *
     * @ensures
     *     \old(edge) != edge;
     */ 
    abstract void modifyEdgeLength(StraightLine edge, Point p1, Point p2);
}
