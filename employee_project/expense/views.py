from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer

import logging
logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def expense(request):

    if request.method == 'GET':
        expenses = Expense.objects.all()

        logger.info('expense api_view called')

        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

