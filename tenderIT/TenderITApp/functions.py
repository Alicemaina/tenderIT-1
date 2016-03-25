import json
from django.http import HttpResponse

# Ajax login decorator
def ajax_login_required(view_function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated():
			return view_function(request, *args, **kwargs)
		output = json.dumbs({'not_authenticated': True})
		return HttpResponse(output, content_type = 'application/json')
	wrap.__doc____ = view_function.__doc__
	wrap.__dict__ =view_function.__dict__
	return wrap



