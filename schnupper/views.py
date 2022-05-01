from .models import SchnupperanmeldungForm, Schnupperanmeldung
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import render
import uuid


class SchnupperanmeldungFormView(FormView):
    """Display and process input form for new registration."""
    template_name = 'schnupper/schnupperanmeldung.html'
    form_class = SchnupperanmeldungForm
    success_url = 'done'  # where to redirect after saving

    def form_valid(self, form):
        new_object = form.save(commit=False)  # create new database object, but don't save yet
        new_object.validation_id = uuid.uuid4()  # create random validation uuid
        new_object.save()  # save to database
        new_object.validation_url = self.request.build_absolute_uri('validate/{}'.format(new_object.validation_id))  # create link from id
        form.send_confirmation(new_object)  # send email
        return super().form_valid(form)


def validate(request, id):
    """Process a validation link clicked from the confirmation mail"""
    status = None
    anmeldung = Schnupperanmeldung.objects.get(validation_id=id)
    if not anmeldung:
        status = 'error'
    elif anmeldung.validated:
        status = 'already validated'
    else:
        anmeldung.validated = True
        anmeldung.save()
        status = 'success'
    return render(request, 'schnupper/validated.html', locals())

class SchnupperanmeldungListView(ListView):
    model = Schnupperanmeldung
    paginate_by = 100  # if pagination is desired

