from django.urls import path
from .views import SAPUploadView, EmissionRecordListView

urlpatterns = [
    path('upload/sap/', SAPUploadView.as_view()),
    path('records/', EmissionRecordListView.as_view()),
]