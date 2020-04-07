from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from App.models import Periods


class Test(APIView):
    def get(self, request):
        print(request.META)
        ip = self.request.query_params.get('server')
        return Response({"My ip": ip,
                         })


class Data(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data_dict = {}
        all_periods = Periods.objects.values_list("period_finish").all()

        for i in all_periods:
            key = data_dict.setdefault(i[0].year)
            if key is None:
                data_dict[i[0].year] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            data_dict[i[0].year][i[0].month - 1] += 1

        return Response(data_dict)