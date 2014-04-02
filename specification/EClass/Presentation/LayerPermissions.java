package EClass.Presentation;
import java.util.Collection;
import EClass.Person.Student;

/**
 * The LayerPermissions object is an aggregate of the Layer class. It contains a
 * collection of Students that are able to draw on the Layer and a boolean
 * representing if a given layer is locked or unlocked allowing or not allowing
 * the collection of Students to draw on.
 * 
 * @param canDraw
 *            the Collection of Students allowed to draw on the layer
 * @param locked
 *            boolean value representing if a slide can be edited by the
 *            Collection of Students
 */
public abstract class LayerPermissions {
	Collection<Student> canDraw;
	boolean locked;
}
