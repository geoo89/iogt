from django.urls import path
from .views import download_xlsxfile, upload_xlsxfile

# TODO: For PO files, these are the absolute paths.
# Here, however, the absolute path will be translation/admin/localize/...
# which is inconsistent.
urlpatterns = [
    path('admin/localize/translate/<int:translation_id>/xlsxfile/download/', download_xlsxfile, name='download_xlsxfile'),
    path('admin/localize/translate/<int:translation_id>/xlsxfile/upload/', upload_xlsxfile, name='upload_xlsxfile'),
]
