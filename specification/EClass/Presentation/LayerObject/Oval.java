package EClass.Presentation.LayerObject;

/**
 * Oval is a LayerObject representing the geomtric shape oval.
 */
abstract public class Oval extends LayerObject
{
   /**
    * The radius extending in the x direction of this oval when the rotation
    *  is at 0 radians.
    */
   double radiusX;

   /**
    * The radius extending in the y direction of this oval when the rotation is
    *  at 0 degrees.
    */
   double radiusY;

   /**
    * Get the radius of this oval in the x direction.
    *  (assuming the oval has 0 rotation).
    * @return the x radius of this oval
    */
   /*@
    * ensures
    *    // The size of this object is equal to the return value.
    *    \return == this.radiusX
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(radiusX) == radiusX
    *    && \old(radiusY) == radiusY
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getRadiusX();

   /**
    * Get the radius of this oval in the y direction.
    *  (assuming the oval has 0 rotation).
    * @return the y radius of this oval
    */
   /*@
    * ensures
    *    // The size of this object is equal to the return value.
    *    \return == this.radiusY
    *       &&
    *    // The data is unchanged.
    *    \old(center) == center
    *    && \old(color) == color
    *    && \old(radiusX) == radiusX
    *    && \old(radiusY) == radiusY
    *    && \old(rotationInRadians) == rotationInRadians;
   @*/
   double getRadiusY();

   /**
    * Resize this Oval.
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
    *    // The new radii reflect the ratio change
    *    \old(radiusX) * ratio == radiusX
    *    && \old(radiusY) * ratio == radiusY
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
