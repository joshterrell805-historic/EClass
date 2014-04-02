package EClass.Presentation.LayerObject;

/**
 * A StraightLine object represents a mark or band between two points. A
 * StraightLine is a type of LayerObject and therefore extends the LayerObject
 * class. It also aggregates the Point class.
 * 
 * @param p1
 *            The first point required to make up the StraightLine
 * @param p2
 *            The second point required to make up the StraightLine
 */
public abstract class StraightLine extends LayerObject {
	Point p1;
	Point p2;
}
