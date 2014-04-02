package EClass.Person;

import EClass.ApprovalTracker.ApprovalRating;
import EClass.Presentation.Layer;
/**
 * Student contains informaton on the student.
 *
 * It contains things like if they are here, if their hand is raised, layers they might want to push,
 * current approval, and their permissions/restrictions to how they use the app.
 */
abstract public class Student extends Person {
    /**
     * States the permission level of the student to do various things inside the app.
     */
	private StudentPermissions permissions;
    /**
     * States whether a student is logged in and viewing the lecture or not.
     */
	private boolean present;
    /**
     * States whether a student is local or remote access.
     */
	private boolean local;
    /**
     * States if a student has been kicked.
     */
	private boolean kicked;
    /**
     * Information of whether a hand is raised and if there is a question attached.
     */
	private Hand hand;
    /**
     * One of the students layers that they are trying to push the the main presentation.
     */
	private Layer pushedLayer;
    /**
     * The last approval rating the student submitted for the lecture.
     */
	private ApprovalRating approval;


	/**
	 * When a student logs on to the EClass this function is called to set the correct feilds
	 */
	/*@
	 * requires
	 *  // The student is not already present
	 *  (\exists Student s; students.contains(s))
	 *  && !(s.isPresent());
    * ensures
    *  // That the status of the student will be set to present
    *  (s.isPresent() == true);
    @*/
    public abstract boolean checkIn(boolean local);
    public abstract boolean leave();
    public abstract void pushLayer(Layer l);
    public abstract Layer pullBackLayer();
    public abstract void submitApproval();

    /**
     * Toggle whether a hand is raised. Could be putting a hand up or down
     */
    /*@
     * ensures
     *    // The hand's state has been changed, and the rest of the data is unchanged.
     *    \old(permissions) == permissions
     *    && \old(present) == present
     *    && \old(local) == local
     *    && \old(kick) == kick
     *    && \old(hand) != hand
     *    && \old(pushedLayer) == pushedLayer
     *    && \old(approval) == approval;
    @*/
    public abstract void toggleHandraise(String question);
    /**
     * Tells if the student has been kicked.
     *
     * @return whether this Student is kicked
     */
    /*@
     * ensures
     *    // The value of kick is returned
     *    \return == kick
     *       &&
     *    // The data is unchanged.
     *    \old(permissions) == permissions
     *    && \old(present) == present
     *    && \old(local) == local
     *    && \old(kick) == kick
     *    && \old(hand) == hand
     *    && \old(pushedLayer) == pushedLayer
     *    && \old(approval) == approval;
     */
    public abstract boolean isKicked();
    /**
     * Tells if the student has is local or remote.
     *
     * @return whether this Student is local
     */
    /*@
     * ensures
     *    // The value of local is returned
     *    \return == local
     *       &&
     *    // The data is unchanged.
     *    \old(permissions) == permissions
     *    && \old(present) == present
     *    && \old(local) == local
     *    && \old(kick) == kick
     *    && \old(hand) == hand
     *    && \old(pushedLayer) == pushedLayer
     *    && \old(approval) == approval;
     */
    public abstract boolean isLocal();
    /**
     * Tells if the student is present.
     *
     * @return whether this Student is present
     */
    /*@
     * ensures
     *    // The value of present is returned
     *    \return == present
     *       &&
     *    // The data is unchanged.
     *    \old(permissions) == permissions
     *    && \old(present) == present
     *    && \old(local) == local
     *    && \old(kick) == kick
     *    && \old(hand) == hand
     *    && \old(pushedLayer) == pushedLayer
     *    && \old(approval) == approval;
     */
    public abstract boolean isPresent();
    /**
     * Get the full student permissions of a Student.
     * @return the permissions
     */
    /*@
     * ensures
     *    // The student permissions of this Student are equal to the return value.
     *    \result == permissions
     *       &&
     *    // The data is unchanged.
     *    \old(permissions) == permissions
     *    && \old(present) == present
     *    && \old(local) == local
     *    && \old(kick) == kick
     *    && \old(hand) == hand
     *    && \old(pushedLayer) == pushedLayer
     *    && \old(approval) == approval;
    @*/
    public abstract StudentPermissions getStudentPermissions();
    
    public abstract void changeStudentPermissions(StudentPermissions sp);

}
