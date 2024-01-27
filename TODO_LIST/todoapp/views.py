from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import Task

# Create your views here.
def display(request):
    # obj={'task':[{'id':1,'name':'Drinking Water','time':'6:00 AM'},
    #              {'id':2,'name':'Exercise','time':'6:30 AM'},
    #              {'id':3,'name':'Breakfast','time':'7:30 AM'}
    #              ]}
    data=Task.objects.all()
    obj={'task':data}
    return render(request,'task.html',obj)

def add(request):
    if request.method=='GET':
        return render(request,'add.html')
    else:
        nm=request.POST['name']
        time=request.POST['time']
        obj=Task.objects.create(name=nm,time=time)
        obj.save()
        return redirect('/')
    
def edit(request,tid):
    if request.method=='GET':
        obj=Task.objects.filter(id=tid)
        return render(request,'edit.html',{'task':obj})
    else:
        nm=request.POST['name']
        time=request.POST['time']
        obj=Task.objects.filter(id=tid)
        obj.update(name=nm,time=time)
        return redirect('/')

def delete(request,tid):
    obj=Task.objects.filter(id=tid) # where clause
    obj.delete()
    return redirect('/')