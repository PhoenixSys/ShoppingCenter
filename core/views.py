# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Transactions


class BackGroundTasks(APIView):
    def post(self, request):
        token = request.POST["token"]
        if token == "HiAdmin":
            transactions = Transactions.objects.all()
            for transaction in transactions:
                if transaction.get_status_display() == "Waiting":
                    print(transaction.transactionId)
            return Response("Ok")
        else:
            return Response("Access Denied !")
