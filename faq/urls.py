# faq/urls.py
from django.urls import path
# from .views import faq_list, faq_detail, faq_create
from .views import faq_create

urlpatterns = [
    # path('list/', faq_list, name='faq_list'),
    # path('detail/<int:faq_id>/', faq_detail, name='faq_detail'),
    path('create/<int:index>', faq_create, name='faq_create'),
]
