from django.shortcuts import render

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


#get post end point
@api_view(['GET','POST'])
def get_post_method(request):
    if request.method == 'POST':
        return Response({
            'message' : 'Got some data!',
            'data' : request.data
        })
    return Response({
        'message' : 'hellow world'
    })


# add rate limit on our api
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '2/day' #rate limit is 2 day per day

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})


#return model data by using serializer
from .models import *
from .serializers import *
@api_view(['GET'])
def get_user_data(request):
    user_data_object = UserDetails.objects.all()
    serializer = UserDetailSerializer(user_data_object, many = True) #many=true for returnig multipl eobject
    return Response({
        'status' : 200,
        'payload' : serializer.data
    })