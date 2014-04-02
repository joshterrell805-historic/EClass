package EClass.Forum;
import EClass.Forum.Forum;
import EClass.Person.Person;
import EClass.*;

/**
 * A Message object contains the person who wrote the message, the text of the message to be sent,
 * the time the message was sent, and the date the message was sent.
 *
 *
 */

abstract public class Message {
   /**
    * Variable that holds the information of the person who created the message.
    */
   Person author;
   /**
    * Variable that holds the content of the message.
    */
   String text;
   /**
    * Variable that holds the time the message was created.
    */
   Time time;
   /**
    * Variable that holds the date the message was created.
    */
   Date date;
}
