from django.shortcuts import render


# Представление для страницы "О проекте"
def about(request):
    return render(request, 'pages/about.html')


# Представление для страницы "Наши правила"
def rules(request):
    return render(request, 'pages/rules.html')


def category_posts(request, category_slug):
    # Передаём slug категории в контекст
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
