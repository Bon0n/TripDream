from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import City, State, VisitedCities, UserDetails
from app.services.generate_map import generate_map


def login(request):
    return render(request, 'account/login.html')


@login_required
def home(request):
    print(request.user)
    return render(request, 'user/index.html')


# def update_user(request, id):
#     userdata = User.objects.get(id=id)
#     userdata.name = request.POST.get('name')
#     userdata.username = request.POST.get('username')
#     userdata.password = request.POST.get('password')
#     userdata.hometown = request.POST.get('hometown')
#     userdata.state_hometown = request.POST.get('state_hometown')
#     userdata.regenerate_map = True
#     return redirect(user)


@login_required
def visited_cities(request):
    user = User.objects.get(username=request.user)
    visitedcities_id = VisitedCities.objects.filter(user_id_id=user.id)

    visitedcities = []
    for visitedcity_id in visitedcities_id:
        visitedcities.append(City.objects.get(id=visitedcity_id.city_id_id))

    states = State.objects.all()
    cities = City.objects.all()
    data = {
        'states': states,
        'cities': cities,
        'visited_cities': visitedcities
    }
    return render(request, 'user/visited_cities.html', data)

@login_required()
def new_visited_city(request):
    user = User.objects.get(username=request.user)
    city_id = request.POST.get('visited_city')
    city = City.objects.get(id=city_id)
    try:
        has_city = VisitedCities.objects.get(city_id_id=city_id, user_id_id=user.id)
        return redirect(visited_cities)
    except:
        visited = VisitedCities()
        visited.city_id = city
        visited.user_id = user
        visited.save()
        return redirect(visited_cities)


@login_required()
def delete_visited_city(request, id):
    user = User.objects.get(username=request.user)
    visitedcity = VisitedCities.objects.get(city_id_id=id,user_id_id=user.id)
    visitedcity.delete()
    return redirect(visited_cities)

@login_required
def user_map(request):
    user = User.objects.get(username=request.user)
    #user_details = UserDetails.objects.get(user_id=user.id)
    generate_map(request)

    return render(request, f'map/{user.username}/map.html')
