from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'personal_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/news/')


@login_required
def do_author(request):
    user = request.user
    author_group = Group.objects.get(name = 'authors')
    if not request.user.groups.filter(name = 'authors').exists():
        author_group.user_set.add(user)
    return redirect('/news/')