import os

import folium
from django.contrib.auth.models import User
from app.models import VisitedCities, City
from app.services.legacy_session import get_legacy_session


def generate_map(request):
    user = User.objects.get(username=request.user)
    visited_cities = VisitedCities.objects.filter(user_id_id=user.id)
    cities_name = []
    for visited_city in visited_cities:
        cities_name.append(City.objects.get(id=visited_city.city_id_id))
    user_map = folium.Map(location=[-22.9051, -47.0613])
    cities_geojson = []
    for city in cities_name:
        url = f"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/{city.ibge_id}?formato=application/vnd.geo+json&qualidade=maxima"
        cities_geojson.append(get_legacy_session().get(url).json())
    for city in cities_geojson:
        print(city)
        folium.GeoJson(city, name=f'teste').add_to(user_map)
    if not os.path.isdir(f'app/templates/map/{user.username}'):
        os.mkdir(f'app/templates/map/{user.username}')
    user_map.save(f'app/templates/map/{user.username}/map.html')