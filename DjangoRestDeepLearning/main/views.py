from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'change_language.html'
