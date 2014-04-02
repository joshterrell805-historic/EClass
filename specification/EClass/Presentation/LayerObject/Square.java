package EClass.Presentation.LayerObject;

/**
 * Square is a LayerObject representing the gemoetric shape square.
 */
abstract public class Square extends LayerObject
{
   /**
    * The side length of the square.
    */
   double length;

   /**
    * Get the length of this square.
    * @return the side length of this square
    */
   /*@
    * ensures
    *    // The size of this object is equal to the return value.
    *    \return == this.length
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(length) == length
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getLength();

   /**
    * Resize this Square.
    *
    * @param ratio the ratio of the current size to resize this
    *  layer object to.
    */
   /*@
    *
    * requires
    *    // the ratio is greater than 0 (size must never be zero)
    *    ratio > 0;
    *
    * ensures
    *    // The new length reflects the ratio change
    *    \old(length) * ratio == length
    *
    *       &&
    *    // The other data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
    */
   @Override
   abstract void resize(double ratio);
}
