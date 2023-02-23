from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"
    queryset = Contact.objects.all().order_by("-modified_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact List"
        return context


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Details Contact"
        return context


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Contact"
        return context


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Contact"
        return context


class ContactDeleteView(DeleteView):
    model = Contact

    success_url = reverse_lazy("contacts:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Contact"
        return context
