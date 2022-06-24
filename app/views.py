from django.shortcuts import render

# Create your views here.
def hai(request):
    #d={'name':0}
    d={'a':10,'b':30,'c':50}
    return render(request,'hai.html',context=d)

def loop(request):
    d={'name':'shashi'}
    return render(request,'loop.html',context=d)
