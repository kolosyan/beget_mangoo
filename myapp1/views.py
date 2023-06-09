from django.shortcuts import render

def home(request):
    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для главной страницы
    return render(request, 'myapp1/home.html')


def about(request):
    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для страницы "О нас"
    return render(request, 'myapp1/about.html')

def contact(request):
    # Здесь вы можете добавить любую логику, которую вы хотите выполнять для страницы "Контакты"
    return render(request, 'myapp1/contact.html')