from django.core.management.base import BaseCommand, CommandError
from daterapp.models import PastDate 
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete objects older than 10 days'

    def handle(self, *args, **options):
        # dates = PastDate.objects.filter(created_at=datetime.now()-timedelta(days=10)).delete()
        dates = PastDate.objects.filter(created_at = timezone.now()-timezone.timedelta(days=1))
        # dates = PastDate.objects.all()
        print(dates)
        
        self.stdout.write('Deleted objects older than 1 days')