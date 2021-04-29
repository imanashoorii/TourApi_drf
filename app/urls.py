from django.urls import path
from .views import hello_world, hello, calculator, calculatorWithSerializer

urlpatterns = [
    # localhost:8000/api/hello -> {message: hello World!}
    path('hello/', hello_world, name='hello'),
    # localhost:8000/api/name -> GET:{message: hello Admin!}, POST:{message: hello {req.data.name}}
    path('name/', hello, name='name'),
    # localhost:8000/api/calculator -> POST: num1, num2, opr
    path('calculator/', calculator, name='calculator'),
    # localhost:8000/api/calculator -> (SerializerValidation) POST: num1, num2, opr
    path('calculatorser/', calculatorWithSerializer, name='calculatorWithSerializer'),

]