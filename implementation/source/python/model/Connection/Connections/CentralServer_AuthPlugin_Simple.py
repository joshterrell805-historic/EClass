# user simple auth plugin for test purposes
_students = [
   {
      'firstname' : 'Josh',
      'lastname'  : 'Terrell',
      'username'  : 'jmterrel'
   },
   {
      'firstname' : 'Mike',
      'lastname'  : 'Sevilla',
      'username'  : 'mjsevill'
   },
   {
      'firstname' : 'Student',
      'lastname'  : 'LastName',
      'username'  : 'student'
   }
]

# the first presenter in this array is displayed as the presenter hosting
# classes, although any presenter can host
# First and last name together form a key.. MUST BE UNIQUE
_presenters = [
   {
      'firstname' : 'Gene',
      'lastname'  : 'Fisher',
      'username'  : 'gfisher'
   }
]
def _getUsername(user):
   return user['username']
_studentUsernames = map(_getUsername, _students)
_presenterUsernames = map(_getUsername, _presenters)

_classes = ['CPE 309','CPE 357']

def _classNameToPresenterClass(className):
   return {
      'name'     : className,
      'students' : _students
   }

def _classNameToStudentClass(className):
   return {
      'name'      : className,
      'firstname' : _presenters[0]['firstname'],
      'lastname'  : _presenters[0]['lastname']
   }

_presenterClasses = map(_classNameToPresenterClass, _classes)
_studentClasses = map(_classNameToStudentClass, _classes)

def login(username, password, callback):
   if username in _presenterUsernames:
      user = _presenters[_presenterUsernames.index(username)]
      callback({
         'success'   : True,
         'role'      : 'presenter',
         'firstname' : user['firstname'],
         'lastname'  : user['lastname'],
         'classes'   : _presenterClasses
      });
   elif username in _studentUsernames:
      user = _students[_studentUsernames.index(username)]
      callback({
         'success'   : True,
         'role'      : 'student',
         'firstname' : user['firstname'],
         'lastname'  : user['lastname'],
         'classes'   : _studentClasses
      });
   else:
      callback({
         'success' : False,
         'reason'  : 'invalid credentials'
      })
