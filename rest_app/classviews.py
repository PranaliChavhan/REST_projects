# class based view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views import View
from rest_app.serializers import StudentSerializer
from rest_app.models import Student

def common_lines(request):
    byte_data = request.body
    streamed_data = io.BytesIO(byte_data)
    python_dict = JSONParser().parse(streamed_data)
    return python_dict


class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        python_data = common_lines(request)
        sid = python_data.get("id")
        if sid:
            stud = Student.objects.get(id = sid)
            python_obj = StudentSerializer(stud)
            json_data = JSONRenderer().render(python_obj.data)
            return HttpResponse(json_data, content_type = 'application/json')
        studs = Student.objects.all()
        python_obj = StudentSerializer(stud)
        json_data = JSONRenderer().render(python_obj.data)
        return HttpResponse(json_data, content_type = 'application/json')
    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass