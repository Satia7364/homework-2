class Course:
    def __init__(self, course_name,
                 course_id, course_credits):
        self.course_name= course_name
        self.course_id= course_id
        self.course_credits= course_credits
    def __str__(self):
        return f"課程名稱: {self.course_name}\n課程代碼 = {self.course_id}\n課程學分 = {self.course_credits}"
    
class Student:
    def __init__(self, eclass, id, name):
        self.eclass = eclass
        self.id = id
        self.name= name
    def __str__(self):
        return f"班級: {self.eclass}\n學號: {self.id}\n姓名: {self.name}"
    def addCourse(self, object):
        self.course =object
c1 = Course(course_name="套裝軟體應用", 
            course_id="(G0D17M01",
            course_credits=3)
s1= Student("資工二乙", "4b1g0072", "王小明")
s1.addCourse(c1)
print(s1)