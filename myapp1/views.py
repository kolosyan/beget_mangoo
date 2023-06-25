from django.shortcuts import render
from .forms import MyModelForm
from .models import Employer  # Не забудьте про этот импорт

# Остальной код...

def home(request):
    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для главной страницы
    return render(request, 'myapp1/home.html')


def about(request):
    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для страницы "О нас"
    return render(request, 'myapp1/about.html')

def contact(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = MyModelForm()
            # возвращаемся на страницу после успешного сохранения
    else:
        form = MyModelForm()


    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для страницы "Контакты"
    return render(request, 'myapp1/contact.html', {'form': form})

def output(request):
    employers = Employer.objects.all()
    return render(request, 'myapp1/output.html', {'employers': employers})
