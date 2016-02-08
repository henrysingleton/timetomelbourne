from __future__ import absolute_import
from .route_loader import RouteLoader
from celery import shared_task
import random
import time


@shared_task
def load_route():
    loader = RouteLoader()
    loader.load_standard_routes(1)
    # Wait some time before running the next one, between 1 and 3 minutes (15 second increments)
    #next_delay = random.randrange(60, 60*3, 15)
    #time.sleep(next_delay)

