#Course Class
class Course:
  def __init__(self, id, cname, teacher):
    self.id = id
    self.courseName = cname
    self.teacherName = teacher.name

  def courseDetails(self):
    print(self.courseName, end=", ")
    print(self.teacherName)

  def courseList(self):
    print(self.id+1,".",self.courseName)

  def printCourseName(self, id, courses):
    print(courses[id].courseName)