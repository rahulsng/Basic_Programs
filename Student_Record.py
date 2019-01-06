class Student_Record():
	def _init_(self, Name, Course, Roll_num, Age):
		self.Name = Name
		self.Course = Course
		self.Roll_num = Roll_num
		self.Age = Age
		
	def Display(self):
		print(self.Name,end='\t\t')
		print(self.Course,end='\t\t')
		print(self.Roll_num,end='\t\t')
		print(self.Age,end)
		
student = list()
n = int(input("Enter the number of student:"))
print("Student Detail's")
for i in range(n):
	print("Student : ", i+1)
	Name=input("\tName: ")
	Course=input("\tCourse: ")
	Roll_num=input("\tRoll_num: ")
	Age=input("\tAge: ")
	student.append(Student_Record(Name, Course, Roll_num, Age))
	


for i in range(n):
    for j in range(i+1,n):
        if(student[i].Name>student[j].Name):
            temp=student[i]
            student[i]=student[j]
            student[j]=temp

print("Student Information")
print("Name\t\tCourse\tRoll_num\tAge")

for i in range(n):
	student.Display()