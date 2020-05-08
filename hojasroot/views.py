from django.shortcuts import render
from .models import User, Community, Workplace

# Index - Autonomous Region Feed
# goal: display all communities near you. but part of a scalable map of all communities
def index (request):
    
    
    
   # communities=Community.objects
    #{'communities':communities}
    
    return render(request, 'index.html', {})




# Community Feed
# goal: display all small-scale communities and workplaces near you. limited area of map?

def community (request):

   # workplaces=Workplace.objects
   #{'workplaces':workplaces}

    return render(request, 'communityfeed.html', {})


# Community Detail
# goal: display users in community and community needs







# Workplace Detail
# goal: display users and projects and needs of workplace



# Needs Analysis Detail Feed




# Project Feed


# Project Detail


#About

def about (request):
    
    return render(request, 'about.html', {})
