from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def serializers_form(request):
    EQS=Employee.objects.all()
    MSD=EmployeeMS(EQS,many=True)
    return Response(MSD.data)
    