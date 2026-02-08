from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Initiative, Resource
from .forms import InitiativeForm

def index(request):
    return render(request, "manara/index.html")

def dashboard(request):
    initiatives = Initiative.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "manara/dashboard.html", {
        "initiatives": initiatives
    })
def resources(request):
    all_resources = Resource.objects.all()
    return render(request, "manara/resources.html", {
        "resources": all_resources
    })
def create_initiative(request):
    if request.method == "POST":
        form = InitiativeForm(request.POST)
        if form.is_valid():
            initiative = form.save(commit=False)
            initiative.user = request.user
            initiative.save()
            return redirect('dashboard')
    else:
        form = InitiativeForm()

    return render(request, "manara/create.html", {"form": form})
def delete_initiative(request, initiative_id):
    # Get initiative and ensure it belongs to the current user
    initiative = get_object_or_404(Initiative, id=initiative_id, user=request.user)

    if request.method == "POST":
        initiative.delete()
        return redirect('dashboard')

    return redirect('dashboard')
def resources(request):
    # Render the static learning resources page
    return render(request, "manara/resources.html")
def initiative_detail(request, initiative_id):
    # Fetch the specific initiative by its ID
    initiative = get_object_or_404(Initiative, id=initiative_id)
    return render(request, "manara/initiative_detail.html", {
        "initiative": initiative
    })
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
