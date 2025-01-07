# Multiple inheritance

class SkillSet:
    def __init__(self,name="",exp=0,poc=0):
        self.skill=name
        self.exp=exp
        self.poc=poc
    def view(self):
        return self.skill+" "+str(self.exp)+" "+str(self.poc)


class Personal:
    def __init__(self,name,qual="",con=0,mail=""):
        self.name=name
        self.qualification=qual
        self.contact=con
        self.mail=mail
    def __str__(self):
        return self.name+" "+self.qualification+" "+str(self.contact)+" "+self.mail


#multiple
class Profile(Personal,SkillSet):
    def __init__(self,user="",q="",c=0,m="",s="",e=0,p=0):
        super(Profile, self).__init__(user,q,c,m)
        self.skill=s;self.exp=e;self.poc=p
    def __str__(self):
        return super(Profile, self).__str__()+" "+self.view()


pro=Profile("nandha","IT",789555,"nadha@gmail.com","core python",10,3)
pro1=Profile("Annamalai","cse",1245,"sam@gmail.com","Python and Java")
print(pro)
print(pro1)


# class Travels:
#     def name(self):
#         print("YBM TRAVELS")
# class Travels1:
#     def name1(self):
#         print("KPN TRAVELS")
# class main(Travels,Travels1):
#     def Luxary(self):
#         print("Enjoy the journey of the happiness ")
# m=main()
# m.name()       
# m.name1()
# m.Luxary()