from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jobname', views.jobname),
    path('create_jobname', views.create_job),
    path('delete_job/<int:job_id>', views.delete_job),
    path('create_order', views.create_order),
    path('workorder', views.all_work_orders),
    path('show_work_order/<int:workorder_id>', views.show_work_order),
    path('delete/<int:workorder_id>', views.delete_work_order),
    path('workorderpreview/<int:workorder_id>', views.workorderpreview),
]
