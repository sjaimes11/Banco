from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .logic import consultas_logic as cl
import json
from .forms import ConsultasForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def consultas_view(request):
    if request.method == 'GET':
        form = ConsultasForm()
        return render(request, 'Consulta/consultas.html', {'form': form})
    
    if request.method == 'POST':
        consulta_dto = cl.create_consulta(json.loads(request.body))
        consulta = serializers.serialize('json', [consulta_dto])
        return HttpResponse(consulta, 'application/json')