import csv, io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from django.http import HttpResponse, Http404
import datetime
from .form import empregadoForm, ProfileForm, pontForm
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
#pdf
from django.views.generic import View
from django.utils import timezone
from .pdf import Render

@login_required
def home(request):
    return render(request, 'contas/home.html')

@staff_member_required
@login_required
def listagem (request):
    data={}
    data['transacoes'] = Profile.objects.all()
    return render (request, 'contas/listagem.html', data)

@staff_member_required
@login_required
def blabla (request):
    data = {}
    form = ProfileForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_blabla')
    data['form'] = form
    return render(request, 'contas/form.html', data)

@staff_member_required
@login_required
def update (request, pk):
    data= {}
    Empregado = empregado.objects.get(pk=pk)
    form = empregadoForm(request.POST or None, instance=Empregado)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['Empregado'] = Empregado
    return render(request, 'contas/form.html',data)

@staff_member_required
@login_required
def delete (request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.delete()
    return redirect('url_listagem')

@staff_member_required
@login_required
def individual (request, pk):
    data = {}
    profile = Profile.objects.get(pk=pk)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['profile'] = profile
    return render(request, 'contas/individual.html', data)

@staff_member_required
@login_required
def diretoria (request):
    return render(request, 'contas/diretoria.html')

def perfil (request):
    data = {}
    Perfil = Profile.objects.get
    form = ProfileForm(request.POST or None, request.FILES or None, instance=Profile)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['Perfil'] = Perfil
    return render(request, 'contas/perfil.html', data)

@permission_required('admin.can_add_log_entry')
def upload (request):
    template = 'upload.html'
    prompt = {
        'order': 'Order of the CSV should be ID_func, ID_atv, Data '
    }

    if request.method == 'GET':
        return render(request, template, prompt)
    csv_file = request.FILES ['files']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next (io_string)
    for column in csv.reader(io_string, delimiter= ';', quotechar="|"):
        _, created = Nutri.objects.update_or_create(
            numIng = column[0],
            nomeIng = column [1],
            umidade = column [2],
            energiaKCal =column[3],
            energiaKJ =column[4],
            proteina=column[5],
            lipideos=column[6],
            colesterol=column[7],
            carboidrato=column[8],
            fibraAlimentar=column[9],
            cinzas=column[10],
            calcio=column[11],
            magnesio=column[12],
            manganes=column[13],
            fosforo=column[14],
            ferro=column[15],
            sodio=column[16],
            potassio=column[17],
            cobre=column[18],
            zinco=column[19],
            retinol=column[20],
            RE=column[21],
            RAE=column[22],
            tiamina=column[23],
            riboflavina=column[24],
            piridoxina=column[25],
            niacina=column[26],
            vitaminaC=column[27],
            Q1=column[28],
            DS1=column[29],
            DZ1=column[30],
            V1=column[31],
            DZDNS=column[32],
            DZTNT=column[33],
            V4=column[34],
            V5=column[35],
            VD5=column[36],
            VD6=column[37],
            DZ1t=column[38],
            DZ2t=column[39]
        )
    context = {}
    return render (request, template, context)
#-------------------------------------------------------------------------------
class Pdf(View):

    def get(request, pk):
        today = timezone.now()
        data={}
        data['profile'] = Profile.objects.all()
        return Render.render('pdf.html', data)

def pont(request):
    data = {}
    form = pontForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('url_pont')
    data['form'] = form
    return render(request, 'contas/pontuacao.html', data)

def pont2(request):
        if request.method == 'POST':
            form = pontForm(request.POST or None)
        valor = request.POST.get[ColdCall]
        if valor == True:
            form.pCC = 20
            form.save

        return render(request, 'contas/pont2.html', {'form': form})