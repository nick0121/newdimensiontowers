try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError:
    pass
# SECURITY WARNING: don't run with debug turned on in production!

try:
    GET_DEBUG = os.environ["DEBUG"]

    if GET_DEBUG == "True":
        DEBUG = True
    else:
        DEBUG = False
except KeyError:
    DEBUG = True


###################### DATABASE for local development
try:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PASSWORD"],
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
except KeyError:
    pass


################# AWS ACCESS KEYS
try:
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]


except KeyError:
    pass


AWS_LOCATION = "static"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_CUSTOM_DOMAIN = "%s.s3.us-east-2.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
