from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import salesAgent
from .forms import salesAgentForm


# Create your views here.
def index(request):
    return render(request, 'salesagents/index.html', {
        'salesagents': salesAgent.objects.all()
    })


def view_salesagent(request, id):
    salesagent = salesAgent.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = salesAgentForm(request.POST)
        if form.is_valid():
            new_agent_serial_no = form.cleaned_data['agent_serialNo']
            new_first_name = form.cleaned_data['first_name']
            new_surname = form.cleaned_data['surname']
            new_phone_number = form.cleaned_data['phone_number']
            new_assigned_area = form.cleaned_data['assigned_area']
            new_team_leader = form.cleaned_data['team_leader']
            new_status = form.cleaned_data['status']

            new_salesagent = salesAgent(
                agent_serialNo = new_agent_serial_no,
                first_name = new_first_name,
                surname = new_surname,
                phone_number = new_phone_number,
                assigned_area = new_assigned_area,
                team_leader = new_team_leader,
                status = new_status
            )
            new_salesagent.save()
            return render(request, 'salesagents/add.html', {
                'form': salesAgentForm(),
                'successs': True
            })
        else:
            form = salesAgentForm()
        return render(request, 'salesagents/add.html', {
            'form': salesAgentForm()
        })


def edit(request, id):
    if request.method == 'POST':
        salesagent = salesAgent.objects.get(pk=id)
        form = salesAgentForm(request.POST, instance=salesagent)
        if form.is_valid():
            form.save()
            return render(request, 'salesagents/edit.html', {
                'form': form,
                'success': True
            })
        else:
            salesagent = salesAgent.objects.get(pk=id)
            form = salesAgentForm(instance=salesagent)
        return render(request, 'salesagents/edit.html', {
            'form': form
        })


def delete(request, id):
    if request.method == 'POST':
        salesagent = salesAgent.objects.get(pk=id)
        salesagent.delete()
    return HttpResponseRedirect(reverse('index'))
