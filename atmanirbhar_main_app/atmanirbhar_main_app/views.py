from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
#generic view made
class TestPage(TemplateView):
    template_name = 'test.html'

#generic view made
class ThanksPage(TemplateView):
    template_name = 'thanks.html'

#generic view made
class HomePage(TemplateView):
    template_name = 'index.html'

    #redirect to test if user is authenticated
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
