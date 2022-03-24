from django.test import TestCase

# Tested in httpie

# (.venv) C:\Users\taylo\python\django\anime-jwt>http POST :8000/api/token/ username=admin password=admin
# HTTP/1.1 200 OK
# Allow: POST, OPTIONS
# Content-Length: 483
# Content-Type: application/json
# Cross-Origin-Opener-Policy: same-origin
# Date: Thu, 24 Mar 2022 03:12:29 GMT
# Referrer-Policy: same-origin
# Server: WSGIServer/0.2 CPython/3.10.3
# Vary: Accept
# X-Content-Type-Options: nosniff
# X-Frame-Options: DENY

# {
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ4MDkxODQ5LCJpYXQiOjE2NDgwOTE1NDksImp0aSI6IjgzYjE4ODY5ZmE0ODQ3NTM4Mzg3N2QzYTBmNjIxNjExIiwidXNlcl9pZCI6MX0.LnzZhIu6LgC24o6-52SGL2uaMIgYj63uYR3IKoXNL24",
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0ODE3Nzk0OSwiaWF0IjoxNjQ4MDkxNTQ5LCJqdGkiOiJiYzg1OWVhNzg3Mzk0YTA3OGI5ZjhkMTFiOWIxZWE5YyIsInVzZXJfaWQiOjF9.Lf3KZCj5pqVA0AbRTKyANOqJe8uKB4DFqp0srdsgmFk"
# }

