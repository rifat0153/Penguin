import os, time
#Routine Class
class Routine:
  def __init__(self, day, hour, courseId):
    self.courseId = courseId
    self.day = day
    self.hour = hour

  def printRoutine(self, routineList,courseList):
    for x in routineList:
      cId = x.courseId
      print(x.day, x.hour, end=" ")
      courseList[cId].printCourseName(cId, courseList)

#Teacher Class
class Teacher:
  def __init__(self, name):
    self.name = name

  def printName(self):
    print("Teachers name is: ",self.name,)

#Course Class
class Course:
  def __init__(self, id, cname, teacher):
    self.id = id
    self.cname = cname
    self.name = teacher.name

  def courseDetails(self):
    print(self.cname, end=", ")
    print(self.name)

  def courseList(self):
    print(self.id+1,".",self.cname)

  def printCourseName(self, id, courses):
    print(courses[id].cname)

#hardcoing teahcers and courses
t0 = Teacher("John Smith") 
t1 = Teacher("Lara Gilbert")
t2 = Teacher("Johana Kabir")
t3 = Teacher("Daniel Robertson")
t4 = Teacher("Larry Cooper")

c0 = Course(0,"English Grammer",t0)
c1 = Course(1,"Mathematics",t1)
c2 = Course(2,"Physics",t2)
c3 = Course(3,"Chemistry",t3)
c4 = Course(4,"Biology",t4)

#working with list is easier
courses = [c0, c1, c2, c3, c4]

#method of main function
def detail(course):
  for x in course:
    x.courseDetails()

def courseDetail(course):
  for x in course:
    x.courseList()

def routineDetail(routine):
  for x in routine:
    pass
#prints the menu
def menu():
  print("\n\nA. Create Routine \nB. Show Routine\nC. List Courses with Teachers Name\n\n")

routineList = []

while(True):
  menu()
  i = input()
  
  if ( i=='A') :
    courseDetail(courses)

    for x in range(0, 5):
      while(True):
        d, h, cId = input().split()
        day = int(d)
        hour = int(h)
        courseIndex = int(cId)

        #validation of inputs
        if(day<0 or day>4):
          print("Invalid input of day. Enter all value again")
        if(hour<0 or hour>3):
          print("Invalid input of hour. Enter all value again")
        if(courseIndex<0 or courseIndex>4):
          print("Invalid input of CourseIndex. Enter all value again")
        if( (day>=0 and day<=4) and (hour>=0 and hour<=3) and (courseIndex>=0 and courseIndex<=4) ):
          break
      
      newRoutine = Routine(day, hour, courseIndex)

      routineList.append(newRoutine)

  if ( i=='B'):
    if not routineList:
      print("Routine is Empty")
    else:
      routineList[0].printRoutine(routineList, courses)
    
  if ( i=='C'):
    detail(courses)

  if(i=='D'):
    break

  os.system('clear')  
  time.sleep(1)