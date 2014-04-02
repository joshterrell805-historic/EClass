package EClass.Person;
/**
 * Credentials that a student uses to log into the app. Cannot be changed.
 */
abstract public class Credentials {
   /**
    * The name that is used to log in with, and can be displayed next to the name
    * throughout the app.
    */
	private String username;
   /**
    * Password required to access the app. Unique password username combination
    * for each account.
    */
	private String password;

   /**
    * Get the username.
    * @return the username of a person
    */
   /*@
    * ensures
    *    // The name of this Person is equal to the return value.
    *    \result == username
    *       &&
    *    // The data is unchanged.
    *    \old(username) == username
    *    && \old(password) == password;
   @*/
   abstract public String getUserName();
   /**
    * Try to log the user.
    * @param username attempted username
    * @param password attempted password
    * @return whether the login was succesful
    */
   /*@
    * requires
    *    // That as username and password are supplied.
    *    username != null
    *    && password != null;
    * ensures
    *    // There is a result from trying to log in.
    *    \result == true || false
    *       &&
    *    // The data is unchanged.
    *    \old(username) == username
    *    && \old(password) == password;
   @*/
   abstract public boolean logon(String username, String password);
}
