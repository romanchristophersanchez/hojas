from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Community, Workplace

# Index - Autonomous Region Feed
# goal: display all communities near you. but part of a scalable map of all communities
def index (request):
 #   so = Community(communityID='4253', city="Southbury", state='Connecticut')
  #  so.save()

   # co=User(name='Roman',email='stwrs59@gmail.com', communityID=so)
    #co.save()

 #   mo = User(name='Teresa', email='teresa@gmail.com', communityID=so)
    
  #  mo.save()


 #   users = User.objects
  #  context = {'users':users}
    
    return render(request, 'index.html', )
    




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
