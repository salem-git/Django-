from django.shortcuts import render
from .models import Journey
from django.contrib.auth.models import User 
from django.core.paginator import Paginator
import io 
from django.http import FileResponse 
from reportlab.pdfgen import canvas
from django.http import HttpResponse


# Create your views here.
def index(response,id):
    ls = Journey.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")

def cutomer_reserve_submission(request):
    print("ticket successfully reserved")
    journey_departure = request.POST["journey_departure"]
    journey_destination = request.POST["journey_destination"]
    journey_date = request.POST["journey_date"]
    journey_numberOfTicket = request.POST["journey_numberOfTicket"]
    journey_seatReserve = request.POST["journey_seatReserve"]

    journey = Journey(departure=journey_departure,destination=journey_destination,date=journey_date,number_of_ticket=journey_numberOfTicket,seat_number=journey_seatReserve )
    journey.save()
    return render(request,"CustomerHome/CustomerHome.html")

def fetch_journey(request): 
    all_journey = Journey.objects.all()

    paginator = Paginator(all_journey,3)
    page = request.GET.get('page')
    journies =  paginator.get_page(page)
    context = {'all_journey':journies}
    return render(request,"CustomerHome/recentJourney.html",context)

def recent_journey_detail(request,rjourney_id):
    single_journey = Journey.objects.get(id=rjourney_id)
    context = {'single_journey':single_journey}
    return render(request,'CustomerHome/recentJourneyDetail.html',context)

def logged(request):
    return render(request,'CustomerHome/CustomerHome.html')
def create(response):
    if response.method == "POST":
        if form.is_valid():
            d=form.cleaned_data["destination"]
            j = Journey(destination=d)
            j.save()
            response.user.journey.add(j)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response,"CustomerHome/recentJourney.html",{"form":form})
def buyTicket(request):
    return render(request,'BookConfirmation/buy.html')
def confirm_ticket(request):
    return render(request,'BookConfirmation/success.html')
def profile(request):
    return render(request,'CustomerHome/profile.html')
def generate_pdf(request):
    
    # Model data
    user = User.objects.all().order_by('username')

    # Rendered
    html_string = render_to_string('CustomerHome/ticket.html', {'user': User})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    return response
def toPdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer) #if you don't want the buffer you can write like "mm.pdf"
    p.drawString(40,450, "Ticket Reserved Successfully.Here is Your Ticket.Now you are legitmate to travel")
    



    p.showPage() 
    p.save()
    buffer.seek(0) 
    return FileResponse(buffer, as_attachment=True, filename='ticket.pdf')
