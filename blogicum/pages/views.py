from django.shortcuts import render


def about(request):
    """Описание проекта."""
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Правила проекта."""
    template: str = 'pages/rules.html'
    return render(request, template)
