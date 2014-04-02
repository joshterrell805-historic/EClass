package EClass.ApprovalTracker;
import EClass.*;

/**
 * The ApprovalRating is an object that contains a rating for a specific slide at a specific time.
 *
 *
 */

abstract public class ApprovalRating {
   /**
    * Variable that holds a student's rating.
    */
   double rating;
   /**
    * Variable that holds the time the rating was made.
    */
   Time time;
   /**
    * Variable that holds the date the rating was made on.
    */
   Date date;
   /**
    * Vairable that holds the slide number the rating was made on.
    */
   int slideNum;
}
