from django.http import HttpResponse

def About_AIDS(request):
    return HttpResponse(
        "<h1>Artificial Intelligence and Data Science (AI & DS) Branch</h1>"
        "<p>The Department of Artificial Intelligence and Data Science focuses on modern computational technologies, "
        "including Machine Learning, Deep Learning, Big Data Analytics, Natural Language Processing, "
        "and Computer Vision. It equips students to build intelligent systems and data-driven solutions.</p>"
    )
