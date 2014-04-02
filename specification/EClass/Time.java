package EClass;

/**
 * A Time object holds the milliseconds since the beginning of the current day, have
 * methods to convert the current time into a string and return the current seconds of the time,
 * minutes of the time, and hours of the time.
 *
 *
 */

abstract public class Time {
   /**
    * Variable that holds the current time in milliseconds.
    */
   double milliseconds;

   /**
   * Returns the second of the current time from 0-59.
   * @return the seconds of the current time
   */
   /*@
    * requires
    *    // The milliseconds field must be initialized to a value greater than or equal to zero.
    *    milliseconds >= 0;
    *
    * ensures
    *    // Milliseconds is converted into seconds
    *    \result Math.floor(milliseconds / 1000);
    *
   @*/
   abstract int getSeconds();

   /**
   * Returns the minutes of the current time from 0-59.
   * @return the minutes of the current time
   */
   /*@
    * requires
    *    // The milliseconds field must be initialized to a value greater than or equal to zero.
    *    milliseconds >= 0;
    *
    * ensures
    *    // Milliseconds is converted into minutes
    *    \result Math.floor(milliseconds / 60000);
    *
   @*/
   abstract int getMinutes();

   /**
   * Return the hours of the current time from 1-12.
   * @return the hours of the current time
   */
   /*@
    * requires 
    *    // The milliseconds field must be initialized to a value greater than or equal to zero.
    *    milliseconds >= 0;
    *
    * ensures
    *    // Milliseconds is converted into hours
    *    \result Math.floor(milliseconds / 3600000);
    *
   @*/
   abstract int getHours();

   /**
   * Return the whole time "HH:MM:SS" as a string.
   * @return formatted time as a string
   */
   /*@
    * requires
    *    // The Time object must be initialized
    *    this != null;
    *
    * ensures
    *    // A valid String object created and returned representing the time
    *    \result != null;
   @*/
   @Override
   public abstract String toString();
}
