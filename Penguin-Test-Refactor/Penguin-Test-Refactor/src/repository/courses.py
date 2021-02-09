from src.model.teacher import Teacher
from src.model.course import Course


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

