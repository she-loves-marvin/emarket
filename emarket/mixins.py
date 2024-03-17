
from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode

from humanfriendly import format_timespan
from django.http import JsonResponse


def FormErrors(*args):
    '''
    Handles form error that are passed back to AJAX calls
    '''
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message


class AjaxFormMixin(object):

    '''
    Mixin to ajaxify django form - can be over written in view by calling form_valid method
    '''

    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        is_ajax = self.request.headers.get('X_REQUESTED_WITH') == "XMLHttpRequest"
        if is_ajax:
            message = FormErrors(form)
            return JsonResponse({'result': 'Error', 'message': message})
        return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        is_ajax = self.request.headers.get('X_REQUESTED_WITH') == "XMLHttpRequest"
        if is_ajax:
            form.save()
            return JsonResponse({'result': 'Success', 'message': ""})
        return response


#incase mtake story za location tena. uncomment pia at models.py
# def RedirectParams(**kwargs):
# 	'''
# 	Used to append url parameters when redirecting users
# 	'''
# 	url = kwargs.get("url")
# 	params = kwargs.get("params")
# 	response = redirect(url)
# 	if params:
# 		query_string = urlencode(params)
# 		response['Location'] += '?' + query_string
# 	return response

