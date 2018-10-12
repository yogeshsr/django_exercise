from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class ExpenseListClassView(APIView):

    def get(self, request, format=None):
        
        expenses = Expense.objects.all()
        
        serializer = ExpenseSerializer(expenses, many=True)
        
        return Response(serializer.data)


class ExpenseList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExpenseListGeneric(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# TODO list and update to be handled by separate mixins