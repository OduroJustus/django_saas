from decouple import config

print("Email Settings Test:")
print(f"EMAIL_HOST: {config('EMAIL_HOST', default='smtp.gmail.com')}")
print(f"EMAIL_PORT: {config('EMAIL_PORT', default='587')}")
print(f"EMAIL_HOST_USER: {config('EMAIL_HOST_USER', default='Not Set')}")
print(f"EMAIL_HOST_PASSWORD: {'Set' if config('EMAIL_HOST_PASSWORD', default=None) else 'Not Set'}")
print(f"EMAIL_USE_TLS: {config('EMAIL_USE_TLS', default=True, cast=bool)}")

