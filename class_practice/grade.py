class Student(object):
    def __init__(self, grades, __gender):
        self.grades = grades
        self.__gender = __gender
    
    def add(self, grade):
        self.grades.append(grade)
        return
    
    def Calc_ave(self):
        sum_num = self.calc_sum(self.grades)
        return sum_num/(len(self.grades))

    def fcount(self):
        count = 0
        for i in range(0,len(self.grades)):
            if self.grades[i] < 60:
                count = count + 1
        return count

    def calc_sum(self,grades):
        sum_num = sum(self.grades)
        return sum_num
    
    @classmethod
    def calc_std(cls,grades):
        std = 0
        sum1 = 0
        for i in range(0,len(grades)):
            sum1 = sum1 + grades[i]
        avg = sum1/(len(grades))
        sum2 = 0
        for i in range(0,len(grades)):
            sum2 = sum2 + pow((grades[i]-avg),2)
        std = pow((sum2/len(grades)), 0.5)
        return std

    @property
    def gender(self):
        return self.__gender

grades_list = [100, 40, 20, 70, 56, 89, 100, 30, 20]
gender_list = ["Male", "Female", "Male", "Female", "Female", "Female", "Female", "Female", "Male"]

list1 = Student(grades_list, gender_list)
print("The average grade is", list1.Calc_ave())
print("The fail number is", list1.fcount())
print("The STD is", list1.calc_std(grades_list))
print(list1.gender)
list1.add(60)
print(list1.grades)