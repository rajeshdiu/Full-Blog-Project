from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from myApp.models import *
from django.db.models import Q 

def signupPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        age = request.POST['age']
        Contact_No = request.POST['Contact_No']
        email = request.POST['email']
        confirm_password = request.POST['confirm-password']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        user_type = request.POST.get('user_type')

        if password == confirm_password:
            if Custom_user.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('signupPage')
            elif Custom_user.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return redirect('signupPage')
            else:
                user = Custom_user.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Contact_No=Contact_No,
                Age=age
                )
                
                if user_type=='viewers':
                    viewersProfileModel.objects.create(user=user)
                    
                elif user_type=='blooger':
                    BloggerProfileModel.objects.create(user=user)
                    
                
                return redirect("signInPage")
        else:
            return redirect('signupPage')

    return render(request, 'signupPage.html')


def signInPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Custom_user.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('homePage') 
            else:
                messages.error(request, 'Invalid credentials, please try again.')
                return redirect('signInPage')

        except Custom_user.DoesNotExist:
            messages.error(request, 'No user with this email exists.')
            return redirect('signInPage')

    return render(request, 'signInPage.html')


def logoutPage(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('signInPage')

@login_required
def homePage(request):
    
    return render(request,"homePage.html")


def addBlogPage(request):
    
    current_user=request.user
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        
        return redirect("createdBlogBy")
        
    
    return render(request,"addBlogPage.html")


def createdBlogBy(request):
    
    current_user=request.user
    
    blog=BlogPostModel.objects.filter(user=current_user)
    
    context={
        'blog':blog
    }
    
    
    return render(request,"createdBlogBy.html",context)


def ProfilePage(request):
    
    
    blogger=BloggerProfileModel.objects.all()
    viewers=viewersProfileModel.objects.all()
    
    context={
        'blogger':blogger,
        'viewers':viewers
    }
    
    return render(request,"ProfilePage.html",context)


def editBlog(request,blog_id):
    
    current_user=request.user
    
    
    blog=BlogPostModel.objects.get(id=blog_id)
    
    context={
            'blog':blog
        }
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            id=blog_id,
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        return redirect("createdBlogBy")
    
    return render(request,"editBlog.html",context)

def deleteBlog(request,blog_id):
    
    
    blog=BlogPostModel.objects.get(id=blog_id).delete()
    
    return redirect("createdBlogBy")


def AllBlogPost(request):
    
    blog=BlogPostModel.objects.all()
    
    context={
        'blog':blog
    }
    
    return render(request,"AllBlogPost.html",context)

def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        try:
            viewersprofile = viewersProfileModel.objects.get(user=current_user)
            
            viewersprofile.Bio = request.POST.get('bio', viewersprofile.Bio)
            viewersprofile.Gender = request.POST.get('gender', viewersprofile.Gender)
            viewersprofile.Profile_Pic = request.FILES['profile_pic']
            
            viewersprofile.save()

        except viewersProfileModel.DoesNotExist:
            
            viewersprofile = None  

        try:
            
            bloggerprofile = BloggerProfileModel.objects.get(user=current_user)
            bloggerprofile.Bio = request.POST.get('bio', bloggerprofile.Bio)
            bloggerprofile.Gender = request.POST.get('gender', bloggerprofile.Gender)
            bloggerprofile.Profile_Pic = request.FILES['profile_pic']
            
            bloggerprofile.save()

        except BloggerProfileModel.DoesNotExist:
            bloggerprofile = None 

        current_user.username = request.POST.get('username', current_user.username)
        current_user.email = request.POST.get('email', current_user.email)
        current_user.first_name = request.POST.get('first_name', current_user.first_name)
        current_user.last_name = request.POST.get('last_name', current_user.last_name)
        current_user.save() 
        
        return redirect("ProfilePage")

    return render(request, "edit_profile.html")



def search_blog(request):
    
    query = request.GET.get('query')
    
    if query:
        
        blog = BlogPostModel.objects.filter(Q(BlogTitle__icontains=query) 
                                       |Q(Category__icontains=query) 
                                       |Q(BlogBody__icontains=query) 
                                       |Q(user__username__icontains=query)
                                       )
    
    else:
        blog = BlogPostModel.objects.none()
        
    context={
        'blog':blog,
        'query':query
    }
    
    return render(request,"search_blog.html",context)

    
   