class Student:
    def __init__(self,name):
        self.name=name
        self.attend=0
        self.grades=[]
        print('Welcome {0}' .format (self.name)) 
    def addGrade(self,grade):
        self.grades.append(grade)
    
    def  getAv(self):
        self.avg=sum(self.grades)/len(self.grades)
        
        print ('My average grade is {0}' .format(self.avg))
    def nextcls(self):
        if (self.avg<=49):
            print ("repeat class")
        else:
            print("proceed to next class")

