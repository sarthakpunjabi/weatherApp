from django.shortcuts import render
import urllib.request 
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f'api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=e38ea79e03a8c02b34eb82d4dbc780a4').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+','+ str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp'])+'°C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":str(list_of_data['weather'][0]['icon']),
            "name":str(list_of_data["name"])
        }
        print(data)
    else:
        data = {}
    return render(request,"main.html",context=data)

