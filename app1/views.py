from django.shortcuts import render,redirect
from .forms import MedicineForm
from .models import Medicine
from django.conf import settings
from decimal import Decimal

# Create your views here.
def medicine_list(request):
    gst_rate = Decimal(settings.GST_RATE)
    # gst_rate_percentage = gst_rate * 100 
    medicines=Medicine.objects.all()

    total = Decimal(0)
    for medicine in medicines:
        medicine.total_price=medicine.price*medicine.quantity
        total += medicine.total_price

    # total=sum(m.price*m.quantity for m in medicines)
    gst=total* gst_rate
    grand_total=total+gst

    form=MedicineForm()
    if request.method=='POST':
        if 'submit' in request.POST:
            form=MedicineForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('medicine_list')
        elif 'calculate_total'in request.POST:
            pass
            

    context={
        'form':form,
        'medicines':medicines,
        'total':total,
        'gst':gst,
        'grand_total':grand_total,
        'gst_rate_percentage': gst_rate*Decimal(10),
    }
    return render(request,'index.html',context)

def delete_medicine(request, id):
    erase=Medicine.objects.filter(id=id)
    erase.delete()
    return redirect('medicine_list')
