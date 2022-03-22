# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json

from orders.models import Transactions, Order


class BackGroundTasks(APIView):
    def post(self, request):
        token = request.POST["token"]
        if token == "HiAdmin":
            transactions = Transactions.objects.all()
            counter = 0
            for transaction in transactions:
                if transaction.get_status_display() == "Waiting":
                    resp = requests.post("https://api.idpay.ir/v1.1/payment/inquiry",
                                         headers={'Content-Type': 'application/json',
                                                  "X-API-KEY": 'c377d98e-0c65-4696-9d7f-db122b15b5e0',
                                                  'X-SANDBOX': "1"},
                                         data=json.dumps(
                                             {"order_id": transaction.order.id, "id": f"{transaction.transactionId}"})
                                         )
                    verification = resp.json()
                    verification_status = int(verification["status"])
                    if (verification_status == 100) or (verification_status == 101) or (verification_status == 1):
                        trans_order = Order.objects.get(id=transaction.order.id)
                        transaction.status = 2
                        trans_order.status = 2
                        trans_order.save()
                        transaction.save()
                        counter += 1
            return Response(f"{counter} Transaction Accepted !")
        else:
            return Response("Access Denied !")
