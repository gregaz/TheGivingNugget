from django.shortcuts import render_to_response, get_object_or_404
from urllib import unquote
from django.http import HttpResponse
from NugAccount.models import NugAccount
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def NugAccount_give(request, NugAccount_name):
	if request.user.is_authenticated():
		return HttpResponse('You are logged in, so you can give')
	else:
		return HttpResponse('You not logged in bro')


def NugAccount_loggedInBalance(request):
	if request.user.is_authenticated():
		account = get_object_or_404(NugAccount, name=request.user.username)
		return render_to_response('balance.html',
			{
					'NugAccount' : account,
					'balance' : account.balance
					},
				)
	else:
		return HttpResponse('You not logged in bro')

def NugAccount_balance(request, NugAccount_name):
	account = get_object_or_404(NugAccount, name=unquote(NugAccount_name))
	return render_to_response('balance.html',
		{
				'NugAccount' : account,
				'balance' : account.balance
				},
			)

def NugAccount_list(request):
	r = ''
	ps = NugAccount.objects.all()
	for na in ps:
		r += na.name + ' ' + str(na.balance) + '<br/>'
	return HttpResponse(r)

def logout_view(request):
    logout(request)
    return HttpResponse('Logged out')

def am_I_logged_in(request):
	if request.user.is_authenticated():
		return HttpResponse('True')
	else:
		return HttpResponse('False')