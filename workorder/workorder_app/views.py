from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

# Create your views here.
def admin_view(request):
    return render(request, 'admin_view.html')

def index(request):
    request.session.flush()
    request.session.clear()
    context = {
        'all_jobs' : JobName.objects.all()
    }
    return render(request, 'home.html', context)

def jobname(request):
    context = {
        'all_jobs' : JobName.objects.all()
    }
    return render(request, 'jobname.html', context)

def create_job(request):
    if request.method == 'POST':
        new_job = JobName.objects.create(name = request.POST['job_name'], contractor_name = request.POST['contractor_name'], street = request.POST['street'], city= request.POST['city'], state= request.POST['state'], zip_code = request.POST['zipcode'])
        return redirect('/jobname')
    else:
        return redirect('/jobname')

def delete_job(request, job_id):
    JobName.objects.get(id=job_id).delete()
    return redirect('/jobname')

def create_order(request):
    if request.method == 'POST':
        print('Welcome, you are trying to create a work order!')
        job_id_selected = JobName.objects.get(id=request.POST['contractor'])
        new_c_f = CarpenterForeman.objects.create(labor_type=request.POST['labor_type_cf'],employee_numbers=request.POST['employee_numbers_cf'], regular_hours=request.POST['regular_hours_cf'], premium_hours=request.POST['premium_hours_cf'])
        new_c_j = CarpenterJourneyamn.objects.create(labor_type=request.POST['labor_type_cj'],employee_numbers=request.POST['employee_numbers_cj'], regular_hours=request.POST['regular_hours_cj'], premium_hours=request.POST['premium_hours_cj'])
        new_t_f = TaperForeman.objects.create(labor_type=request.POST['labor_type_tf'],employee_numbers=request.POST['employee_numbers_tf'], regular_hours=request.POST['regular_hours_tf'], premium_hours=request.POST['premium_hours_tf'])
        new_t_j = TaperJourneyman.objects.create(labor_type=request.POST['labor_type_tj'],employee_numbers=request.POST['employee_numbers_tj'], regular_hours=request.POST['regular_hours_tj'], premium_hours=request.POST['premium_hours_tj'])
        new_lab = Laborer.objects.create(labor_type=request.POST['labor_type_l'],employee_numbers=request.POST['employee_numbers_l'], regular_hours=request.POST['regular_hours_l'], premium_hours=request.POST['premium_hours_l'])
        new_sup = Supervisor.objects.create(labor_type=request.POST['labor_type_s'],employee_numbers=request.POST['employee_numbers_s'], regular_hours=request.POST['regular_hours_s'], premium_hours=request.POST['premium_hours_s'])
        new_order = WorkOrder.objects.create(
            location=request.POST['location'], 
            work_performed=request.POST['work_performed'],
            signature_1=request.POST['signature_1'],
            signator_1=request.POST['signator_1'], 
            signature_2=request.POST['signature_2'],
            signator_2=request.POST['signator_2'], 
            jobname=job_id_selected, 
            carpenterforeman=CarpenterForeman.objects.get(id=new_c_f.id), 
            carpenterjourneyamn=CarpenterJourneyamn.objects.get(id=new_c_j.id), 
            taperforeman=TaperForeman.objects.get(id=new_t_f.id), 
            taperjourneyman=TaperJourneyman.objects.get(id=new_t_j.id), 
            laborer=Laborer.objects.get(id=new_lab.id), 
            supervisor=Supervisor.objects.get(id=new_sup.id))
        mat_count = int(request.POST['material_count'])
        for i in range(1, mat_count+1):
            new_material = Material.objects.create(product=request.POST[f"product{i}"], quantity= request.POST[f"quantity{i}"],workorder=WorkOrder.objects.get(id=new_order.id))   
        return redirect (f"/workorderpreview/{new_order.id}")
    else:
        return redirect('/')

def all_work_orders(request):
    context = {
        'all_work_orders': WorkOrder.objects.all()
    }
    return render(request, "workorder.html", context)

def show_work_order(request, workorder_id):
    context = {
        'this_work_order' : WorkOrder.objects.get(id=workorder_id)
    }
    return render(request, 'showworkorder.html', context)

def workorderpreview(request, workorder_id):
    context = {
        'this_work_order' : WorkOrder.objects.get(id=workorder_id)
    }
    return render(request, 'workorderpreview.html', context)


def delete_work_order(request, workorder_id):
    WorkOrder.objects.get(id=workorder_id).delete()
    return redirect ('/workorder')