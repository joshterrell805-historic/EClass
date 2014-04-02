package EClass.Presentation.LayerObject;

/**
 * Circle is a LayerObject representing the geometric shape circle.
 */
abstract public class Circle extends LayerObject
{
   /**
    * The radius of the circle.
    */
   double radius;


   /**
    * Get the radius of this circle.
    * @return the radius
    */
   /*@
    * ensures
    *    // The size of this object is equal to the return value.
    *    \return == this.radius
    *       &&
    *    // The other data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(raidus) == radius
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getRadius();

   /**
    * Resize this Circle.
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
    *    // The new radius reflects the ratio change
    *    \old(radius) * ratio == radius
    *
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(rotationInRadians) == rotationInRadians;
    */
   @Override
   abstract void resize(double ratio);
}
