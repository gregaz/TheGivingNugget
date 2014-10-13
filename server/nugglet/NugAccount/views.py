from django.shortcuts import render, render_to_response, get_object_or_404
from urllib import unquote
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from NugAccount.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def NugAccount_give(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			return render(request, 'give.html')
		elif request.method == 'POST':
			try:
				amount = request.POST['giveamount']
			except (KeyError):
				# Redisplay the give form.
				return render(request, 'give.html', {
					'error_message': "You didn't input a value",
				})
			usernameToGiveTo = request.user.userprofile.linkedAccount
			
			userToGiveTo = User.objects.get(username = usernameToGiveTo)
			userToGiveTo.userprofile.balance = int(amount) + userToGiveTo.userprofile.balance
			userToGiveTo.userprofile.save()
		
			#try:
			#	userToGiveTo = User.objects.get(username = usernameToGiveTo)
			#	userToGiveTo.userprofile.balance = int(amount) + userToGiveTo.userprofile.balance
			#	userToGiveTo.save()
			#except:
			#	return HttpResponse(usernameToGiveTo + ' does not exist :(')

			return HttpResponse('You have given ' + usernameToGiveTo + ' ' + amount +' nuggets')
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