from django.shortcuts import render
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import BranchModel, BankModel


from .forms import BankForm,UserForm,BranchForm
# Create your views here.


class DashboardView(TemplateView):
   template_name = 'banks/dashboard.html'
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bank = BankModel.objects.all()
        branch = BranchModel.objects.all()
        context = {'bk':bank, 'br':branch}
        print(context)
        return context    

class BankView(FormView):
    template_name = 'banks/banktemp.html'
    form_class = BankForm
    success_url = '/bank/bankform/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class BankUpdateView(UpdateView):
    model =BankModel
    fields =['owner', 'bankname', 'swift_code', 'inst_num', 'description']
    success_url = '/'
    template_name = 'banks/banktemp.html'

class BankDeleteView(DeleteView):
    model = BankModel
    success_url ='/'
   
    
class BranchView(FormView):
    template_name = 'banks/branchtemp.html'
    form_class = BranchForm
    success_url = '/bank/branchform/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)   


class BranchUpdateView(UpdateView):
    model =BranchModel
    fields =['bank','name', 'transit_num', 'address', 'email', 'capacity']
    success_url = '/'
    template_name = 'banks/banktemp.html'

class BranchDeleteView(DeleteView):
    model = BranchModel
    success_url ='/' 

class UserView(FormView):
    template_name ='banks/login.html'
    form_class = UserForm
    success_url= '/'