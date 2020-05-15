from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .forms import UserCreationForm
from .models import User
from django.core.mail import send_mail

import time
from django.shortcuts import redirect
from .models import UserManager

from django.contrib.auth.decorators import login_required

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']

        code = 'qwe67ghfyewkl'
        user = authenticate(email=email, password=password)
     
        
        send_mail(
            "код подтверждения",
            f"Перейди по ссылке для подверждения:)\nlocalhost:8000/accounts/reg/?code={code}",
            "marysadness160@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
        time.sleep(10)
        #code = self.request.headerssuper(RegisterView, self).form_valid(form)
        
        return ValureError
    

@login_required
def reg(request):
    answer = "Ошибка"
    code = request.GET.get('code', '')

    code_begin = 'qwe67ghfyewkl'
    if code == code_begin:

        answer = "Добро пожаловать!"
        request.user.is_active = True

        request.user.save()
        login(request, request.user)

        return redirect(f"/notes/?answer={answer}")

    else:

        return redirect(f"/accounts/login/?answer={answer}")
