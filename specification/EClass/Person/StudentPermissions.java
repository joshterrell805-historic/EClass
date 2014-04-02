package EClass.Person;
/**
 * StudentPermissions has various access rights to tools that the student can use.
 */
abstract public class StudentPermissions {
   /**
    * States the ability of the student to push layers to the main presentation
    */
	private boolean canPush;
   /**
    * States the ability of the student to raise their hand and ask a question
    */
	private boolean canRaiseHand;
   /**
    *  PresentationPermissionLevel is a permission level determining student
    *  drawing capabilities.
    */
	private PresentationPermissionLevel wbPermissions;

   /**
    * Toggle the ability to Push
    */
   /*@
    * ensures
    *    // The ability to push is the opposite of what it was before, and all other data is unchanged.
    *    \old(canPush) != canPush
    *    && \old(canRaiseHand) == canRaiseHand
    *    && \old(wbPermissions) == wbPermissions;
   @*/
   public abstract void togglePush();
   /**
    * Respond with the current state of canPush.
    *
    * @return whether this Student has the ability to push
    */
   /*@
    * ensures
    *    // The value of canPush is returned
    *    \return == canPush
    *       &&
    *    // The data is unchanged.
    *    \old(canPush) == canPush
    *    && \old(canRaiseHand) == canRaiseHand
    *    && \old(wbPermissions) == wbPermissions;
    */
   public abstract boolean canPush();
   /**
    * Toggle the ability to Raise Hand
    */
   /*@
    * ensures
    *    // The ability to raise hand is the opposite of what it was before, other data unchanged.
    *    \old(canRaiseHand) != canRaiseHand
    *    && \old(canRaiseHand) == canRaiseHand
    *    && \old(wbPermissions) == wbPermissions;
   @*/
   public abstract void toggleRaisehand();
   /**
    * Respond with the current state of canRaiseHand.
    *
    * @return whether this Student has the ability to push
    */
   /*@
    * ensures
    *    // The value of canRaiseHand is returned
    *    \return == canRaiseHand
    *       &&
    *    // The data is unchanged.
    *    \old(canPush) == canPush
    *    && \old(canRaiseHand) == canRaiseHand
    *    && \old(wbPermissions) == wbPermissions;
    */
   public abstract boolean canRaiseHand();
   public abstract boolean setWBPermission();
   /**
    * Get the whiteboard permissions of a Student.
    * @return the PresentationPermissionLevel
    */
   /*@
    * ensures
    *    // The white board permission are equal to the return value.
    *    \result == wbPermissions
    *       &&
    *    // The data is unchanged.
    *    \old(canPush) == canPush
    *    && \old(canRaiseHand) == canRaiseHand
    *    && \old(wbPermissions) == wbPermissions;
   @*/
   public abstract PresentationPermissionLevel getWBPermission();
}
