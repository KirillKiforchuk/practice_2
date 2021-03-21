import os

env = os.environ.get

bind = '{0}:{1}'.format('0.0.0.0', env('GUNICORN_PORT', 8001))

worker_class = 'aiohttp.GunicornWebWorker'
workers = env('GUNICORN_WORKERS', 1)

keepalive = env('GUNICORN_KEEPALIVE', 4)
timeout = graceful_timeout = env('GUNICORN_TIMEOUT', 60)

errorlog = '-'
reload = True
