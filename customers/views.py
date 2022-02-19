from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Costumers
from customers.serializer import CostumerSerializer


class CostumerManagerApi(APIView):
    def get(self, request):
        costumers_ser = CostumerSerializer(instance=Costumers.objects.all(), many=True)
        return Response(costumers_ser.data)
