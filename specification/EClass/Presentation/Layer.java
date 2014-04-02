package EClass.Presentation;
import java.util.Collection;
import EClass.Presentation.LayerObject.LayerObject;

/**
 * A Layer object is essentially a stack-able, editable image on top of a Slide.
 * It is an aggregate of a Slide, as a Slide may have a Collection of Layers,
 * and aggregates both a LayerObject and LayerPermissions.
 *
 * @param objects
 *            A Collection of LayerObjects that represent all graphics on a
 *            Layer
 * @param opacity
 *            A double representing how transparent a Layer is
 * @param permissions
 *            The LayerPermissions for a given Layer
 * @param visible
 *            Boolean value representing if a Layer can or cannot be seen
 */
public abstract class Layer {
	Collection<LayerObject> objects;
	double opacity;
	LayerPermissions permissions;
	boolean visible;

	/**
	 * addObject returns a boolean representing if an object was successfully
	 * added to the Layer. It takes in the object the presenter or student
	 * wishes to add to the Layer. Only one object can be added to the Layer at
	 * a time.
     * @param object the new LayerObject to be added to the layer
	 */
    /*@
     * requires
     *    //The LayerObject is initialized
     *    object != null
     *
     *    &&
     *
     *    //The objects collection is initialized
     *    objects != null;
     *
     * ensures
     *    //The LayerObject is added to the layer.
     *    objects.size == \old(objects.size) + 1
     *
     *    &&
     *
     *    // The collection contains the new object.
     *    objects.contains(object);
    @*/
	abstract boolean addObject(LayerObject object);

	/**
	 * removeObject returns a boolean representing if an object was successfully
	 * removed form the Layer. It takes in the object on the Layer that the
	 * presenter or student wishes to remove from the Layer. Only one object
	 * can be removed from a Layer at a time and only objects on the Layer can
	 * be removed.
     * @param object the object to be removed from the layer
	 */
    /*@
     * requires
     *    //The LayerObject exists in the layer and is initialized
     *    object != null
     *     
     *    &&
     *
     *    // the objects collection contains the object to be removed.
     *    objects.contains(object)
     *
     *    &&
     *
     *    objects != null;
     *
     * ensures
     *    //The LayerObject is removed from the layer
     *    !objects.contains(object)
    @*/
	abstract boolean removeObject(LayerObject object);

	/**
	 * orderObject will re-order the objects by moving a given object to a
	 * different location on the object stack. It takes in the object on the 
    * Layer that the presenter or student wishes to re-order on the Layer stack.
    * It also takes in the index, or place, at which the layer will be moved to.
     * @param object the LayerObject to be re-ordered
     * @param newIndex the index, or location, where the object is to be placed
	 */
    /*@
     * requires
     *    // The LayerObject exists in the layer and is initialized
     *    object != null
     *
     *    &&
     *
     *    // The objects collection contains the object to be removed
     *    objects.contains(object)
     *
     *    &&
     *
     *    objects != null
     *
     *    &&
     *    
     *    // The index is a valid integer
     *    newIndex != null
     *
     * ensures
     *    // The LayerObject is re-ordered
     *    object.index != \old{object.index)
    @*/
	abstract void orderObject(LayerObject object, int newIndex);
}
