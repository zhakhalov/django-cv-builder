from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from models import Resume
from models import Skill
from models import Experience
from models import Education
from models import Language

from forms import ResumeForm
from forms import SkillForm
from forms import ExpForm
from forms import EduForm
from forms import LangForm


#  --------------------------------------------------------------------------     

def login_view(request, onsuccess = '/resume', onfail = '/login'):
    if request.method == 'POST':
        
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        
        if user is not None:
            login(request, user)
            return redirect(onsuccess)
        else: 
            return redirect(onfail)
        
    return render(request, 'auth/login.html')
    
# --------------------------------------------------------------------------     

def logout_view(request):
    logout(request)
    return redirect('/login')

#  --------------------------------------------------------------------------     

def register_view(request, onsuccess = '/resume', onfail = '/login'):
    if request.method == 'POST':
        if not 'password' in request.POST.keys():
            return render(request, 'auth/register.html', {
                'password_err': 'Password required'
            })
        if request.POST['password'] != request.POST['confirm']:
            return render(request, 'auth/register.html', {
                'confirm_err': 'Password does not match confirmation'
            })
        elif User.objects.filter(username=request.POST['email']).count() == 0:
            user = User(username=request.POST['email'], email=request.POST['email'])
            user.set_password(request.POST['password'])
            user.save()
            resume = Resume(user = user)
            resume.save()
            return login_view(request)
        else:
            return render(request, 'auth/register.html', {
                'email_err': 'E-mail already used'
            })
    return render(request, 'auth/register.html')
    
#  --------------------------------------------------------------------------     

def index_view(request):
    return redirect('login/')

#  --------------------------------------------------------------------------     

@login_required(login_url='/login/')
def resume_view(request):
    if request.method == 'POST':
        f = ResumeForm(request.POST, instance=Resume.objects.get(user=request.user))
        if f.is_valid():
            f.save()
            return render_resume(request)
        else :
            print f.errors
            return render_resume(request)
    return render_resume(request, request.GET.get('tab'))
    
#  ---------------------------------------------------------------------------     
#                                                                       SKILLS
#  ---------------------------------------------------------------------------     

@login_required(login_url='/login/')
def skill_view(request):
    if request.method == 'POST':
        f = SkillForm(request.POST)
        if f.is_valid():
            resume = Resume.objects.get(user=request.user)
            model = f.save(commit=False)
            model.resume = resume
            model.save()
            return render_resume(request, tab='skill')
    return redirect('/resume')

#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def skill_edit_view(request, id = -1):
    if request.method == 'POST':
        f = SkillForm(request.POST, instance=Skill.objects.get(pk=id))
        if f.is_valid():
            f.save()
            return render_resume(request, tab='skill')
    elif id != -1:
        return render(request, 'edit/skill.html', {
            'form': SkillForm(instance=Skill.objects.get(pk=id)),
            'id': id
        });
    return redirect('/resume')
    
#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def skill_delete_view(request, id = -1):
    if id != -1:
        Skill.objects.get(pk=id).delete()
        return render_resume(request, tab='skill')
        
    return redirect('/resume')

#  ---------------------------------------------------------------------------     
#                                                                   EXPERIENCE
#  ---------------------------------------------------------------------------     

@login_required(login_url='/login/')
def exp_view(request):
    if request.method == 'POST':
        f = ExpForm(request.POST)
        if f.is_valid():
            resume = Resume.objects.get(user=request.user)
            model = f.save(commit=False)
            model.resume = resume
            model.save()
            return render_resume(request, tab='exp')
    return redirect('/resume')

#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def exp_edit_view(request, id = -1):
    if request.method == 'POST':
        f = ExpForm(request.POST, instance=Experience.objects.get(pk=id))
        if f.is_valid():
            f.save()
            return render_resume(request, tab='exp')
    elif id != -1:
        return render(request, 'edit/exp.html', {
            'form': ExpForm(instance=Experience.objects.get(pk=id)),
            'id': id
        });
    return redirect('/resume')
    
#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def exp_delete_view(request, id = -1):
    if id != -1:
        Experience.objects.get(pk=id).delete()
        return render_resume(request, tab='exp')
        
    return redirect('/resume')
    
#  --------------------------------------------------------------------------     
#                                                                   EDUCATION
#  --------------------------------------------------------------------------     

@login_required(login_url='/login/')
def edu_view(request):
    if request.method == 'POST':
        f = EduForm(request.POST)
        if f.is_valid():
            resume = Resume.objects.get(user=request.user)
            model = f.save(commit=False)
            model.resume = resume
            model.save()
            return render_resume(request, tab='edu')
    return redirect('/resume')

#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def edu_edit_view(request, id = -1):
    if request.method == 'POST':
        f = EduForm(request.POST, instance=Education.objects.get(pk=id))
        if f.is_valid():
            f.save()
            return render_resume(request, tab='edu')
    elif id != -1:
        return render(request, 'edit/edu.html', {
            'form': EduForm(instance=Education.objects.get(pk=id)),
            'id': id
        });
    return redirect('/resume')
    
#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def edu_delete_view(request, id = -1):
    if id != -1:
        Education.objects.get(pk=id).delete()
        return render_resume(request, tab='edu')
        
    return redirect('/resume')
    
#  --------------------------------------------------------------------------     
#                                                                   LANGUAGES
#  --------------------------------------------------------------------------     

@login_required(login_url='/login/')
def lang_view(request):
    if request.method == 'POST':
        f = LangForm(request.POST)
        if f.is_valid():
            resume = Resume.objects.get(user=request.user)
            model = f.save(commit=False)
            model.resume = resume
            model.save()
            return render_resume(request, tab='lang')
    return redirect('/resume')

#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def lang_edit_view(request, id = -1):
    if request.method == 'POST':
        f = LangForm(request.POST, instance=Language.objects.get(pk=id))
        if f.is_valid():
            f.save()
            return render_resume(request, tab='lang')
    elif id != -1:
        return render(request, 'edit/lang.html', {
            'form': LangForm(instance=Language.objects.get(pk=id)),
            'id': id
        });
    return redirect('/resume')
    
#  --------------------------------------------------------------------------       
  
@login_required(login_url='/login/')
def lang_delete_view(request, id = -1):
    if id != -1:
        Language.objects.get(pk=id).delete()
        return render_resume(request, tab='lang')
        
    return redirect('/')

#  --------------------------------------------------------------------------

def render_resume(request, tab='general'):
    resume = Resume.objects.get(user=request.user)
    return render(request, 'resume.html', {
        'general_form': ResumeForm(instance=resume),
        'skill_form': SkillForm(),
        'experience_form': ExpForm(),
        'education_form': EduForm(),
        'language_form': LangForm(),
        'skills': Skill.objects.filter(resume=resume),
        'experience': Experience.objects.filter(resume=resume),
        'education': Education.objects.filter(resume=resume),
        'languages': Language.objects.filter(resume=resume),
        'tab':tab
    })
    