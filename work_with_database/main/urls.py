from django.contrib import admin
from django.urls import path

import phones.views


# class DateConverter:
#     regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
#
#     def to_python(self, value):
#         return datetime.strptime(value, '%Y-%m-%d')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', phones.views.show_catalog),
    path('catalog/<name>/', phones.views.show_product),
]
