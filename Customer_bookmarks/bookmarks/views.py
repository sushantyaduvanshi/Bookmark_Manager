from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Customer, Bookmarks, customer_bookmark
from django.db.models import Q
from datetime import date

# Create your views here.

def index(request):
    # Simple Index Page for the Application
    return HttpResponse('<h3>Welcome to Bookmarks Manager...!!!</h3>')

@api_view(['GET','POST'])
@csrf_exempt
def create_bookmark(request):
    # take customer's and bookmark's information in request to create entries in the database

    # following are POST request body parameters for creating customer database table entry
    cu_name = request.POST.get('customer_name')
    cu_age = request.POST.get('customer_age')
    cu_lat = request.POST.get('customer_latitude')
    cu_lng = request.POST.get('customer_longitude')

    # following are POST request body parameters for creating bookmark database table entry
    bm_title = request.POST.get('bookmark_title')
    bm_url =  request.POST.get('bookmark_url')
    bm_source = request.POST.get('bookmark_source_name')
    
    cu = Customer.objects.create(name=cu_name, age=cu_age, lat=cu_lat, lng=cu_lng)  # creating Customer model's entry
    
    bm = Bookmarks.objects.create(title=bm_title, url=bm_url, source_name=bm_source)    # creating Bookmars model's entry

    cu_bm = customer_bookmark.objects.create(customer=cu, bookmark=bm)      # creating customer_bookmark model's entry

    return Response({
        "Status": "Bookmark Successfully saved.",
        "Customer": str(cu),
        "Bookmark": str(bm)
    })


@api_view(['GET','POST'])
@csrf_exempt
def browse_bookmark(request):
    # Input => (date_range, title_contains, sort_by)
    # e.g.
    # date_range = YYYY-MM-DD/YYYY-MM-DD, title_contains = 'jungle', sort_by = customer_id
    # Return data from Customer and Bookmark table in database
    # From Customer table => (customer_id, lat, lng)
    # From Bookmark table => (source_name, date, title)

    date_range = request.POST.get('date_range')
    title_contains = request.POST.get('title_contains')
    sort_by = request.POST.get('sort_by')

    # getting date (from_date and to_date) object from date_range input
    from_date = date_range.split('/')[0]
    from_yr = int(from_date.split('-')[0])
    from_mn = int(from_date.split('-')[1])
    from_day = int(from_date.split('-')[2])
    from_date = date(from_yr, from_mn, from_day)

    to_date = date_range.split('/')[1]
    to_yr = int(to_date.split('-')[0])
    to_mn = int(to_date.split('-')[1])
    to_day = int(to_date.split('-')[2])
    to_date = date(to_yr, to_mn, to_day)

    # making db query
    bm = Bookmarks.objects.filter(
        Q( title__contains=title_contains ),      # filter objects that contain given pattern in title
        Q( date__gte=from_date ) & Q( date__lte=to_date )       # filter objects by : from_date <= date <= to_date
        )

    print(bm)

    bm = bm.order_by(sort_by)   # finally sort the result by db tabel field given in sort_by parameter of POST request

    # Creating JSON response to api
    return Response(
        { i:{
            "Customers": [
            {
            "Customer_id": cu.id,
            "Latitude": cu.lat,
            "Longitude": cu.lng 
            } for cu in bm[i].customer.all() ],
            "Source_name": bm[i].source_name,
            "Date": bm[i].date,
            "Title": bm[i].title
        } for i in range(len(bm)) }
    )