from django.db import models

# Create your models here.
class ParticularCourse(models.Model):
    Course_video_identifier_name=models.CharField(max_length=100,blank=True)
    Course_video=models.CharField(max_length=300)
    def __str__(self):
        return self.Course_video_identifier_name


class Register(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    otp=models.IntegerField(default=0)
    password=models.CharField(max_length=16)
    Paid=models.BooleanField(default=False)
    Course_purchased=models.CharField(blank=True,max_length=100)
    def __str__(self):
        return self.name

    
class OverView(models.Model):
    Course_overview=models.CharField(max_length=1000)
    Course_r=models.ForeignKey(ParticularCourse,related_name="Review",on_delete=models.CASCADE)
    def __str__(self):
        return self.Course_overview

class Demo(models.Model):
     Course_QA=models.CharField(max_length=100)
     Course_r=models.ForeignKey(ParticularCourse,related_name='Demo',on_delete=models.CASCADE)
     def __str__(self):
         return self.Course_QA

class CourseContent(models.Model):
    Course_PName=models.CharField(max_length=100)
    Course_name=models.CharField(max_length=100)
    Course_students=models.CharField(max_length=100)    
    Course_image=models.ImageField(unique=True)
    Course_price=models.CharField(max_length=100)
    Course_rating=models.CharField(max_length=100)
    Course_time=models.CharField(max_length=100)
    Course_use=models.ForeignKey(ParticularCourse,related_name="kush",on_delete=models.CASCADE)
    def __str__(self):
        return self.Course_PName
    
class Rating(models.Model):
    Course_ratername=models.CharField(max_length=51)
    Course_rate=models.CharField(max_length=77)
    Course_rateview=models.CharField(max_length=1999)
    Course_rawrate=models.ForeignKey(ParticularCourse,related_name="rateview",on_delete=models.CASCADE)
    def __str__(self):
        return self.Course_ratername

class Inquerry(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)   
    mobile=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name + " is Requested Us to InQuerry The Mobile Number Is :=>"+ self.mobile




class Paid_Course_Content(models.Model):
    Select= models.CharField(max_length = 20,choices =( 
    ("Java", "Java"), 
    ("Python", "Python"), 
    ("Dot_net", "Dot_net"), 
    ("Javascript", "Javascript")))
    Course_name=models.ForeignKey(CourseContent,on_delete=models.CASCADE)
    Paid_Course_video=models.CharField(max_length=200)   
    Course_Heading=models.ForeignKey(Demo,on_delete=models.CASCADE)
    def __str__(self):
        return self.Select