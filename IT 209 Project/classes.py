#------------------------------------------------------------------------
# IT209_A8_S20_classes.py - University, Catalog, and Courses classes
#                           meant for import
#          
# Previously created classes (A6 and prior):
#        Department - contains Faculty and Student
#        Person - parent class for Faculty and Student
#        Faculty - inherits from Person, object is a faculty member
#        Student - inherits from Person, object is a student
#
# Author:  Gene Shuman         04/24/2020  
#------------------------------------------------------------------------
# Mods:
#------------------------------------------------------------------------

class Department():
    """ Department class - creates Department objects, each holding a 
        roster of student objects majoring in the Department
        ---------------------------------------------------------- """
    univ_students = 0 # class variable - total # students in all Departments
    count = 0         # class variable - total # Departments created  
    
    def __init__(self, d_code= '', d_name = '', capacity = 5, minGPA = 2.5):
        self.d_code = d_code 
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.num_students = 0
        self.avgGPA = 0.0
        self.roster = [ ]
#       self.qualified = True   # internal attribute used by addStudent()
        self.reason = ''        #    <ditto> 
        Department.count += 1
 
    def __str__(self):
        return('Department ' + self.d_code + ' ' + self.d_name + ' ' +
               ' capacity= ' + str(self.capacity) + ' number of students= ' +
               str(self.num_students) + ' min GPA= ' +
               str(self.minGPA))
    
    def addFaculty(self, f_obj):
        if not f_obj or not isinstance(f_obj, Faculty):
            return False, 'add failed: missing or wrong obj type'
        self.roster.append(f_obj)
        return True, 'added'
        
    def addStudent(self, s_obj):
        if not s_obj or not isinstance(s_obj, Student):
            return False, 'add failed: missing or wrong obj type'
        else:
            self.qualified, self.reason = self.isQualified(s_obj)
            if self.qualified:
                self.roster.append(s_obj)
                self.num_students += 1
                Department.univ_students += 1
                self.calcAvgGPA()
                s_obj.setMajor(self.d_code)  # set Student's major to Dept
            else:
                return False, self.reason
            return True, 'added'

    def isQualified (self, s_obj):
        if self.num_students >= self.capacity:  # Check Dept. capacity
            return (False, 'add failed: over capacity')
        elif s_obj.gpa() < self.minGPA:         # Check student gpa > min
            return (False, 'add failed: minGPA')
        elif not s_obj.isEnrolled():            # Student must be enrolled 
            return (False, 'add failed: not enrolled')
        else:
            if len(self.roster) > 0:            # Check student not already
                for s in self.roster:           #   in Dept. major roster
                    if s.samePerson(s_obj):
                        return (False, 'add failed: already in Department')
        return (True, '')
        
    def calcAvgGPA(self):                       # recalculates Dept. avg GPA
        self.avgGPA = 0
        for s in self.roster:
            if isinstance(s, Student):
                self.avgGPA += s.gpa()
        return (round(self.avgGPA / len(self.roster),2))

    def listFaculty(self):
        print('\nFaculty for the ', self.d_name, ' Department: ')
        for f in self.roster:
            if isinstance(f, Faculty):
                print(f.name, ', ', f.rank)
         
    def printRoster(self, which = 'b', output = 'f'):
        print('\nList in Department ', self.d_name)
        for s in self.roster:
            if which == 'b':
                print(s)
            elif which == 's' and isinstance(s, Student):
                if output == 'f':
                    s.status_summary()
                else:
                    print(s)
            elif which == 'f' and isinstance(s, Faculty):
                if output == 'f':
                    s.status_summary()
                else:
                    print(s)
                
    

#------------------------------------------------------------------
# Person - Parent class for Faculty and Student classes
#
# Author:  Gene Shuman      10/14/2019  (original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Person():
    """ Person Class - parent for Faculty and Student classes 
        ---------------------------------------- """ 
    def __init__(self, g_num, name, address, telephone, email):
        self.g_num = str(g_num) 
        self.name = str(name)
        self.address = str(address)
        self.telephone = str(telephone)
        self.email = str(email)

    def samePerson (self, p_obj):
        return(self.g_num == str(p_obj.g_num) and
               self.name == str(p_obj.name) ) # return True if g_num, name match  

    def __str__(self):
        return('\n\t' + self.name + ', ' + str(self.g_num) +
               '\n\t  ' + self.address + ', ' + str(self.telephone) +
               '\n\t  ' + self.email)
     

