"""
@description: integrate with django
@author: fallenthrough
"""
import logging
from django.apps import AppConfig
from simple_background_task import BackgroundTask


class InitBackgroundConfig(AppConfig):
    name = 'simple_background_task.integrate.django'

    def ready(self):
        logging.getLogger("background_task").info("running at now!!!")
        BackgroundTask().start()
