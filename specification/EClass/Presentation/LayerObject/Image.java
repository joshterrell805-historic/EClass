package EClass.Presentation.LayerObject;

import java.util.Collection;

/**
 * The Image is a LayerObject for a layer. It can be instantiated
 * and put onto a Layer. Images will be able to be imported from 
 * the users machine.
 * 
 * imagePoints is a collection that will contain all points of the image.
 */
abstract public class Image extends LayerObject{
    //An image will be represented with a collection of a ImagePoints.
    Collection<ImagePoint> imagePoints;
}
