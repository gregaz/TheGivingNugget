from django.shortcuts import render, render_to_response, get_object_or_404
from urllib import unquote
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from NugAccount.models import UserProfile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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
			
			try:
				userToGiveTo = User.objects.get(username = usernameToGiveTo)
				userToGiveTo.userprofile.balance = int(amount) + userToGiveTo.userprofile.balance
				userToGiveTo.userprofile.save()
			except:
				return HttpResponse(usernameToGiveTo + ' does not exist :(')

			return HttpResponse('You have given ' + usernameToGiveTo + ' ' + amount +' nuggets')
	else:
		return HttpResponse('nil')

@csrf_exempt
def NugAccount_setLinkedAccount(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			return render(request, 'linkedAccount.html')
		elif request.method == 'POST':
			try:
				request.user.userprofile.linkedAccount = request.POST['linkedAccount']
				request.user.userprofile.save()
			except (KeyError):
				# Redisplay the give form.
				return render(request, 'linkedAccount.html', {
					'error_message': "You didn't input a value",
				})
			return HttpResponse('You have set the linkedAccount to ' + request.POST['linkedAccount'] )
	else:
		return HttpResponse('nil')

@csrf_exempt
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

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse('Logged out')

@csrf_exempt
def am_I_logged_in(request):
	if request.user.is_authenticated():
		return HttpResponse('True')
	else:
		return HttpResponse('False')