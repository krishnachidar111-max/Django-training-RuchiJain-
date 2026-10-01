from django.http import HttpResponse

def Home(request):
    return HttpResponse(
        "<h1>SISTec - Sagar Institute of Science and Technology</h1>"
        "<p>SISTec is one of the premier educational institutions in Bhopal, Madhya Pradesh. "
        "It is known for its academic excellence, state-of-the-art campus infrastructure, "
        "expert faculty, and top-tier placement records across engineering, pharmacy, and management programs.</p>"
    )
