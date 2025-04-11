from Django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("hello world") 