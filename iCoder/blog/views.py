from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    # return HttpResponse('This is blogHome page. We will put our blogs here')
    return render(request,'blog/blogHome.html')

def blogPost(request,slug):
    # return HttpResponse(f'This is blogPost page : {slug}')   
    return render(request,'blog/blogPost.html') 