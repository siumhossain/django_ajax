from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin



# Create your views here.

def homepage(request):
    return HttpResponse('hello homepage')

class LeadListView(ListView):
    model = Lead
    context_object_name = 'leads'

class LeadDetailView(DetailView):
    context_object_name = 'lead'
    queryset = Lead.objects.all()

class LeadCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'is_staff'
    template_name = 'lead/lead_create.html'
    form_class = LeadForm
    def handle_no_permission(self):
        return redirect('/no/')
    def get_success_url(self):
        return reverse("lead:lead")
class LeadUpdateView(UpdateView):
    template_name = 'lead/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadForm
    def get_success_url(self):
        return reverse("lead:lead")

class No(TemplateView):
    template_name ='no.html'

class LeadDeleteView(DeleteView):
    template_name = 'lead/lead_delete.html'
    queryset = Lead.objects.all()
    form_class = LeadForm
    def get_success_url(self):
        return reverse("lead:lead")


# search value in request
def search_results(request):
    if request.is_ajax():
        res = None
        people = request.POST.get('people')
        #print('people')
        qs = Lead.objects.filter(first_name__icontains=people)
        #print(qs)
        if len(people)>0 and len(qs)>0:
            data = []
            for pos in qs:
                item = {
                    'pk':pos.pk,
                    'first_name':pos.first_name
                }
                data.append(item)
            res = data
        else:
            res = 'not found'
        return JsonResponse({'data':res})
    return JsonResponse({})


def lead(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,'lead_home.html',context)


def lead_details(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {'lead': lead }
    return render(request,'lead_details.html',context)

def lead_create(request):
    form = LeadForm()
    data =[]
    if request.is_ajax():
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request,'lead_create.html',context)

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/lead')
    context = {
        'form':form,
        'lead':lead
    }
    return render(request,'lead_create.html',context)
def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/lead')
    


