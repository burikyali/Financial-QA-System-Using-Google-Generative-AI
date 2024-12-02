from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.process_pdfs, name="process_pdfs"),
    path("ask/", views.ask_question, name="ask_question"),
    path("features/", views.features, name="features"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
    path("feedback/submit/", views.submit_feedback, name="submit_feedback"),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
