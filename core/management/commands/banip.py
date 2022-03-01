from core.models import IpManagerDb

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "You Can Ban Ip With This Method"

    def add_arguments(self, parser):
        parser.add_argument("-ip", "--ip", type=str)

    def handle(self, *args, **options):
        ip = options["ip"]
        ip_obj = IpManagerDb.objects.get(ip=ip)
        print("Before", ip_obj.access)
        ip_obj.access = False
        ip_obj.save()
        print("After", ip_obj.access)
