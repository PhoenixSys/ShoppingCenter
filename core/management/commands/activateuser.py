from django.core.management import BaseCommand

from core.models import User


class Command(BaseCommand):
    help = "Change User Activation"

    def add_arguments(self, parser):
        parser.add_argument("-u", "--username", type=str)

    def handle(self, *args, **options):
        username = options["username"]
        user_obj = User.objects.get(username=username)
        print("Before", user_obj.is_active)
        user_obj.is_active = True
        user_obj.save()
        print("After", user_obj.is_active)
# 09142520209
