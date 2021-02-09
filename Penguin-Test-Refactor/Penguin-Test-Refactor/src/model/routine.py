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