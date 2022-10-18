from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(
                request,
                'dashboard/index.html',
                 )

def robotPositionRequest(request):
    return render(
                request,
                'dashboard/index.html', # make waiting process.
    )


def topicConnectionTest(request):
    return render(
        request,
        'dashboard/topicConnectionTest.html',
    )