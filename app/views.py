from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalcSerializer

# Create your views here.

@api_view()
def hello_world(request):
    return Response({'message': 'hello World!'})

# calculator Without Seializers
@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({'message': 'hello Admin!'})
    elif request.method == 'POST':
        return Response({'message': 'hello %s' % request.data['name']}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def calculator(request):
    try:
        num1 = request.data['num1']
        num2 = request.data['num2']
        opr = request.data['opr']
    except:
        return Response({'error:': "Enter valid num1, num2 and opr!"}, status=status.HTTP_404_BAD_REQUEST)
    else:
        if isinstance(num1, int) and isinstance(num2, int):
            if opr == '+':
                return Response({'result': num1 + num2})
            elif opr == 'x':
                return Response({'result': num1 * num2})
            
            elif opr == '-':
                return Response({'result': num1 - num2})
            
            elif opr == '/':
                return Response({'result': num1 / num2})

            else:
                return Response({"error": "send Valid opr !"}, status=status.HTTP_400_BAD_REQUEST)

        else: 
            return Response({'error':  'send integer values!'}, status=status.HTTP_400_BAD_REQUEST)

# calculator With Seializers
@api_view(['POST'])
def calculatorWithSerializer(request):
    ser = CalcSerializer(data=request.data)

    if ser.is_valid():
        num1 = ser.data['num1']
        num2 = ser.data['num2']
        opr = ser.data['opr']

        if opr == '+':
            return Response({'result': num1 + num2})
        
        elif opr == 'x':
            return Response({'result': num1 * num2})
            
        elif opr == '-':
            return Response({'result': num1 - num2})
            
        elif opr == '/':
            return Response({'result': num1 / num2})

        else:
            return Response({"error": "send Valid opr !"}, status=status.HTTP_400_BAD_REQUEST)


    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)