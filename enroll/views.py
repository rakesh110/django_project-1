from django.shortcuts import render
from .forms import Registration
from .models import Employee
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from enroll.filters import EmployeeFilter
from enroll.resources import EmployeeResource
from tablib import Dataset
import xlwt
from datetime import datetime
import requests
import json

# Create your views here.
def registration(request):
  if request.method == 'POST':
    fm = Registration(request.POST)
    if fm.is_valid():
      user = fm.save(commit=False)
      user.is_active = False
      user.save()
      current_site = get_current_site(request)
      message = render_to_string('enroll/acc_active_email.html', {
          'user':user, 'domain':current_site.domain,
          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      })
      mail_subject = 'Confirmation mail.'
      to_email = fm.cleaned_data.get('email')
      email = EmailMessage(mail_subject, message, to=[to_email])
      email.send()
      return HttpResponse('Congratulations,Your form has been submitted successfully')
      fm = Registration()
  
  else:
    fm = Registration()

  return render(request, 'enroll/userregistration.html', {'form':fm})

def showformdata(request):
  stud = Employee.objects.all()  #show data
  user_filter = EmployeeFilter(request.GET, queryset=stud)  #filter data
  stud = user_filter.qs
  return render(request,'enroll/showformdata.html',{'stu':stud , 'filter': user_filter})

##Import Export data from database 
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Employee'+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Employee')
    row_num=0
    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    columns = ['id','serial_no','date','employee_name','father_name','gender','residence','dob','physical_fitness','descriptive_marks','refusel_of_certificate','certificate_being_revoked','age','telephone','email','factory','department','examination_after_a_period']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style=xlwt.XFStyle()

    rows = Employee.objects.filter().values_list('id','serial_no','date','employee_name','father_name','gender','residence','dob','physical_fitness','descriptive_marks','refusel_of_certificate','certificate_being_revoked','age','telephone','email','factory','department','examination_after_a_period')
    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

#Sending sms from fast2sms
def send_sms(request):
  if request.method == 'POST':
    fm = Registration(request.POST)
    if fm.is_valid():
     
      url = 'https://www.fast2sms.com/dev/bulk'
      params = {
          'authorization': '47mj0bWsOpJzBCxNMuK8adQk9Ulnq6LHRPwGYIFXegtrSvZT5AMSv45INhgR0P2nTDeaWdKwpim9X3BF',
          'sender_id': 'FSTSMS',
          'message': message,
          'language': 'english',
          'route': 'p',
          'numbers': telephone
      }
      response = requests.get(url, params=params)
      dic = response.json()
      print(dic)
      return dic.get('return')
      return render(request,'enroll/contact.html',{'form':fm,'prms':params,'url':url})