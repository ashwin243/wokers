from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Worker
from .forms import BookingForm
def home(request):
    return render(request, 'services/home.html')

def index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})


def service_list(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    workers = Worker.objects.filter(service=service)
    return render(request, 'services/service_list.html', {'service': service, 'workers': workers})

def worker_detail(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    return render(request, 'services/worker_detail.html', {'worker': worker})

def book_worker(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.worker = worker
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'services/booking_form.html', {'form': form, 'worker': worker})
