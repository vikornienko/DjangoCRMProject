# https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project

DEBUG = False

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True