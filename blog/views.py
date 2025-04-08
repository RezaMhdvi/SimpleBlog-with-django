from django.shortcuts import render
from datetime import date

all_posts=[
    {
        'slug':'learning-django',
        'title':'django course',
        'author':'Reza Mahdavi',
        'image':'django.png',
        'date':date(2021,4,5),
        'short_description':'this is django course in website',
        'content':"""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug':'learning-python',
        'title':'python course',
        'author':'Reza Mahdavi',
        'image':'python.png',
        'date':date(2021,4,3),
        'short_description':'this is django course in website',
        'content':"""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est
        """
    },
    {
        'slug':'learning-python',
        'title':'python course',
        'author':'Reza Mahdavi',
        'image':'python.png',
        'date':date(2021,6,3),
        'short_description':'this is django course in website',
        'content':"""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
    {
        'slug':'learning-machine-learning',
        'title':'ml course',
        'author':'Reza Mahdavi',
        'image':'ml.png',
        'date':date(2021,4,1),
        'short_description':'this is django course in website',
        'content':"""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts= sorted(all_posts, key=get_date)
    latest_posts=sorted_posts[-2:]
    return render(request, 'blog/index.html',{
        'latest_posts':latest_posts
    })


def posts(request):
    context={
        'all_posts':all_posts
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request,slug):
    post=next(post for post in all_posts if post['slug'] == slug)
    return  render(request, 'blog/post-detail.html',{
        'post':post
    })
