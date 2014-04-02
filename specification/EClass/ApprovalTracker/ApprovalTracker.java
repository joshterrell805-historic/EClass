package EClass.ApprovalTracker;
import java.util.Collection;

/**
 * An ApprovalTracker contains all of the current ratings and methods for tracking how
 * well students are understanding an EClass presentation.
 */

public abstract class ApprovalTracker {
   /** Holds each approval rating collected during a presentation */
   Collection<ApprovalRating> approvalRatings;

   /**
    * GetCurrentAverage takes all of the current student approval ratings and returns 
    * the average.
    */
   /*@
    * requires
    *    //There must be at least one rating.
    *    approvalRatings.size() >= 1;
    * ensures
    *    //Return value is equal to the arithmetic mean of all the ratings.
    *    \result >= 0.0;
   @*/
   abstract double getCurrentAverage();
}
