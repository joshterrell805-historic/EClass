package EClass;
import EClass.ApprovalTracker.ApprovalTracker;
import EClass.Presentation.Presentation;
import EClass.Person.*;
import EClass.Forum.Forum;

/**
 * An EClass contains all of the major components needed for an electronic classroom session.
 * These include a Presentation, Roster, Forum, and ApprovalTracker.
 */
public abstract class EClass {
   /** Holds all presentation information for an EClass session */
   Presentation presentation;
   /** The class roster for the current presentation */
   Roster roster;
   /** Holds all information for an ongoing forum */
   Forum forum;
   /** Enables approval tracking operations and data collection */
   ApprovalTracker tracker;
   /** Used to interact with presentation audio */
   Audio audioStream;
   /** Used to interact with presentation video */
   Video videoStream;
}
