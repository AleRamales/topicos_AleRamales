from django.shortcuts import render
from datetime import datetime
now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")

posts= [
    {
       'title': 'Mont Black',
       'user': {
        	'name':'Yesica Cortés',
			'Picture' : 'https://picsum.photos/200/200/?image=1036',
		},

		'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
       'title': 'Via lactea',
       'user':{
       		'name': 'Christian Van der Henst',
       		'Picture' : 'https://picsum.photos/200/200/?image=903',		
       },
       'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo': 'https://picsum.photos/800/800/?image=903'
       
    },
    {
       'title': 'Nuevo Auditorio',
       'user': {
        	'name': 'Uriel (thepianartist)',
        	'Picture': 'https://picsum.photos/60/60/?image=883'
        },
       'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo' : 'https://picsum.photos/500/700/?image=1076',
    }

]
# Create your views here.
def list_posts(request):
	return render(request, 'feed.html')