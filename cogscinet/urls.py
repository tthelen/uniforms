from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.VereinFormView.as_view()),  # show form for filling in
    path('done', TemplateView.as_view(template_name='cogscinet/done.html')),  # dsiplay success message
    path('validate/<uuid:id>', views.validate),  # validate e-mail address
    path('list', login_required(views.VereinListView.as_view())),  # list data (authenticated only!)
]