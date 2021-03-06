from django.shortcuts import render
from hashlib import md5
from datetime import datetime
from .models import User
from django.http import JsonResponse
from django.shortcuts import  redirect

data = dict()


def get_user(request):
    global data
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    data['user'] = user


def signup(request):
    global data
    get_user(request)
    """ Форма регистрации пользователей"""
    if request.method == 'GET':
        return render(request, 'account/signup.html',context=data)
    elif request.method == 'POST':
        # Извлечение данных:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        #data =dict()
        data['report'] = 'Отчет по рез'

        # Проверка совпадения паролей:
        if pass1 != pass2:
            data['report'] ='Пароли не совпадают!'
        else:
            #Хеширование пароля:
            _byte = pass1.encode()
            _hash = md5(_byte)
            passw = _hash.hexdigest()
            # Определение времени регистрации:
            now = datetime.now()
            regdate = datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
            status = 'norm'

            #Сохранение данных в базе:
            new_user = User()
            new_user.login = login
            new_user.passw = passw
            new_user.email = email
            new_user.regdate = regdate
            new_user.status = status
            new_user.save()

            #
            data['report'] = 'Регистрация успешно завершена!'



            #   Контроль данных на страницу
            """
            data['login'] = login
            data['pass1'] = pass1
            data['pass2'] = pass2
            data['email'] = email
            data['passw'] = passw
            data['regdate'] = regdate
            data['status'] = status
            """
            # Отправка данных на страницу отчета:
        return render(request,'account/signup_res.html',context=data)


def signin(request):
    global data
    get_user(request)
    if request.method == 'GET':
        return render(request, 'account/signin.html',context=data)
    elif request.method == 'POST':
        #data = dict()

        # извлечение данных
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        # контроль данных
        data['login'] = _login
        data['pass1'] = _pass1

        #Хеширование пароля:
        _byte = _pass1.encode()
        _hash = md5(_byte)
        _passw = _hash.hexdigest()

        # Проверка пользователя:
        try:
            user = User.objects.get(login=_login,passw=_passw)
            data['report'] = 'Вы успешно авторизованы'
            data['x_color'] = 'green'
            request.session['user']= _login
            return redirect('/home')
        except User.DoesNotExist as err:
            data['report'] = 'Авторизация провалена'
            data['x_color'] = 'red'
            return render(request,'account/signin_res.html',context=data)


def profile(request):
    global data
    get_user(request)
    return render(request, 'account/profile.html', context=data)


def signout(request):
    global data
    get_user(request)
    del request.session['user']
    return redirect('/home')
    #return render(request, 'home/index.html', context=data)


def ajax_reg(request):
    response = dict()
    _login = request.GET.get('login')
    try:
        user = User.objects.get(login=_login)
        response['mess'] = 'занят'
    except User.DoesNotExist as err:
        response['mess'] = 'свободен'

    return JsonResponse(response)