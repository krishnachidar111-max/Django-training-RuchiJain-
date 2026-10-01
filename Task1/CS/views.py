from django.http import HttpResponse

def About_about(request):
    return HttpResponse(
        "<h1>Department of Computer Science & Engineering (CS) - SISTec</h1>"
        "<p>The Computer Science and Engineering department at SISTec delivers robust foundational and practical education "
        "in software engineering, algorithms, database management, cloud computing, and cyber security. "
        "SISTec provides high-tech computing labs and dedicated training programs to prepare students for industry careers.</p>"
    )
