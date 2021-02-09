from src.service.detail import detail
from src.service.courseDetail import courseDetail
from src.service.menu import menu
from src.model.course import Course
from src.model.routine import Routine
from src.repository.courses import courses
from src.repository.routineList import routineList





#main menu logic
def mainMenu():
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
