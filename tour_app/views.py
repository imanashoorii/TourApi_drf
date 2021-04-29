from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import tourSerializer

# Create your views here.


@api_view(['POST'])
def createTour(request):

    data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'capacity': request.data['capacity'],
        'description': request.data['description'],
    }

    ser = tourSerializer(data=data)

    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)