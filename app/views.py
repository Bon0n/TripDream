from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import City, State, UserDetails, InterestedCity, VisitedCity, PlanningCity
from app.services.ajax import is_ajax
from app.services.generate_map import generate_map
from app.services.user_details import update_user_details


def login(request):
    return render(request, 'account/login.html')


@login_required
def home(request):
    user = User.objects.get(username=request.user)
    cities = City.objects.all()
    states = State.objects.all()
    try:
        user_details = UserDetails.objects.get(user_id_id=user.id)
        state_hometown = State.objects.get(id=user_details.state_hometown)
        hometown = City.objects.get(id=user_details.hometown)
        data = {
            'user_details': user_details,
            'cities': cities,
            'states': states,
            'hometown': hometown,
            'state_hometown': state_hometown
        }
        return render(request, 'user/index.html', data)
    except:
        data = {
            'cities': cities,
            'states': states
        }
        return render(request, 'user/index.html', data)


@login_required
def update_user(request):
    userdata = User.objects.get(username=request.user)
    userdata.name = request.POST.get('name')
    update_user_details(request)
    return redirect(home)


@login_required
def visited_cities(request):
    user = User.objects.get(username=request.user)
    visited_cities_id = VisitedCity.objects.filter(user_id_id=user.id)

    visited_cities = []
    for visited_city_id in visited_cities_id:
        visited_cities.append(City.objects.get(id=visited_city_id.city_id_id))

    for visited_city in visited_cities:
        visited_city.state = State.objects.get(id=visited_city.state_id_id)

    states = State.objects.all()
    cities = City.objects.all()
    data = {
        'states': states,
        'cities': cities,
        'visited_cities': visited_cities
    }
    return render(request, 'user/visited_cities.html', data)


@login_required
def interested_cities(request):
    user = User.objects.get(username=request.user)
    interested_cities_id = InterestedCity.objects.filter(user_id_id=user.id)

    interested_cities = []
    for interested_city_id in interested_cities_id:
        interested_cities.append(City.objects.get(id=interested_city_id.city_id_id))

    for interested_city in interested_cities:
        interested_city.state = State.objects.get(id=interested_city.state_id_id)

    states = State.objects.all()
    cities = City.objects.all()
    data = {
        'states': states,
        'cities': cities,
        'interested_cities': interested_cities
    }
    return render(request, 'user/interested_cities.html', data)


@login_required
def planning_cities(request):
    user = User.objects.get(username=request.user)
    planning_cities_id = PlanningCity.objects.filter(user_id_id=user.id)

    planning_cities = []
    for planning_citiy_id in planning_cities_id:
        planning_cities.append(City.objects.get(id=planning_citiy_id.city_id_id))

    for planningicty in planning_cities:
        planningicty.state = State.objects.get(id=planningicty.state_id_id)

    states = State.objects.all()
    cities = City.objects.all()
    data = {
        'states': states,
        'cities': cities,
        'planning_cities': planning_cities
    }
    return render(request, 'user/planning_cities.html', data)


@login_required()
def new_visited_city(request):
    user = User.objects.get(username=request.user)
    city_id = request.POST.get('city')
    city = City.objects.get(id=city_id)
    try:
        has_city = VisitedCity.objects.get(city_id_id=city_id, user_id_id=user.id)
        return redirect(visited_cities)
    except:
        visited = VisitedCity()
        visited.city_id = city
        visited.user_id = user
        visited.save()
        return redirect(visited_cities)


@login_required
def new_interested_city(request):
    user = User.objects.get(username=request.user)
    city_id = request.POST.get('city')
    city = City.objects.get(id=city_id)
    try:
        has_city = InterestedCity.objects.get(city_id_id=city_id, user_id_id=user.id)
        return redirect(interested_cities)
    except:
        interested = InterestedCity()
        interested.city_id = city
        interested.user_id = user
        interested.save()
        return redirect(interested_cities)


@login_required
def new_planning_city(request):
    user = User.objects.get(username=request.user)
    city_id = request.POST.get('city')
    city = City.objects.get(id=city_id)
    try:
        has_city = PlanningCity.objects.get(city_id_id=city_id, user_id_id=user.id)
        return redirect(planning_cities)
    except:
        planning = PlanningCity()
        planning.city_id = city
        planning.user_id = user
        planning.save()
        return redirect(planning_cities)


@login_required()
def delete_visited_city(request, id):
    user = User.objects.get(username=request.user)
    visitedcity = VisitedCity.objects.get(city_id_id=id, user_id_id=user.id)
    visitedcity.delete()
    return redirect(visited_cities)


@login_required()
def delete_interested_city(request, id):
    user = User.objects.get(username=request.user)
    interestedcity = InterestedCity.objects.get(city_id_id=id, user_id_id=user.id)
    interestedcity.delete()
    return redirect(interested_cities)


@login_required()
def delete_planning_city(request, id):
    user = User.objects.get(username=request.user)
    planningcity = PlanningCity.objects.get(city_id_id=id, user_id_id=user.id)
    planningcity.delete()
    return redirect(planning_cities)


@login_required
def get_cities(request, state_hometown):
    # state = State.objects.get(state=state_hometown)
    if is_ajax(request):
        cities = City.objects.filter(state_id_id=state_hometown).values('id', 'city')
        # data = {
        #     'cities': cities
        # }
        return JsonResponse({'data': list(cities)})
    return JsonResponse({'data': ''})


@login_required
def user_map(request):
    user = User.objects.get(username=request.user)
    # user_details = UserDetails.objects.get(user_id=user.id)
    generate_map(request)

    return render(request, f'map/{user.username}/map.html')
