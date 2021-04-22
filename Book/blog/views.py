from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime , timedelta
from .models import Book




@csrf_exempt
def create(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        print(received_json_data["title"])
        book = Book(
            title = received_json_data["title"],
            category = int(received_json_data["category"])
        )
        book.save()

        print(request)

        return HttpResponse("created successfully, book id = "+str(book.id),status= 201)
    else:
        return HttpResponse(status=401,content="method not allowed!")
