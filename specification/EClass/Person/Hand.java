package EClass.Person;
import EClass.*;

/**
 * The Hand class represents a Student virtually asking a question. The Hand
 * class is an aggregate of the Student class and aggregates the Time class and
 * Date class.
 * 
 * @param question
 *            A string representing the Student's question
 * @param raised
 *            Boolean value representing if a Student has a question
 * @param timeRaised
 *            The hour and minute the Student raised their hand
 * @param dateRaised
 *            The month, day, and year the Student raised their hand
 */
public abstract class Hand {
	String question;
	boolean raised;
	Time timeRaised;
	Date dateRaised;
}
