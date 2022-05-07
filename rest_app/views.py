from functools import partial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_app.models import Student
from rest_app.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes that can then be easily rendered into 
# JSON, XML or other content types.

# Serializers also provide deserialization, 
# allowing parsed data to be converted back into complex types, 
# after first validating the incoming data.

def single_stud(request, pk):
    '''get the data of single student'''
    print("In single_stud serializer")
    stud_obj = Student.objects.get(id = pk)    # complex datatype
    python_obj = StudentSerializer(stud_obj) # python datatype
    json_data = JSONRenderer().render(python_obj.data)   #json data
    return HttpResponse(json_data, content_type = 'application/json')

def all_stud(request):
    '''get the data of all students'''
    print("In all_stud serializer")
    stud_obj = Student.objects.all()
    python_obj = StudentSerializer(stud_obj, many = True)
    json_data = JSONRenderer().render(python_obj.data)
    return HttpResponse(json_data, content_type = 'application/json')

@csrf_exempt
def create_data(request):
    '''get data from client and save in database'''
    if request.method == "POST":
        bytes_data = request.body
        streamed_data = io.BytesIO(bytes_data)
        python_data = JSONParser().parse(streamed_data)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            msg = {'msg':'data Saved successfully...!'}
            res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type = 'application/json')
    else:
        msg = {'error':'Other than POST method is not allowed...!'}
        res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type = 'application/json')

def common_lines(request):
    byte_data = request.body
    streamed_data = io.BytesIO(byte_data)
    python_dict = JSONParser().parse(streamed_data)
    return python_dict

@csrf_exempt
def stu_api(request):  
    '''To perform CRUD operations '''                     
    if request.method == "GET":
        python_data = common_lines(request)
        sid = python_data.get("id")

        if sid:                             # if id is passed by client get single stud data
            try:
                stud = Student.objects.get(id = sid)

            except Student.DoesNotExist:
                return JsonResponse({"error":"Given id does not exist...!"})
            ser = StudentSerializer(stud)
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type = 'application/json')

        # if id is not passed get all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many= True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type = 'application/json')

    elif request.method == "POST":
        python_data = common_lines(request)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"Success":"Data saved Successfully...!"})
        return JsonResponse({"Error":ser.errors})
    
    elif request.method == "PUT":
        python_data = common_lines(request)
        sid = python_data.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
        ser = StudentSerializer(instance = stud, data = python_data, partial = True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"Success":"Data updated Successfully...!"})
        return JsonResponse({"Error":ser.errors})
            

    elif request.method == "DELETE":
        python_data = common_lines(request)
        # print(len(python_data))
        # for i in python_data:
        sid = python_data.get("id")
            # print(sid)
        if sid:
            try:
                stud = Student.objects.get(id = sid)
                stud.delete()
                return JsonResponse({"Success":"Data Deleted Successfully...!"})
            except Student.DoesNotExist:
                return JsonResponse({"Error" : "Id does not exists...!"})
        else:
            return JsonResponse({"Error":"Unable to delete the data...!"})

    else:
       return JsonResponse({"error":"Invalid request method...!"})          # Python Dictionary
