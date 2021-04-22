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

@csrf_exempt
def update(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        if not "id" in received_json_data:
            return HttpResponse("book id please.", status=400)
        id = received_json_data["id"]
        book = Book.objects.filter(id=id)[0]
        if "title" in received_json_data:
            book.title = received_json_data["title"]
        if "category" in received_json_data:
            book.category = int(received_json_data["category"])
        book.save()
        response_data = {"id":book.id,"title":book.title,"category":book.category}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)

    else:
        return HttpResponse(status=401,content="method not allowed!")

@csrf_exempt
def delete(request):
    if request.method != 'POST':
        return HttpResponse(status=401, content="method not allowed!")
    received_json_data = json.loads(request.body)
    if not "id" in received_json_data:
        return HttpResponse("book id please.", status=400)
    book = Book.objects.filter(id=received_json_data["id"])
    if len(book) == 0:
        return HttpResponse(status=401, content="the book does not exists!")
    book = book[0]
    id = book.id
    book.delete()
    # print(123)
    return HttpResponse("book "+ str(id)+ " delete successfully!", status=200)


def read(request):
    if request.method != 'GET':
        return HttpResponse(status=401, content="method not allowed!")
    print(id)
    title = ""
    received_json_data = json.loads(request.body)
    books = Book.objects.all()
    if "title" in received_json_data:
        books = books.filter(title__icontains=received_json_data["title"])
    if "category" in received_json_data:
        books = books.filter(category = int(received_json_data["category"]))
    response_data = {}
    for book in books:
        response_data[book.id]={"title":book.title,"category":book.category}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)