#------------------------------------------------------------------
# Faculty - Faculty class, subclass of PErson
#
# Author:  Gene Shuman      10/14/2019  (original from Spring 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Faculty(Person):
    """ Faculty Class - Person subclass 
        ---------------------------------------- """ 
    def __init__(self, g_num, name, address, telephone, email, rank,
                 active, teach_load, specialty, funding):
        super().__init__(g_num, name, address, telephone, email)
        self.g_num = str(g_num) 
        self.name = str(name)
        self.address = address
        self.telephone = telephone
        self.email = email
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.funding = funding

    def __str__(self):        
        return(super().__str__() + '\n\t  ' + 'Rank: ' + str(self.rank) + '\n\t  ' +
               'Specialty: ' + str(self.specialty) + '\n')           

    def status_summary (self):
        if self.active == 'y':
            curr_status = 'active'
        else:
            curr_status = 'inactive'
        print ('\nSummary:\n\t', self.name, ' is a faculty member at GMU ', end = '')
        print ('with g-number ', self.g_num)
        print ('\t Their rank is ', self.rank, ' specializing in ', self.specialty)
        if self.teach_load > 0:            
            print ('\t Their teaching load is ', str(self.teach_load), end = '')
            print (' credit hours per year')

    def activiate (self):
        self.active = 'y'
        return True

    def deactivate (self):
        self.active = 'n'
        return True

#------------------------------------------------------------------
# Student - Student class definition, subclass of Person
#           Identical to A3 class except it inherits from Person
#
# Author:  Gene Shuman      10/14/2019  (Original from Sprint 2018)
#-------------------------------------------------------------------
# Mods:
#-------------------------------------------------------------------
class Student(Person):
    """ Faculty Class - creates Faculty objects, subclass of Person. 
        ------------------------------------------------------------ """ 
    def __init__(self, g_num, name, address, telephone, email,
                 status = 'Freshman', major = 'IST', enrolled = 'y',
                 credits = 0, qpoints = 0):
        super().__init__(g_num, name, address, telephone, email)
        self.status = str(status)
        self.major = str(major)
        self.enrolled = str(enrolled)
        self.credits = credits
        self.qpoints = qpoints

    def __str__(self):        
        return(super().__str__()+ '\n\t  ' + 'Major: ' + str(self.major) + '\n\t  ' +
               'Status: ' + str(self.status) + '\n\t  ' +
               'Active: ' + str(self.enrolled) + '\n\t  ' +
               'Credits: ' + str(self.credits) + '\n\t  ' +
               'GPA  = {0:4.2f}'.format(self.gpa()) + '\n') # calculate gpa, don't store           

    def gpa (self) :
        if self.credits > 0:     # prevent division by zero...
            return self.qpoints / self.credits
        else :
            return 0             # ...if zero credits, return gpa = 0

    def setMajor (self, major) :
        self.major = major
        return True
     
    def isEnrolled (self):
        return (self.enrolled == 'y')    # return True if student is enrolled

    def status_summary (self):
        if self.enrolled == 'y':
            curr_status = 'active'
        else:
            curr_status = 'inactive'
        print ('\nSummary:\n\t', self.name, ' is a student at GMU, ', end = '')
        print ('with g-number ', self.g_num)
        print ('\t They are a ', self.status, ' majoring in ', self.major)
        print ('\t Their gpa is {0:4.2f} and they are currently {1:8s}'
               .format(self.gpa(), curr_status) + '\n')

    def activate (self):
        self.enrolled = 'y'
        return True

    def deactivate (self):
        self.enrolled = 'n'
        return True


