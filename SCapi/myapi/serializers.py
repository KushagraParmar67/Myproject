from .models import CourseContent,ParticularCourse,Paid_Course_Content,Rating,Inquerry,OverView,Register,Demo
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields="__all__"

class OverViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverView
        fields=['Course_overview']

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields=['Course_QA']

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['Course_rate','Course_ratername','Course_rateview']


class ParticularCourseSerializer(serializers.ModelSerializer):
    kush=CourseSerializer(many=True)
    Review=OverViewSerializer(many=True)
    Demo=DemoSerializer(many=True)
    rateview=RatingSerializers(many=True)
    class Meta:
        model = ParticularCourse
        fields=['id','Course_video','kush','Review','Demo','rateview']

class InquerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquerry
        fields = "__all__"
    def create(self,validated_data):
        user = Inquerry(
            name=validated_data['name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            message=validated_data['message']
        )
        user.save()
        return user
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['name','email','mobile','password']
        def create(self,validated_data):
            user=Register(
            name=validated_data['name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password']
            )
            user.save()
            return user

class Paid_Course_Content_Serializers(serializers.ModelSerializer):
    Course_Heading=DemoSerializer()
    # Course_name=CourseSerializer()
    class Meta:
        model=Paid_Course_Content
        fields=["id","Paid_Course_video","Course_Heading","Course_name"]        

from django.contrib.auth.models import Group

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']    
