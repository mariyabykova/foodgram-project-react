import csv

from django.apps import apps
from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404


MODELS_FIELDS = {}


class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument(
            '--app_name',
            type=str,
            help="django app name that the model is connected to"
        )

    def handle(self, *args, **options):
        file_path = options['path']
        model = apps.get_model(options['app_name'], options['model_name'])
        with open(file_path, 'rt', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                for field, value in row.items():
                    if field in MODELS_FIELDS.keys():
                        row[field] = get_object_or_404(
                            MODELS_FIELDS[field], pk=value
                        )
                model.objects.create(**row)
