from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import MyForm

@require_http_methods(["GET"])
def home(request):
    return render(request, 'home.html')

def myform(request):
    myformset = formset_factory(MyForm)
    if request.POST:
        formset = myformset(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data['first_input'])
            return HttpResponseRedirect(reverse('thanks'))
    else:
        formset = myformset()
    return render(request, 'myform.html', {'formset':formset})

def thanks(request):
    return render(request, 'thanks.html')
