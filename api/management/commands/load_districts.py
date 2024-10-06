from django.core.management.base import BaseCommand
from api.models import District

class Command(BaseCommand):
    help = 'Load districts into the database'

    def handle(self, *args, **kwargs):
        districts_data = [
            {
                "name": "Bhojpur District",
                "headquarters": "Bhojpur",
                "area": 1463,
                "population": 300000,
                "province": 1
            },
            {
                "name": "Dhankuta District",
                "headquarters": "Dhankuta",
                "area": 1177,
                "population": 200000,
                "province": 1
            },
            {
                "name": "Ilam District",
                "headquarters": "Ilam",
                "area": 1556,
                "population": 380000,
                "province": 1
            },
            {
                "name": "Khotang District",
                "headquarters": "Diktel",
                "area": 1471,
                "population": 200000,
                "province": 1
            },
            {
                "name": "Okhaldhunga District",
                "headquarters": "Okhaldhunga",
                "area": 1071,
                "population": 120000,
                "province": 1
            },
            {
                "name": "Panchthar District",
                "headquarters": "Panchthar",
                "area": 1181,
                "population": 160000,
                "province": 1
            },
            {
                "name": "Sankhuwasabha District",
                "headquarters": "Khandbari",
                "area": 2594,
                "population": 150000,
                "province": 1
            },
            {
                "name": "Solukhumbu District",
                "headquarters": "Salleri",
                "area": 3578,
                "population": 120000,
                "province": 1
            },
            {
                "name": "Terhathum District",
                "headquarters": "Terhathum",
                "area": 1192,
                "population": 100000,
                "province": 1
            },
            {
                "name": "Udayapur District",
                "headquarters": "Udayapur",
                "area": 1855,
                "population": 250000,
                "province": 1
            }
        ]

        for district in districts_data:
            District.objects.create(**district)

        self.stdout.write(self.style.SUCCESS('Districts loaded successfully!'))

# python manage.py load_districts