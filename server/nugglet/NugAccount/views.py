from django.shortcuts import render, render_to_response, get_object_or_404
from urllib import unquote
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from NugAccount.models import UserProfile

# Create your views here.
def NugAccount_give(request):
	if request.user.is_authenticated():
		try:
			amount = request.POST['giveamount']
		except (KeyError):
			# Redisplay the give form.
			return render(request, 'give.html', {
				'error_message': "You didn't input a value",
			})
		return HttpResponse('You are logged in, so you can give')
	else:
		return HttpResponse('nil')


def NugAccount_loggedInBalance(request):
	if request.user.is_authenticated():
		return render_to_response('balance.html',
			{
					'NugAccount' : request.user.userprofile.balance,
					'balance' : request.user.userprofile.balance
					},
				)
	else:
		return HttpResponse('nil')

def logout_view(request):
    logout(request)
    return HttpResponse('Logged out')

def am_I_logged_in(request):
	if request.user.is_authenticated():
		return HttpResponse('True')
	else:
		return HttpResponse('False')