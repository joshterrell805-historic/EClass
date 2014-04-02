package EClass.Presentation.LayerObject;

/**
 * LayerObject is a graphical object to be drawn on a Layer.
 *
 * LayerObjects are represented as instructructions to draw an object.
 *
 * LayerObjects are a collection of all the data necissary to draw themselves
 *  on the layer including position, size, and color.
 *
 * LayerObjects are responsible for drawing image representations of themselves
 *  in the draw() method.
 *
 * LayerObjects may be manipulated (move, resize, setColor, and rotate).
 */
abstract public class LayerObject
{
   /**
    * The center of the layer object with respect to the origin of the layer.
    *
    * <b>Note: as should be described in layer, the origin or (0,0) of graphical
    *  regions in the white board, layer, and layerobjects are at the center
    *  of those regions. That means that a positive x center for a layer object
    *  places this layer object right of center of the layer, and a negative
    *  y center for this layer object places this layer object below the
    *  center of the layer.</b>
    *
    * This coordinate system is consistent across other aspects of EClass such
    *  as relocating objects.
    */
   Point center;

   /**
    * The color of this layer object.
    */
   Color color;

   /**
    * The rotation in radians of this object where a positive change in radians
    *  rotates the object counter clock-wise.
    */
   double rotationInRadians;

   /**
    * Draw the LayerObject.
    *
    * Note: After we decide which graphics library to use, this method will
    *  be passed the necissary graphics objects to draw itself on the graphics
    *  object.
    *
    * Note: It would be smart to cache an image of this LayerObject
    *  and provide some sort of isChanged() method on this object.
    */
   /*@
    * requires
    *    // The object must have a center and a color. Other data needed to
    *    //  draw the object is contained in subclasses.
    *    center != null
    *       &&
    *    color != null;
    * ensures
    *    // The object is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians
    *
    *       &&
    *    // The graphics object has the newly drawn layer object. Since we 
    *    // don't have a graphics library yet, this is a bit impossible to
    *    // JML.
    *    true;
    */
   abstract void draw();

   /**
    * Move this object to be centered at the specified point.
    * @param center the new center of this object.
    */
   /*@
    * requires
    *    // The parameter is a valid point.
    *    position != null;
    *
    * ensures
    *    // The new center is equal to the parameter.
    *    this.center == center

    *       &&
    *    // Other data is unchanged
    *    \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   abstract void move(Point center);

   /**
    * Resize the LayerObject.
    *
    * How resizing occurs depends on which kind of layer object this is.
    *
    * @param ratio the ratio of the current size to resize this
    *  layer object to.
    *
    * Ex:
    * layerObject.resize(2.0)  // make this object twice as large
    * layerObject.resize(0.25) // shrink this object to 1/4 of its current size
    */
   /*@
    *
    * requires
    *    // the ratio is greater than 0 (size must never be zero)
    *    ratio > 0;
    *
    * ensures
    *    // The other data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
    */
   abstract void resize(double ratio);

   /**
    * Change the rotation of this LayerObject.
    * @param rotationInRadians the new rotation of this LayerObject
    */
   /*@
    * requires
    *    // The parameter must be between +/- 2PI radians
    *    rotationInRadians > -2 * Math.PI
    *       && rotationInRadians < 2 * Math.PI;
    *
    * ensures
    *    // The new angle of this object is equal to the parameter.
    *    this.rotationInRadians == rotationInRadians

    *       &&
    *    // No other data is changed.
    *    \old(center) == center
    *    && \old(color) == color;
   @*/
   abstract void rotate(double rotationInRadians);

   /**
    * Set the color of this LayerObject.
    * @param color the color to set this object to
    */
   /*@
    * requires
    *    // The parameter color must be initialized.
    *    color != null;
    *
    * ensures
    *    // The new color of this object is equal to the parameter.
    *    this.color == color
    *
    *       &&
    *    // The other data is unchanged.
    *    \old(center) == center
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   abstract void setColor(Color color);

   /**
    * Get the color of this object.
    * @return the Color of this LayerObject
    */
   /*@
    * ensures
    *    // The color of this object is equal to the return value.
    *    \result == this.color
    *
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   Color getColor();

   /**
    * Get the center point of this object.
    * @return the center Point of this LayerObject
    */
   /*@
    * ensures
    *    // The center of this object is equal to the return value.
    *    \result == this.center
    *
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   Point getCenter();
   
   /**
    * Get the rotation in radians of this object.
    * @return the rotation in radians of this LayerObject
    */
   /*@
    * ensures
    *    // The rotation of this object is equal to the return value.
    *       \result == this.rotationInRadians
    *
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getRotation();
}
