from celery import shared_task
from .models import Counter



@shared_task
def update_counter():
    print("inside update_counter")
    instance = Counter.objects.first()
    if not instance:
        Counter.objects.create(count=1)
    else:
        Counter.objects.filter(id=instance.id).update(count=instance.count+1)
    return True
