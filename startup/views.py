from django.shortcuts import render, redirect, get_object_or_404
from .models import Startup
from django.contrib import messages
from django.core.mail import send_mail



def startup(request):
    if request.method == "POST":

        product_name = request.POST['product_name']
        description = request.POST['description']
        image = request.POST['image']
        user_id = request.POST['user_id']
        price = request.POST['price']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        sponsered = 'sponsered' in request.POST
        
        startup = Startup(product_name=product_name, description=description, image=image, prices=price, facebook=facebook, twitter=twitter, is_sponsered=sponsered, user_id=user_id)
        
        startup.save()
        # Send mail
        send_mail(
            'Property Listing Inquiry',
            'there has been an inquiry for ' + str(startup) + '. Sign into the admin panel for more info',
            'umershuja12@gmail.com',
            ['suirsan12@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your requested has been submitted, wait for the admin response')
        
        return redirect('dashboard')




def listing(request, id):
    startup = Startup.objects.order_by('submission_date').filter(published=True, id = id)
    context = {
        'startup': startup,
    }
    
    return render(request, 'pages/listing.html', context)



def editstartup(request, startuplist_id):
    startups = Startup.objects.all().filter(id=startuplist_id)
            
    context= {
        'startups' : startups,
    }
    return render(request, 'pages/editstartup.html', context)


def changeoccur(request, startuplist_id):
    if request.method == 'POST':
        startup = Startup.objects.get(pk = startuplist_id)
        startup.product_name = request.POST['product_name']
        startup.description = request.POST['description']
        startup.image = request.POST['image']
        startup.prices = request.POST['price']
        startup.facebook = request.POST['facebook']
        startup.twitter = request.POST['twitter']
        startup.is_sponsered = 'sponsered' in request.POST
        startup.save()
        messages.success(request, 'You startup has been altered sucessfully!')
        
        return redirect('dashboard')



def delstartup(request, startuplist_id):
    jobs = get_object_or_404(Startup, pk=startuplist_id)
    jobs.delete()
    messages.success(request, 'Your startup has been deleted successfully')
    return redirect('dashboard')
