from django.shortcuts import render
from django.views import View


class ApplyViews(View):
    def get(self, request):

        return render(request, '')
