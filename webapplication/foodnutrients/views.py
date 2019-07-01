from django.shortcuts import render, redirect
from foodnutrients.forms import nutrientsform
from foodnutrients.models import nutrients

def nut(request):
    if request.method=="POST":
        form=nutrientsform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
    else:
        form=nutrientsform()
    return render(request,"index.html",{'form':form})
def show(request):
    nutrient=nutrients.objects.all()
    return render(request,"show.html",{'nutrient':nutrient})
def edit(request,id):
    nutrient=nutrients.objects.get(id=id)
    return render(request,"edit.html",{'nutrient':nutrient})
def update(request,id):
    nutrient=nutrients.objects.get(id=id)
    form=nutrientsform(request.POST,instance=nutrient)
    if form.isvalid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'nutrient':nutrient})
