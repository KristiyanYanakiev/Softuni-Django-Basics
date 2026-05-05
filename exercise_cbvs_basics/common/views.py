from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View


# Create your views here.
class BasicView(View):
    def get(self, request: HttpRequest):
        return HttpResponse('Welcome to Traveler Management')

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Post was called")

