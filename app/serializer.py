from rest_framework import serializers
from app.models import *

class EmployeeMS(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['Ename','Eid']