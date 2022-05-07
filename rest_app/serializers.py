
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_app.models import Student

def name_startswit_P(value):
    if value[0].lower() == 'p':
        return value
    raise ValidationError("Name should starts with P")
def name_len(value):
    if len(value) >= 6:
        return value
    raise ValidationError("length of name should be greater than 6")
'''
class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[name_startswit_P, name_len])
    city = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    marks = serializers.IntegerField()

    def create(self, validated_data):
        stud = Student.objects.create(**validated_data)
        return stud

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.age = validated_data.get('age', instance.age)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.save()
        return instance

    # field level validation
    # to validate single field
    # def validate_age(self, value):
    #     if value >= 21:
    #         return value
    #     raise ValidationError("Age should not be less than 21...!")

    # def validate_marks(self, value):
    #     if value >= 35 and value <=90:
    #         return value
    #     raise ValidationError("marks should be in between 35 to 90")

    # object level validation
    # to validate multiple fields
    # def validate(self, data):
    #     if (data.get("city") == "Pune") and (data.get("age")>=21):
    #         return data
    #     raise ValidationError("City must be Pune and age must be above 21")
'''
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ['id', 'marks']
        read_only_fields = ['name']
        # extra_kwargs = {"name":{"read_only": True}, "age":{"write_only": True}}
        
    