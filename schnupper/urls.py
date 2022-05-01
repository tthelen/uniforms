from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.SchnupperanmeldungFormView.as_view()),  # show form for filling in
    path('done', TemplateView.as_view(template_name='schnupper/done.html')),  # dsiplay success message
    path('validate/<uuid:id>', views.validate),  # validate e-mail address
    path('list', login_required(views.SchnupperanmeldungListView.as_view())),  # list data (authenticated only!)
]