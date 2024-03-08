from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]


def about(request) -> HttpResponse:
    """Описание проекта."""
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    """Правила проекта."""
    template: str = 'pages/rules.html'
    return render(request, template)
