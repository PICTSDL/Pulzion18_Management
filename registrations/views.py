from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from .models import Registration, Certification, Participant
import sqlite3

eventName = ""
eventURL = ""


def getRegistrationForm(request):
    return render(request, 'register.html')


def homePage(request):
    return render(request, 'homepage.html')

# Save Details After Submitting The Registration Form
def registered(request):
    try:
        registration = Registration()
        registration.receiptNumber = request.GET["receipt"]
        registration.name = request.GET["name"]
        registration.college = request.GET["college"]
        registration.year = request.GET["year"]
        registration.email = request.GET["email"]
        registration.contact = request.GET["phone"]
        registration.event = request.GET["event"]
        registration.save()
        return redirect('/register/')
    except:
        return HttpResponse("<h1>ERROR! The Receipt Number Must Be Unique</h1>")

# Get List Of All Participants Of Pulzion
def getParticipantList(request):
    participantList = Registration.objects.all().order_by('receiptNumber')
    return render(request,'participantsListPage.html', locals())

def postToEventList(request,receiptNumber):
    RegData = Registration.objects.get(receiptNumber=receiptNumber)
    participant = Participant()
    participant.receiptNumber = RegData.receiptNumber
    participant.name = RegData.name
    participant.college = RegData.college
    participant.year = RegData.year
    participant.event = RegData.event
    participant.save()
    return redirect("/participants/")

def postToCertificateList(request, receiptNumber):
    RegData = Registration.objects.get(receiptNumber=receiptNumber)
    participant = Participant.objects.get(receiptNumber=receiptNumber)
    certification = Certification()
    certification.receiptNumber = RegData.receiptNumber
    certification.name = RegData.name
    certification.college = RegData.college
    certification.year = RegData.year
    certification.event = RegData.event
    certification.save()
    participant.delete()
    return redirect('/' + eventURL + '/')

# Get List Of Participant Who Have Finished The Event And Certificate Can Be Given
def certificateList(request):
    query_details = Certification.objects.all().order_by('receiptNumber')
    return render(request, 'certificates.html', locals())

# Get List Of Participants Of The Current Selected Event
def getEventParticipants(request,event):
    global eventURL
    eventURL = event
    event = event[:-5]
    whitespace1 = event.find("_")
    if whitespace1!=-1:
        eventName = event[:whitespace1] + " "
        whitespace2 = event.find("_", whitespace1+1)
        if whitespace2!=-1:
            eventName = eventName + event[whitespace1+1:whitespace2] + " "
            eventName = eventName + event[whitespace2+1:]
        else:
            eventName = eventName + event[whitespace1 + 1:]
    else:
        eventName = event

    participantList = Participant.objects.all().filter(event=eventName)
    return render(request, 'displayEventParticipants.html', locals())

def eventsList(request):
    return render(request, 'events.html')