#--------------------------------------------------------------------
# University - University class - container for Department objects
#                                 and Catalog objects 
#   Only one object for A8, but could hold other unviersity objects
#
# Author:  Gene Shuman      10/14/2019  (Original from Sprint 2018)
#---------------------------------------------------------------------
class University():
    """ University class - creates Univrsity objects, one for A8. 
        container for Department, Catalog, and Student objects.
        ---------------------------------------------------------- """
    
    def __init__(self, name = 'GMU'):
        self.__name = name
        self.__departments = [ ] # container for Department objects
        self.__catalogs = [ ]    # container for catalogs
        self.__students = [ ]    # container for all univ. student objects
 
    def __str__(self):
        return('University name: ' + self.__name + ', contains ' + 
               str(len(self))+ ' departments ')
    
    def addDept(self, d_obj):
        """Add d_obj to department list """
        pass   # provide code              

    def addCat(self, c_obj):
        """Add c_obj to catalog list """
        pass   # provide code

    def addStudent (self, s_obj):
        """Add s_obj to student list """
        pass   # provide code

    def __contains__(self, u_obj):
        """Return True if u_obj is in the departments list.
           Return True if uobj is in the catalogs list.
           Otherwise return False.                        """
        pass    # provide code 
        
    def listDepts(self):
        """Return a list of all department objects """
        pass    # provide code

    def listStudents(self):
        """Return a list of all student objects """
        pass    # provide code

    def printDepts(self):
        """Print/display the list of departments """
        pass    # provide code

#--------------------------------------------------------------------
# Course - Course class - course objects
#
# Author:  Gene Shuman      04/23/2020  
#---------------------------------------------------------------------
class Course():
    """ Course class - creates Course objects - creeated by A8 appl. 
        Attributes:  d_code from Department object + number + title
                     name of Faculty object instructor
                     <obj.id> of assigned Student objects held in list.
        ---------------------------------------------------------- """
    
    def __init__(self, d_code, number, title, instructor):
        self.__d_code = d_code
        self.__number = number
        self.__title = title
        self.__instructor = instructor  # name - user entered
        self.__students = [ ]   # container for Student objects
 
    def __str__(self):
        return('Course: ' + self.__d_code + '-' + self.__number +
               ' - ' + self.__title + ' Prof: ' + self.__instructor +
               ', ' + str(len(self.__students)) + ' students registered')

    def addStudent (self, s_obj):
        """Add s_obj to students list - return True+'added, or ...
           ...return False if wrong obj type or already in course+reason
        """
        pass    # provide code

    def getNameNumber (self):
        """Return course code+number, eg. "ENGR-101" """
        pass    # provide code

    def __len__(self):
        """Return length of student list """
        pass    # provide code

    def __eq__(self, c_obj):
        """Return True if c_obj and this course have same name+number.
           Otherwise return False.                                   """
        pass    # provide code
 
    def printStudents(self):
        """Print/display the list of students register for this course.
           Use the student object's __str__ method to print.          """
        pass    # provide code

#--------------------------------------------------------------------
# Catalog - Catalog class - contains Course objects
#                    Only one needed for A8
#
# Author:  Gene Shuman      04/23/2020  
#---------------------------------------------------------------------
class Catalog():
    """ Catalog class - creates Catalog object - one for A8 (F2020). 
        Attributes:  name of catalog, e.g., "F2020"
                     <obj.id> of each Course object in catalog
        ---------------------------------------------------------- """
    
    def __init__(self, name):       
        self.__name = name
        self.__courses = [ ]   # container for Course objects
        
 
    def __str__(self):
        return('Catalog: ' + self.__name + ' - ' + 
               str(len(self.__courses)) + ' courses' )

    def getName (self):
        """Return name of catalog. """
        pass    # provide code
    
    def addCourse (self, c_obj):
        """Add c_obj to the courses list, return True+'added'.
           Return False if worng obj type or course already in catalog
           plus a reason code.                                 """
        pass    # provide code

               
    def __len__(self):
        """Return length of courses list - # courses in cat. """
        pass    # provide code

    def __contains__(self, c_obj):
        """Return True if c_obj is in the catalog (in courses list).
           Oterhwise return False.                                 """
        pass    # provide

    def printCatalog(self):
        """Print/display the courses in the catalog.  Use the course
           object __str__ method.                                   """
        pass    # provide code

    def listCourses(self):
        """Return a list of all course objects in the catalog. """
        pass    # provide code
 


