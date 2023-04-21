from django.shortcuts import render

posts= [
    {
        'author':'sailesh',
        'title':'django-1',
        'content':'first-post-content',
        'date_posted':'april 22, 2023'
    },
    {
        'author':'sarvesh',
        'title':'django-2',
        'content':'second-post-content',
        'date_posted':'april 23, 2023'
    },
    {
        'author':'sanush',
        'title':'django-3',
        'content':'third-post-content',
        'date_posted':'april 22, 2023'
    }
]
# Create your views here.
def home(request):
    context={
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})