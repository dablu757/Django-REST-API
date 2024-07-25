from django.shortcuts import render

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status


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

#post path operation to get data from uder
@api_view(['POST'])
def create_user(request):
    user_data = request.data
    serializer = UserDetailSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({
            'status code' : 501,
            'error' : serializer.errors,
            'message' : 'something went to wrong'
        })
    
    serializer.save()
    return Response({
        'message' : 'data successfully createed into the table'
            })


@api_view(['PUT'])
def update_user_details(request, id):

    try:
        user_data = UserDetails.objects.get(id = id)
        serializer = UserDetailSerializer(user_data, data=request.data, partial = True) #partial = true means it
        # update only rquired fields not all fielsd i.e just
        #just like PATCH  method

        if not serializer.is_valid():
           return Response({
               'status':403,
               'error' : serializer.errors,
               'message' : 'something went to wrong'
           })
        
        serializer.save()
        return Response({
            'status' : 200,
            'message' : 'data successfully updated'
        }) 

    except Exception as e:
        return Response({
            'status code' : 403,
            'Error' : str(e),
            'message' : 'some ting went to wrong'
        })


# delete path operation
@api_view(['DELETE'])
def delete_user(request):
    try:
        # Get the ID from the query parameters
        user_id = request.GET.get('id')
        print(f"Got id: {user_id}")

        # Check if the ID is provided
        if not user_id:
            return Response({
                'message': 'ID not provided in request'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Try to get the user with the provided ID
        user_obj = UserDetails.objects.get(id=user_id)
        user_obj.delete()
        
        return Response({
            'message': 'User details deleted'
        }, status=status.HTTP_200_OK)
    
    except UserDetails.DoesNotExist:
        return Response({
            'message': 'User not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({
            'message': 'An error occurred',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


# category get path operation
@api_view(['GET'])
def get_category(request):

    try:
        category_obj = Category.objects.all()
        serializer = CategorySerializer(category_obj, many = True)
        return Response({
            'status' : status.HTTP_200_OK,
            'payload' : serializer.data
        })

    except Exception as e:
        return Response({
            'message' : 'something went to wrong',
            'error' : str(e)
        }, status= status.HTTP_400_BAD_REQUEST)
    


# cayegory post path operation
@api_view(['POST'])
def create_category(request):
    data = request.data
    try:
        serializer = CategorySerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'message' : 'please enter valid data'
            })
        
        serializer.save()
        return Response({
            'status' : 200,
            'message' : 'sucuessfull'
        })
    
    except Exception as e:
        return Response({
            'message' : 'something went to wrong',
            'error' : str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# book get path operation
@api_view(['GET'])
def get_book(request):

    try:
        book_obj = Books.objects.all()
        serializer = BookSerializer(book_obj, many = True)
        return Response({
            'status' : status.HTTP_200_OK,
            'payload' : serializer.data
        })

    except Exception as e:
        return Response({
            'message' : 'something went to wrong',
            'error' : str(e)
        }, status= status.HTTP_400_BAD_REQUEST)
    


# book post path operation
@api_view(['POST'])
def create_book(request):
    try:
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'message' : 'please enter valid data',
                'error ': serializer.errors
            })
        
        serializer.save()
        return Response({
            'status' : 200,
            'message' : 'sucuessfull'
        })
    
    except Exception as e:
        return Response({
            'message' : 'something went to wrong',
            'error' : str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
