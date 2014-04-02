package EClass.Presentation;
import java.util.Collection;

/**
 * A Slide object that can be edited by a presenter or participant. A
 * Slide contains between one and multiple layers that can be drawn on and
 * pushed to the presenter. Only one layer can be pushed to the presenter at a
 * time. The num int represents which slide it is. The presentationHTML is the
 * HTML mark-up for the presentation that is on the given slide.
 * 
 * @param layers
 *            the Collection of layers related to the given slide
 * @param num
 *            the integer representing the slide
 * @param presentationHTML
 *            the HTML that is used to draw the background of the slide
 */

public abstract class Slide {
	Collection<Layer> layers;
	int num;
	PresentationHTML presentationHTML;

	/**
	 * orderLayer will re-order the layers by moving a given layer to a
	 * different location on the layer stack. It will take in the Layer 
    * the presenter or student wants to re-order and the new index at 
    * which to place the layer.
     * @param layer the Layer to be moved
     * @param newIndex the index of where the layer will be moved to
	 */
    /*@
     * requires
     *    //The Layer is initialized
     *    layer != null
     *
     *    &&
     *
     *    //The layers collection is initialized
     *    layers != null
     *
     *    &&
     *
     *    //The index is a valid integer
     *    newIndex != null
     *
     * ensures
     *    //The layer has been moved to the new index
     *    layer.index != \old{layer.index)
    @*/
	abstract void orderLayer(Layer layer, int newIndex);
}
