package EClass.Forum;
import java.util.Collection;

/**
 * A Forum includes a collection of all written messages in a session. It also provides
 * the methods necessary to write and access the current messages that have been entered.
 */
public abstract class Forum {
   /** Holds each message that has been entered during a presentation */
   Collection<Message> messages;

   /**
    * AddMessage puts a new Message into the list of current messages.
    */
   /*@
    * requires
    *    // The messages collection must be initialized.
    *    messages != null
    *
    *    &&
    *
    *    // The message object must be initialized.
    *    message != null
    *
    *    &&
    *
    *    // The message length must be greater than zero.
    *    !text.isEmpty();
    *
    * ensures
    *    // The messages collection has one more message.
    *    messages.size() == \old(messages.size()) + 1
    *
    *    &&
    *
    *    // The messages collection contains the message to be added.
    *    messages.contains(message);
   @*/
   abstract void addMessage(Message message);

   /**
    * Refresh updates the visual display to show any new messages that have been added.
    */
   abstract void refresh();

}
