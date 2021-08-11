from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('product_list',views.product_list_view,name='product_list'),
    path('products/<int:pk>/',views.product_detail_view,name='product_detail'),
    path('products/<int:pk>/request_form/',views.Request_view,name='request_form'),
    path('request/<int:pk>',views.Request_Summary_view,name='request_summary'),
    path('privacy',views.privacy_view,name='privacy_policy'),
    path('terms_and_conditions',views.terms_view,name='terms_and_conditions'),
    path('cancellation_refund',views.refund_policy_view,name='cancellation_policy'),
    path('contact_us',views.contact_info_view,name='contact_info'),
    path('muses',views.Muses_view,name='muses')
]
