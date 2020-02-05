from django.shortcuts import render
from .models import Bus
from django.core.paginator import Paginator
import io 
from django.http import FileResponse 
# from reportlab.pdfgen import canvas

# Create your views here.

def buses(request):
    all_buses = Bus.objects.all()

    paginator = Paginator(all_buses,3)
    page = request.GET.get('page')
    buses =  paginator.get_page(page) 
    context = {'all_buses':buses}
    return render(request,"Buses/buses.html",context)
def detail(request,bus_id):
    single_bus = Bus.objects.get(id=bus_id)
    context = {'single_bus':single_bus}
    return render(request,'Buses/detail.html',context)
    
def toPdf(request,bus_id):
    buffer = io.BytesIO()
    # p = canvas.Canvas(buffer) #if you don't want the buffer you can write like "mm.pdf"
    p.drawString(100, 100, "Hello world.")
    p.showPage() 
    p.save()
    buffer.seek(0) 
    single_bus = Blog.objetcs.get(id = bus_id)
    response = HttpResponse(content_type='application/pdf')
    d = datetime.today().strftime('%Y-%m-%d')
    response['Content-Disposition'] = f'inline;filename="{d}.pdf"'
    buffer = BytesIO()
    p  = canvas.Canvas(buffer,pagesize = A4)
    data = {
        "bus":[{"name":bus_id.name,"description":bus_id.description}]
    }
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')