package EClass.Person;

/**
 * PresentationPermissionLevel is a permission level determining student 
 *  drawing capabilities.
 */
public enum PresentationPermissionLevel
{
   /**
    * The student may not draw on his own layers on his own machine
    *  and he may not push a layer. The intent of this option is to allow the
    *  presenter to draw full attention to his presentation.
    */
   Lockdown,

   /**
    * The student may draw on his own layers, and may ask to add his
    *  layer to the presenter's layer stack by "push"ing that layer.
    */
   Normal,

   /**
    * The student may draw on his own layers and push layers
    *  to the public stack freely. Also, the student may draw freely on the
    *  layers of the public stack.
    */
   Unrestricted
}
