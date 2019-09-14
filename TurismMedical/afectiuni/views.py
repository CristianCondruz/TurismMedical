from django.shortcuts import render
from .forms import AdaugareAfectiuniForm, StatiuniBalneareForm
from .models import AfectiuniStatiuni, StatiuniBalneare, Afectiuni, BazaTratament, Cazare, Proceduri
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

def adaugare_afectiuni_view(request):

    if request.method == 'POST':
        adaugare_afectiuni_form = AdaugareAfectiuniForm(request.POST)
        statiuni_balneare_form = StatiuniBalneareForm(request.POST)

        if adaugare_afectiuni_form.is_valid() and statiuni_balneare_form.is_valid():
            afectiune = adaugare_afectiuni_form.save(commit=False)
            afectiune.clasificare =  adaugare_afectiuni_form.cleaned_data.get('clasificare')
            afectiune.DecontatCNAS =  adaugare_afectiuni_form.cleaned_data.get('DecontatCNAS')
            afectiune.save()
            statiune = StatiuniBalneare.objects.get(nume= statiuni_balneare_form.cleaned_data.get('nume'), judet = statiuni_balneare_form.cleaned_data.get('judet'))
            as1 = AfectiuniStatiuni(afectiune = afectiune, statiune = statiune)
            as1.save()

    else:
        adaugare_afectiuni_form = AdaugareAfectiuniForm()
        statiuni_balneare_form = StatiuniBalneareForm()
    return render(request, 'adaugare_afectiuni.html',{
			'adaugare_afectiuni_form': adaugare_afectiuni_form,
            'statiuni_balneare_form' : statiuni_balneare_form
		})

class ListaAfectiuniView(ListView):

    model = Afectiuni
    template_name = 'afectiuni_list.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

def detalii_afectiune(request,pk):

    if request.method == 'GET':
        afectiune = Afectiuni.objects.get(pk=pk)
        as1 = AfectiuniStatiuni.objects.get(afectiune= afectiune.pk)
        statiune = as1.statiune.nume
        statiune_pk = as1.statiune.pk
        print(statiune_pk)
        judet = as1.statiune.judet
        proceduri_query = as1.statiune.bazatratament_set.all()
        cazare_query = as1.statiune.cazare_set.all()
        proceduri = []
        cazare = {}
        for obj in proceduri_query:
            proceduri.append(obj.procedura)
        for obj in cazare_query:
            cazare.update({'nume':obj.nume})
            cazare.update({'rating':obj.rating})
            cazare.update({'website':obj.website})
    return render(request, 'afectiuni_detail.html',{'object':afectiune,
    'proceduri': proceduri,
    'statiune':statiune,
    'judet': judet,
    'cazare_query':cazare_query,
    'statiune_pk': statiune_pk}
    )

def cazare_view(request, pk):
    if request.method == 'GET':
        statiune = StatiuniBalneare.objects.get(pk=pk)
        print(statiune)
        cazare_query = statiune.cazare_set.all()
    return render(request,'cazare_detail.html',{'cazare_query':cazare_query})

class ListaProceduriView(ListView):

    model = Proceduri
    template_name = 'proceduri_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def addRecordsProceduri():
    with open('/home/cristi/DjangoProjects/TurismMedical/proceduri.txt', encoding = "ISO-8859-1") as f:
        for line in f:
            new_entry = Afectiuni(clasificare=line)
            new_entry.save()
