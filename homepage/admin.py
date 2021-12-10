from .models import contestants_of_one_vs_one, contestants_of_four_producer, contestants_of_eight_producer
from django.contrib import admin

# Register your models here.
admin.site.register(contestants_of_one_vs_one)
admin.site.register(contestants_of_four_producer)
admin.site.register(contestants_of_eight_producer)
