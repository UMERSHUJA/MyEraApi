from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import JobList


def joblist(request):
    if request.method == "POST":
        job_title = request.POST['job_title']
        description = request.POST['description']
        icon = request.POST['image']
        company_name = request.POST['company_name']
        experience = request.POST['experience']
        job_type = request.POST['job_type']
        destination = request.POST['destination']
        job_link = request.POST['job_link']
        # user_id = request.POST['user_id']
        if request.user.is_authenticated:
            user_id = request.user.id
        
        
        joblist = JobList(job_title=job_title, description=description, icon=icon, company_name=company_name, experience=experience, job_type=job_type, destination=destination, job_link=job_link, user_id=user_id)
        joblist.save()
         
        # Send mail
        send_mail(
            'Property Listing Inquiry',
            'there has been an inquiry for ' + str(joblist) + '. Sign into the admin panel for more info',
            'umershuja12@gmail.com',
            ['suirsan12@gmail.com'],
            fail_silently=False
        )


        messages.success(request, 'Your requested has been submitted, wait for the admin response')
        
        return redirect('dashboard')


def listing(request, id):
    job = JobList.objects.order_by('submission_date').filter(published=True, id = id)
    context = {
        'job': job,
    }
    
    return render(request, 'pages/joblist.html', context)



def editjob(request, joblist_id):
    jobs = JobList.objects.all().filter(id=joblist_id)
            
    context= {
        'jobs' : jobs,
    }
    return render(request, 'pages/editjob.html', context)


def changeoccur(request, joblist_id):
    if request.method == 'POST':
        job = JobList.objects.get(pk = joblist_id)
        job.job_title = request.POST['job_title']
        job.description = request.POST['description']
        job.icon = request.POST['image']
        job.company_name = request.POST['company_name']
        job.experience = request.POST['experience']
        job.job_type = request.POST['job_type']
        job.destination = request.POST['destination']
        job.job_link = request.POST['job_link']

        job.save()
        messages.success(request, 'You job has been altered sucessfully!')
        
        return redirect('dashboard')



def deljob(request, joblist_id):
    jobs = get_object_or_404(JobList, pk=joblist_id)
    jobs.delete()
    messages.success(request, 'Your job has been deleted successfully')
    return redirect('dashboard')


