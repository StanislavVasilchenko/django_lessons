from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {"last_name": "Vasilchenko", "first_name": "Stanislav"},
            {"last_name": "Vasilchenko", "first_name": "Olga"},
            {"last_name": "Vasilchenko", "first_name": "Kira"},
            {"last_name": "Vasilchenko", "first_name": "Roman"},
            {"last_name": "Smokvin", "first_name": "Aleksandr"},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        student_for_create = []
        for student_item in student_list:
            student_for_create.append(Student(**student_item))

        Student.objects.bulk_create(student_for_create)
