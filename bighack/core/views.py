from django.views import generic as views
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
from .models import *
from .forms import *

__all__ = ['home', 'apply', 'buildings']


class HomeView(views.ListView):
    template_name = 'base.html'
    queryset = Application.objects.all()
    context_object_name = 'applications'


class ApplicationFormView(views.TemplateView):
    template_name = 'app_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.building = get_object_or_404(Building, pk=request.GET.get('building'))
        return super(ApplicationFormView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'app_form': ApplicationForm(),
            'image_formset': ImageFormSet(),
        }
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        app_form = ApplicationForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        for image_form in image_formset: print(image_form.errors)
        if app_form.is_valid() and image_formset.is_valid():
            app_form.instance.building = self.building
            app = app_form.save()
            for image_form in image_formset:
                if not image_form.instance.file: continue
                image_form.instance.application = app
                image_form.save()
            messages.success(request, 'Success!')
        context = {'app_form': app_form, 'image_formset': image_formset}
        return self.render_to_response(context=context)


home = HomeView.as_view()
apply = ApplicationFormView.as_view()


def buildings(_):
    data = []
    for building in Building.objects.all():
        data.append({
            'id': building.pk,
            'address': building.address,
            'latitude': building.latitude,
            'longitude': building.longitude,
        })
    response = json.dumps(data)
    return HttpResponse(response, content_type='application/json')
