import os

import folium
from django.contrib.auth.models import User
from app.models import VisitedCity, City, UserDetails, InterestedCity, PlanningCity
from app.services.legacy_session import get_legacy_session


def get_geojson(city: City):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/municipios/{city.ibge_id}?formato=application/vnd.geo+json&qualidade=maxima"
    return get_legacy_session().get(url).json()


def get_visited_cities(user_map, user, style):
    visited_cities = VisitedCity.objects.filter(user_id_id=user.id)
    cities_name = []
    for visited_city in visited_cities:
        cities_name.append(City.objects.get(id=visited_city.city_id_id))
    for city in cities_name:
        folium.GeoJson(get_geojson(city), name=f'{city.city}',
                       style_function=lambda x: style).add_to(user_map)


def get_interested_cities(user_map, user, style):
    interested_cities = InterestedCity.objects.filter(user_id_id=user.id)
    cities_name = []
    for visited_city in interested_cities:
        cities_name.append(City.objects.get(id=visited_city.city_id_id))
    for city in cities_name:
        folium.GeoJson(get_geojson(city), name=f'{city.city}',
                       style_function=lambda x: style).add_to(user_map)


def get_planning_cities(user_map, user, style):
    planning_cities = PlanningCity.objects.filter(user_id_id=user.id)
    cities_name = []
    for visited_city in planning_cities:
        cities_name.append(City.objects.get(id=visited_city.city_id_id))
    for city in cities_name:
        folium.GeoJson(get_geojson(city), name=f'{city.city}',
                       style_function=lambda x: style).add_to(user_map)


def get_hometown(user_map, user, style):
    user_details = UserDetails.objects.get(user_id_id=user.id)
    hometown = City.objects.get(id=user_details.hometown)
    folium.GeoJson(get_geojson(hometown), name=f'{hometown.city}',
                   style_function=lambda x: style).add_to(user_map)


def generate_map(request):
    user = User.objects.get(username=request.user)
    user_map = folium.Map(location=[-22.9051, -47.0613])
    visited_cities_style = {'fillColor': '#FF0000', 'color': '#FF0000'}
    interested_cities_style = {'fillColor': '#0000FF', 'color': '#0000FF'}
    planning_cities_style = {'fillColor': '#F8FC03', 'color': '#F8FC03'}
    hometown_style = {'fillColor': '#00FFFF', 'color': '#00FFFF'}
    get_visited_cities(user_map, user, visited_cities_style)
    get_interested_cities(user_map, user, interested_cities_style)
    get_planning_cities(user_map, user, planning_cities_style)
    get_hometown(user_map, user, hometown_style)

    if not os.path.isdir(f'app/templates/map/{user.username}'):
        os.mkdir(f'app/templates/map/{user.username}')
    user_map.save(f'app/templates/map/{user.username}/map.html')
