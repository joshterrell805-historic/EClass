package EClass.Presentation.LayerObject;

/**
 * Rectangle is a LayerObject representing the geometric shape rectangle.
 */
abstract public class Rectangle extends LayerObject
{
   /**
    * The length extends along the x axis when the rectangle has 0 rotation.
    */
   double length;

   /**
    * The height extends along the y axis when the rectangle has 0 rotation.
    */
   double height;

   /**
    * Get the length of this rectangle.
    * @return the length of this rectangle
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
    *    && \old(height) == height
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getLength();

   /**
    * Get the height of this rectangle.
    * @return the height of this rectangle
    */
   /*@
    * ensures
    *    // The size of this object is equal to the return value.
    *    \return == this.height
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(length) == length
    *    && \old(height) == height
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getHegit();

   /**
    * Resize this Rectangle.
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
    *    // The new length and height reflect the ratio change
    *    \old(height) * ratio == height
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
