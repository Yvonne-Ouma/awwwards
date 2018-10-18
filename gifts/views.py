from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,ProjectForm,ProfileForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer





# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):

    project = Project.objects.all()
    profile = Profile.objects.all()
    return render(request, 'index.html',{"project":project, "profile":profile})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# @login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user = request.user
#     profile = Profile.objects.get(user=current_user)
#     user = User.objects.get(username=request.user)
#     return render(request, 'profile/profile.html', {'user': current_user, "profile":profile})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    form = ProfileForm()
    user = request.user
    if request.user.is_authenticated():
        if request.method == "POST":
            try:
                profile = user.profile
                form = ProfileForm(instance=profile)
                form = ProfileForm(
                    request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    update = form.save(commit=False)
                    update.user = user
                    update.save()
            except:
                form = ProfileForm(request.POST, request.FILES)
                print(form.is_valid())
                if form.is_valid():
                    form.save()
                    profile = Profile.objects.last()
                    print(profile)
                    profile.user = user
                    profile.save()
            return redirect('welcome')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form': form, 'user': user})    

@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('welcome')

    else:
        form = ProjectForm()
        return render(request, 'project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get('search')
        projects = Project.filter_by_search_term(search_term)
        print(projects)
        message = f"{search_term}"

    else:
        message = "No searched project"
    #     return render(request, 'search.html', {"message": message})
    return render(request, 'search.html', {"message": message, "projects": projects})   

def each_project(request,id):
    project = get_object_or_404(Project, pk=id)
    return (request, 'each_project.html')

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers =ProjectSerializer(all_project, many=True)
        return Response(serializers.data)





    
