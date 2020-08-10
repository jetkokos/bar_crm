from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *

# Create your views here.

@login_required
def createReportView(request):
    if request.method == 'POST':
        form = CreateReportForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect('reports')
    else:
        form = CreateReportForm()
    context = {
        'form':form,
    }
    return render(request, 'create_report.html', context)
    

@login_required
def updateReportView(request, pk=None):
    if request.user.is_superuser:
        report = get_object_or_404(Report, pk=Report.objects.latest('date').pk) 
    else:
        report = get_object_or_404(Report, pk=Report.objects.filter(created_by=request.user).latest('date').pk)

    if request.method == "POST":
        form = UpdateReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = UpdateReportForm(instance=report)
    context = {
        'form':form,
        'report':report
    }
    return render(request, 'update_report.html', context)


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html', {})


@login_required
# @permission_required('is_superuser')
def reportsView(request):
    last_report = Report.objects.latest('date')
    current_user = request.user
    edit_button_visibility = False
    if current_user.is_superuser:
        edit_button_visibility = True
        reports = Report.objects.all().order_by('-date')
    else:
        reports = Report.objects.order_by('-date')[:3]  
        if last_report.created_by == current_user:
            edit_button_visibility == True

    context = {
        'reports': reports,
        'edit_button_visibility': edit_button_visibility,
    }

    return render(request, 'reports.html', context)
    

@login_required
@permission_required('is_superuser')
def expensesView(request):
    reports = Report.objects.all()
    formatted_reports = reports.order_by('-date')
    context = {
        'reports': reports,
    }

    return render(request, 'expenses.html', context)

@login_required
@permission_required('is_superuser')
def proceedView(request):
    reports = Report.objects.all()
    formatted_reports = reports.order_by('-date')
    context = {
        'reports': reports,
    }

    return render(request, 'proceed.html', context)    


    
