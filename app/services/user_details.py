from django.contrib.auth.models import User

from app.models import UserDetails


def update_user_details(request):
    user = User.objects.get(username=request.user)
    hometown = request.POST.get('hometown')
    state_hometown = request.POST.get('state_hometown')
    try:
        user_details = UserDetails.objects.get(user_id_id=user)
        user_details.hometown = hometown
        user_details.state_hometown = state_hometown
        actually_hometown = user_details.hometown
        if actually_hometown != hometown:
            user_details.regenerate_map = True
        user_details.save()
    except:
        user_details = UserDetails()
        user_details.user_id = user
        user_details.hometown = hometown
        user_details.state_hometown = state_hometown
        user_details.regenerate_map = True
        user_details.save()





