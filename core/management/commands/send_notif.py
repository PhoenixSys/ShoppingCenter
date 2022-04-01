from django.core.mail import send_mail
from django.core.management import BaseCommand

from core.models import User


class Command(BaseCommand):
    help = "Push Notification"

    def add_arguments(self, parser):
        parser.add_argument("-m", "--message", type=str)
        parser.add_argument("-t", "--target", type=str)

    def handle(self, *args, **options):
        target = options["target"]
        message = options["message"]
        if target == "all":
            targets = User.objects.all()
            for user in targets:
                user_email = user.email
                send_mail(
                    'Message',
                    f'Hello Dear {user.username} \n\n{message}\n\nBest Regards',
                    from_email=None,
                    recipient_list=[f"{user_email}"],
                    fail_silently=False,
                )
                print("Sent ! ", user_email)
        else:
            target = target.split(",")
            for t in target:
                user = User.objects.filter(username=t).get()
                user_email = user.email
                send_mail(
                    f'Message',
                    f'Hello Dear {user.username} \n\n{message}\n\nBest Regards',
                    from_email=None,
                    recipient_list=[f"{user_email}"],
                    fail_silently=False,
                )
                print("Sent ! ", user_email)
