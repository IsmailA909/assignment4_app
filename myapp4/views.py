from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from datetime import datetime
from django.http import HttpResponseForbidden
from datetime import datetime, timedelta  # Import timedelta



def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp4/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'myapp4/contact_detail.html', {'contact': contact})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            entry_date = form.cleaned_data['entry_date']
            expiry_date = form.cleaned_data['expiry_date']

            # Check if expiry_date is greater than entry_date
            if expiry_date <= entry_date:
                return HttpResponseForbidden("Expiry date must be greater than entry date.")

            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'myapp4/contact_form.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'myapp4/contact_form.html', {'form': form, 'contact': contact})



def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    
    # Calculate the maximum allowed expiry date (1 year from today)
    max_expiry_date = datetime.today() + timedelta(days=365)

    if request.method == 'POST':
        expiry_date = contact.expiry_date

        # Ensure both expiry_date and max_expiry_date are of type datetime.date
        if isinstance(expiry_date, datetime):
            expiry_date = expiry_date.date()

        # Check if expiry_date is not more than 1 year away
        if expiry_date <= max_expiry_date.date():
            contact.delete()
            return redirect('contact_list')
        else:
            return HttpResponseForbidden("Cannot delete contacts with expiry date more than 1 year away.")

    return render(request, 'myapp4/contact_confirm_delete.html', {'contact': contact})