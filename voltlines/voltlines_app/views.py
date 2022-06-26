from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Passenger, PassengerTrips
from .serializers import PassengerSerializer, PassengerTripsSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

# from django.urls import path
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Voltlines API')

# urlpatterns = [
# 	path('', schema_view, name='home'),
# ]


# class ListVoltlinesAPIView(ListAPIView):
#     """This endpoint list all of the available todos from the database"""
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer

# class CreateVoltlinesAPIView(CreateAPIView):
#     """This endpoint allows for creation of a todo"""
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer

# class UpdateVoltlinesAPIView(UpdateAPIView):
#     """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer

# class DeleteVoltlinesAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific Todo from the database"""
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer



@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)



@api_view(['POST'])
def add_items(request):
	passenger = PassengerSerializer(data=request.data)

	# validating for already existing data
	if Passenger.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if passenger.is_valid():
		passenger.save()
		trip = PassengerTripsSerializer(data=PassengerTrips({"passenger": passenger.data["name"], "total_distance": 0}))
		if trip.is_valid():
			trip.save()
		return Response(passenger.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_trip(request):
	trip = PassengerTripsSerializer(data=request.data)

	# validating for already existing data
	if PassengerTrips.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if trip.is_valid():
		trip.save()
		return Response(trip.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
	
	# checking for the parameters from the URL
	if request.query_params:
		passenger = Passenger.objects.filter(**request.query_params.dict())
		serializer = PassengerSerializer(passenger, many=True)
	else:
		passenger = Passenger.objects.all()
		serializer = PassengerSerializer(passenger, many=True)

	# if there is something in items else raise error
	if passenger:
		# data = PassengerSerializer(passenger)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_trips(request):
	# checking for the parameters from the URL
	if request.query_params:
		trip = PassengerTrips.objects.filter(**request.query_params.dict())
		serializer = PassengerTripsSerializer(trip, many=True)
	else:
		trip = PassengerTrips.objects.filter(**request.query_params.dict())
		serializer = PassengerTripsSerializer(trip, many=True)

	# if there is something in items else raise error
	if trip:
		# data = PassengerSerializer(passenger)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):

	# if request.query_params:
	# 	passenger = Passenger.objects.filter(**request.query_params.dict())

	passenger = Passenger.objects.get(pk=pk)
	data = PassengerSerializer(instance=passenger, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_trips(request, pk):

	# if request.query_params:
	# 	passenger = Passenger.objects.filter(**request.query_params.dict())

	trip = PassengerTrips.objects.get(pk=pk)
	data = PassengerTripsSerializer(instance=trip, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	# delete both passenger and its trips
	item = get_object_or_404(Passenger, pk=pk)
	item.delete()
	item = get_object_or_404(PassengerTrips, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
