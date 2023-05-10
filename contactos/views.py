from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Persona, Ciudad, Email, Telefono

# Create your views here.


def crear_persona(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        sexo = request.POST.get('sexo')
        ciudad_codigo = request.POST.get('ciudad')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        ciudad_codigo = request.POST['ciudad']
        ciudad_seleccionada = Ciudad.objects.get(codigo=ciudad_codigo)
        miCiudad = Ciudad(codigo=ciudad_seleccionada.codigo,
                          nombre=ciudad_seleccionada.nombre)
        print("esta es mi ciudad? ")
        persona = Persona(dni=dni, nombre=nombre, apellido=apellido,
                          fechaNacimiento=fecha_nacimiento, sexo=sexo, ciudad=miCiudad)
        persona.save()

        miPersonaEmail = Email(persona=persona, email=email)
        miPersonaEmail.save()

        miPersonaTelefono = Telefono(persona=persona, numero=telefono)
        miPersonaTelefono.save()

    context = {
        'persona': Persona(),
        'ciudades': Ciudad.objects.all(),
        'sexos': Persona.sexos,
    }

    return render(request, 'formregistro.html', context)


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
