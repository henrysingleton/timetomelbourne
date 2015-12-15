from django.core.management.base import BaseCommand, CommandError
from pttime.route_loader import RouteLoader


class Command(BaseCommand):
    help = 'Loads route data for the next available locations that require it. '

    def add_arguments(self, parser):
        parser.add_argument('limit', type=int)

    def handle(self, *args, **options):
        loader = RouteLoader()
        loader.load_standard_routes(limit=options['limit'])
        self.stdout.write('Route loading complete')