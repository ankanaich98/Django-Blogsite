# users/middleware.py

from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import logout
import json

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')
            last_activity = timezone.now() if last_activity_str is None else timezone.datetime.fromisoformat(last_activity_str)

            if (timezone.now() - last_activity).seconds > settings.SESSION_COOKIE_AGE:
                # Session has expired, log out the user
                del request.session['last_activity']
                return self.log_out_and_redirect(request)

        # Update last activity time
        request.session['last_activity'] = timezone.now().isoformat()

        response = self.get_response(request)
        return response

    def log_out_and_redirect(self, request):
        logout(request)
        return redirect(reverse(''))  # Redirect to your login view
