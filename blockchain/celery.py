from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name)
    celery.config_from_object(app.config, namespace="CELERY")

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    celery.finalize()

    return celery
