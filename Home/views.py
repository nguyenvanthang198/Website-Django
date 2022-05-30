from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Create your views here.
from .forms import LoginForm, SignUpForm
from .models import *

def IndexView(request):
    context = {}
    all_menus = Menu.objects.filter(parent_menu=None).order_by('parent_menu', 'order')
    context['all_menus'] = all_menus

    all_sub_menus = Menu.objects.filter(~Q(parent_menu=None)).order_by('parent_menu', 'order')
    context['all_sub_menus'] = all_sub_menus

    template = loader.get_template(str('Home/index.html'))
    return HttpResponse(template.render(context, request))

@csrf_exempt
def ContactView(request):
    context = {}
    all_menus = Menu.objects.filter(parent_menu=None).order_by('parent_menu', 'order')
    context['all_menus'] = all_menus

    all_sub_menus = Menu.objects.filter(~Q(parent_menu=None)).order_by('parent_menu', 'order')
    context['all_sub_menus'] = all_sub_menus

    print(request)
    if request.POST:
        print(request.POST)

        content = request.POST['test-input']
        new_menu = Menu.objects.create(name=content,
                                       title=content)
    template = loader.get_template(str('Home/index.html'))
    return HttpResponse(template.render(context, request))


def LoginView(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    u_profile = username.objects.filter(user=user).first()
                    if u_profile is not None:
                        u_profile.last_login_at = djnow()
                        u_profile.save()
                except Exception as xx:
                    print("[LoginView] Exception: %s" % str(xx))
                return redirect("/")
                # check type of user direct
            else:
                msg = '<b>Tên tài khoản</b> hoặc <b>Mật khẩu</b> không đúng!'
        else:
            msg = 'Thông tin không hợp lệ'

    return render(request, "Home/login.html", {"form": form, "msg": msg})



def RegistersView(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Đã thêm mới tài khoản - hãy <a href="/login">Đăng nhập</a>.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Thông tin không hợp lệ'
    else:
        form = SignUpForm()

    return render(request, "Home/registers.html", {"form": form, "msg": msg, "success": success})




def logout_view(request):
    logout(request)
    return redirect('/')