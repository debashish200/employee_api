from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import AllowAny

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')

        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)

        return queryset

    
