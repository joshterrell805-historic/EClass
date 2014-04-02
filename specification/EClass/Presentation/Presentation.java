package EClass.Presentation;
import java.util.Collection;

/**
 * A Presentation is a collection of slides and their respective layers which is displayed
 * at the center of the EClass. 
 */
public abstract class Presentation {
   /** Contains each of the slides in a presentation */
   Collection<Slide> slides;
   /** Refers the current slide being viewed */
   Slide currentSlide;
}
