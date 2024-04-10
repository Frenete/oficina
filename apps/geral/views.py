from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import OficinaForm
from .models import Oficina

@login_required
def home(request):
    template_name = 'geral/home.html'
    context = {}
    return render(request, template_name, context)

@login_required
def nova_oficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.sucesses(request, 'Oficina cadastradada com sucesso')
            return redirect('geral:lista_oficina')
    return render()


def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user) # select * from oficina where usuario = usuario_de_sessão
    context ={
        'oficina': oficinas,
    }
    return render(request, template_name, context)
