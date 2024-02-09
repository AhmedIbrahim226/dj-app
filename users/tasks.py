from celery import shared_task



@shared_task(bind=True)
def task1(self, x, y):
    print(self.request.id)
    return x + y

