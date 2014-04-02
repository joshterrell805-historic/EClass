package EClass.Person;
/**
 * A general person in the EClass, used to log into the app as well as post
 * on the forum.
 */
abstract public class Person {
   /**
    * The name associated with the account.
    */
	private PersonName name;
   /**
    * The username and password combination used to log into the app.
    */
	private Credentials credentials;

   /**
    * Get the name of a person.
    * @return the name of a person
    */
   /*@
    * ensures
    *    // The name of this Person is equal to the return value.
    *    \result == (this.name).toString()
    *
    *       &&
    *    // The data is unchanged.
    *    \old(name) == name
    *    && \old(credentials) == credentials
   @*/
   public abstract String getName();
   /**
    * Set the name of a person.
    *
    * @param name new name of the Person
    */
   /*@
    *
    * requires
    *    // There is a new name
    *    name != null;
    *
    * ensures
    *    // The new name has been set
    *    this.name == name
    *
    *       &&
    *    // The other data is unchanged.
    *    \old(center) == center
    *    && \old(name) == name
    *    && \old(credentials) == credentials;
    */
   public abstract void setName(PersonName name);
   /**
    * Get the credentials.
    * @return the credentials
    */
   /*@
    * ensures
    *    // The credentials is equal to the return value.
    *    \result == Credentials
    *       &&
    *    // The data is unchanged.
    *    \old(name) == name
    *    && \old(Credentials) == Credentials;
   @*/
   public abstract Credentials getCredentials();

}
