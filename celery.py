from __future__ import absolute_import, unicode_literals

from celery import Celery

from config.celery import CeleryConfig

app = Celery()

app.config_from_object(CeleryConfig)


if __name__ == '__main__':
    app.start()
