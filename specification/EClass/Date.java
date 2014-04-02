package EClass;

/**
 * A Date is an object that contains the amount of milliseconds since the epoch and methods that
 * convert a date to a formatted string, and return the current day, month, and year.
 *
 *
 */

abstract public class Date {
   /**
    * Variable that holds the current time in milliseconds that can be converted to a date.
    */
   double milliseconds;

   /**
   * Returns the day of the month from 0-31.
   * @return the day of the month
   */
   /*@
    * requires
    *    // The milliseconds field must be initialized to a value greater than or equal to zero.
    *    milliseconds >= 0;
    *
    * ensures
    *    // Milliseconds is used to get the current day from the current milliseconds of time.
    *    \result >= 1 && \result <= 31;
    *
    *
   @*/
   abstract int getDay();

   /**
   * Returns the month of the year from 1-12.
   * @return the current month
   */
   /*@
    * requires
    *    // The milliseconds field must be initialized to a value greater than or equal to zero.
    *    millisconds >= 0;
    *
    * ensures
    *    // Milliseconds is used to get the current month from the current milliseconds of time.
    *    \result >= 1 && \result <= 12;
    *
   @*/
   abstract int getMonth();

   /**
   * Return the current year.
   * @return the year
   */
   /*@
    * requires
    *    // The millisecond field must be initialized to a value greater than or equal to zero.
    *    milliseconds >= 0;
    *
    * ensures
    *    // Millisecond is used to get the current year from the current milliseconds of time.
    *    \result > 2014;
    *
   @*/
   abstract int getYear();

   /**
   * Returns the date in "mm-dd-yyyy" form.
   * @return the formatted date in String form
   */
   /*@
    * requires
    *    // The Date object must be initialized
    *    this != null;
    *
    * ensures
    *    // A valid String object created and returned representing the current date.
    *    \result != null;
    *
   @*/
   @Override
   public abstract String toString();
}
