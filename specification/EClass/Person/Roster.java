package EClass.Person;
import java.util.Collection;

/**
 * A Roster contains all of the students in the class and methods to manage the students.
 */
public abstract class Roster {
   /** Contains each student enrolled in the class associated with the presentation */
   Collection<Student> students;
   
   /**
    * KickStudent kicks a student from the current session.
    */
   /*@
    * requires
    *    // The student object must be initialized.
    *    student != null
    *
    *    &&
    *
    *    // There must be at least one student on the roster.
    *    !students.isEmpty()
    *
    *    &&
    *
    *    // The student to be kicked must be in the current roster.
    *    students.contains(student);
    *
    * ensures
    *    // The student must have kicked status.
    *    \old(student.isKicked()) != student.isKicked();
   @*/ 
   abstract void kickStudent(Student student);

   /**
    * ChangeStudentPermissions sets the permissions for a given student.
    */
   /*@
    * requires
    *    // The permissions object must be initialized.
    *    permissions != null
    *
    *    &&
    *
    *    // The student object must be initialized.
    *    student != null
    *
    *    &&
    *
    *    // There must be at least one student on the roster.
    *    !students.isEmpty()
    *
    *    && 
    *
    *    // The student must be in the roster.
    *    students.contains(student);
    *
    * ensures
    *    // The student's permissions equal the given permissions
    *    student.getStudentPermissions() == permissions;
   @*/
   abstract void changeStudentPermissions(Student student, StudentPermissions permissions);
   
   /**
    * AddNewStudent takes a student and adds them to the roster.
    */
   /*@
    * requires
    *    // The student object must be initialized.
    *    student != null
    *
    *    &&
    *
    *    // The student must not already be on the roster.
    *    !students.contains(student);
    *
    * ensures
    *    // The student is added to the roster.
    *    students.contains(student)
    *
    *    &&
    *
    *    // Returns true if the student was successfully added or false if there was an error.
    *    students.contains(student) ? true : false;
   @*/
   abstract boolean addNewStudent(Student student);
   
   /**
    * RemoveStudent takes a student and removes them from the roster.
    */
   /*@
    * requires
    *    // The student object must be initialized.
    *    student != null
    *
    *    &&
    *
    *    // The student must be on the roster.
    *    students.contains(student);
    *
    * ensures
    *    // The student must no longer be on the roster.
    *    !students.contains(student)
    *
    *    &&
    *
    *    // Returns true if the student was successfully removed or false if there was an error.
    *    !students.contains(student) ? true : false;
   @*/
   abstract boolean removeStudent(Student student);
}
