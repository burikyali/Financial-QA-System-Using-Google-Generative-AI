from django.shortcuts import render
from .utils import (
    get_pdf_text,
    get_text_chunks,
    get_vector_store,
    get_response,
)  # Import functions from utils.py
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings


@csrf_exempt
def process_pdfs(request):
    if request.method == "POST":
        pdf_files = request.FILES.getlist("pdf_files")
        if not pdf_files:
            return render(request, "index.html", {"error": "Please upload a PDF file."})

        file_urls = []
        fs = FileSystemStorage(
            location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL
        )

        # Save uploaded PDFs and get URLs
        for pdf in pdf_files:
            filename = fs.save(pdf.name, pdf)
            file_url = fs.url(filename)
            file_urls.append(file_url)

            # Process the file (optional: you can keep the processing logic if needed)
            raw_text = get_pdf_text([pdf])
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)

        return render(
            request,
            "index.html",
            {
                "file_urls": file_urls,
                "success": "PDFs processed successfully!",
            },
        )

    return render(request, "index.html")


@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        if not question:
            return render(
                request, "index.html", {"error": "Please provide a valid question."}
            )

        answer = get_response(question)
        return render(request, "index.html", {"answer": answer})

    return render(request, "index.html")


from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def features(request):
    return render(request, "features.html")


def about(request):
    return render(request, "about.html")


def feedback(request):
    return render(request, "feedback.html")


from django.shortcuts import render, redirect
from .models import Feedback


def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        message = request.POST.get("message")

        # Save feedback to the database
        Feedback.objects.create(name=name, email=email, rating=rating, message=message)

        # Show a success message
        success_message = "Thank you for your feedback!"
        return render(request, "feedback.html", {"success_message": success_message})

    return render(request, "feedback.html")
