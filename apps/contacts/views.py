from django.views.generic import ListView

from apps.contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact List"
        return context
