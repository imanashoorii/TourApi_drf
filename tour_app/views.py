from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import tourSerializer

from .models import Tour

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
        print('Tour Created Successfully')
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listTour(request):
    tours = Tour.objects.all()
    ser = tourSerializer(tours, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def editTour(request, pk):
    
    try:
        tour = Tour.objects.get(pk=pk)
    except:
        return Response({'error': 'Tour not exists !'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == "GET":
        ser = tourSerializer(tour)
        
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = tourSerializer(tour, data=request.data)

        if ser.is_valid():
            ser.save()

            print("Tour Updated")
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)
            

    elif request.method == "DELETE":
        tour.delete()
        return Response( {'message': 'Tour Deleted!'}, status=status.HTTP_204_NO_CONTENT)
