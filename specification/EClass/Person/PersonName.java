package EClass.Person;
/**
 * PersonName contains the first, middle, and last name of a person.
 */
 abstract public class PersonName {
    private String firstName;
    private String lastName;
    private String middlename;

    /**
	 * Get the name as a String.
	 *
	 * @return The name as a String
	 */
    @Override
    public abstract String toString();
    /**
    * Set the name to the new first, middle, and last name.
    *
    * @param first new first name 
    * @param middle new middle name
    * @param last new last name 
    */
   /*@
    *
    * requires
    *    // There is a new name
    *    first != null
    *    && middle != null
    *    && last != null;
    *
    * ensures
    *    // The new name has been set
    *    firstName == first
    *    && middleName == middle
    *    && lastName == last;
    */
    abstract public void setName(String first, String middle, String last);
    /**
    * Get the name.
    * @return the name
    */
   /*@
    * ensures
    *    // The name is equal to the return value.
    *    \result == first + " " + middle + " " + last
    *       &&
    *    // The data is unchanged.
    *    \old(firstName) == firstName
    *    && \old(middleName) == middleName;
    *    && \old(lastName) == lastName;
   @*/
    abstract public String getName();
 }
