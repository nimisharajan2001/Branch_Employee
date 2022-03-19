from django.http import request
from django.shortcuts import render
from .models import *
# Create your views here.

def Superadmin_index(request):
    return render(request,'Superadmin_index.html')

def Superadmin_Branch(request):
    return render(request,'SuperAdmin_Branch.html')

def Superadmin_AddBranch(request):
    if request.method == 'POST':
        br1 = request.POST['Brname']
        br2 = request.POST['location']
        br3 = request.POST['Brtype']
        br4 = request.POST['Bradmin']
        br5 = request.POST['Bremail']
        br6 = request.POST['Brcontact']
        br7 = request.FILES['img[]']

        new1 = branch_registration(branch_name=br1,location=br2,
                                  branch_type=br3, branch_admin=br4,logo = br7,
                                  email= br5,mobile =br6)
        new1.save()

    return render(request,'SuperAdmin_AddBranch.html')

def Superadmin_Dash(request):
    return render(request,'SuperAdmin_dashboard.html')


def Superadmin_employees(request):
    Dept = department.objects.all()
    return render(request,'SuperAdmin_Employees1.html',{'Dept':Dept})

        
def Superadmin_edepartments(request,id):
    Dept = department.objects.get(id = id)
    deptid=id        
    Desig = designation.objects.all()
    return render(request,'SuperAdmin_edpartments.html',{'Desig':Desig,'Dept':Dept,'dept_id':deptid})

def Superadmin_projectman(request,id,did):
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'Superadmin_projectman.html',{'pro_man_data':Project_man_data,'project_name':project_name,'Project_man':Project_man})
    

def Superadmin_ViewTrainers(request,id,did):       
    projectname=project.objects.all()
    trainer=designation.objects.get(id=id)
    userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
    return render(request,'Superadmin_ViewTrainers.html', {'user_registration':userreg, 'project':projectname})
    


def Superadmin_View_Trainerprofile(request,id):
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]          
        data=[i.workperformance,i.attitude,i.creativity]  
    userreg=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Trainerprofile.html', {'user_registration':userreg,'labels':labels,'data':data})



def Superadmin_View_Currenttraineesoftrainer(request,id):
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='trainee')
    user2=user_registration.objects.filter(designation=trainee)
    return render(request,'Superadmin_View_Currenttraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})
   
def Superadmin_View_Currenttraineeprofile(request,id):
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]          
        data=[i.workperformance,i.attitude,i.creativity]  
    userreg=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Currenttraineeprofile.html', {'user_registration':userreg,'labels':labels,'data':data})
   
       
def Superadmin_View_Currenttraineetasks(request,id):
        # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'Superadmin_View_Currenttraineetasks.html',{'trainer_task':tasks})
    
       
def Superadmin_View_Currenttraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Currenttraineeattendance.html', {'user_registration':usr})


def Superadmin_ViewCurrenttraineeattendancesort(request,id): 
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_View_Currenttraineeattendancesort.html',{'adata':adata,'user_registration':usr})
    
        
def Superadmin_View_Previoustraineesoftrainer(request,id): 
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='trainee')
    user2=user_registration.objects.filter(designation=trainee)
    return render(request,'SuperAdmin_View_Previoustraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def Superadmin_View_Previoustraineetasks(request,id):   
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)        
    return render(request,'Superadmin_View_Previoustraineetasks.html',{'trainer_task':tasks})


def Superadmin_View_Previoustraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'Superadmin_View_Previoustraineeattendance.html', {'user_registration':usr})


def Superadmin_ViewPrevioustraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_ViewPrevioustraineeattendancesort.html',{'adata':adata,'user_registration':usr})
    
   
def Superadmin_View_Trainerattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Trainerattendance.html', {'user_registration':usr})
    


def Superadmin_ViewTrainerattendancesort(request,id):  
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_ViewTrainerattendancesort.html',{'adata':adata,'user_registration':usr})
    

def Superadmin_View_Previoustraineeprofile(request,id):   
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]          
        data=[i.workperformance,i.attitude,i.creativity]  
    usr=user_registration.objects.get(id=id)
    return render(request,'Superadmin_View_Previoustraineeprofile.html', {'user_registration':usr,'labels':labels,'data':data})
    
    
def Superadmin_proname(request,id):
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]          
        data=[i.workperformance,i.attitude,i.creativity]
    Project_man_data = user_registration.objects.get(id = id)
    return render(request,'SuperAdmin_proname.html',{'pro_man_data':Project_man_data,'data':data,'labels':labels})
    

def Superadmin_proinvolve(request,id):
    Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
    return render(request,'Superadmin_proinvolve.html',{'pro_data':Pro_data})
    
def Superadmin_promanatten(request,id):
    id = id
    return render(request, 'Superadmin_promanatten.html',{'id':id})
    

def Superadmin_promanattendsort(request,id):
    id = id
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
        mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
    return render(request, 'SuperAdmin_promanattensort.html',{'mem1':mem1,'id':id})
    


