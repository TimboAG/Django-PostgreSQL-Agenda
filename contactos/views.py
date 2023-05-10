from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def formulario(request):
    return render(request, "formulario.html")


def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        email = request.POST["txtEmail"]
        mensaje = request.POST["txtMensaje"] + " \nEmail: " + email
        email_desde = settings.EMAIL_HOST_USER
        email_para = [email_desde]
        send_mail(asunto, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "contacto_exitoso.html")
    return render(request, "formulario.html")
