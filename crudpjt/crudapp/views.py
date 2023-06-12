from django.shortcuts import redirect, render

from .models import New

# Create your views here.
def create(request):
    obj = New.objects.all()
    if request.method =='POST':
        var1 = request.POST.get('sl_no')
        var2 = request.POST.get('item_name')
        var3 = request.POST.get('description')
        x = New(sl_no = var1, item_name = var2, description = var3)
        x.save()
    return render(request,'create.html',{'key1':obj})

def update(request,id):
    obj1 = New.objects.get(id=id)
    if request.method =='POST':
        var1 = request.POST.get('sl_no')
        var2 = request.POST.get('item_name')
        var3 = request.POST.get('description')
        New.objects.filter(id=id).update(sl_no = var1, item_name = var2, description = var3)
        return redirect('/')
    return render(request, 'update.html', {'key2': obj1})


def delete(request,id):
    obj2 = New.objects.get(id=id)
    if request.method=='POST':
        obj2.delete()
        return redirect('/')
    return render(request,'delete.html')
    