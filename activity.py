# -*- coding: utf-8 -*-

from api import get_listener_manager
from application import Application
from constants import Path
from event_manager import Event
from launcher_widget import App_widget, Notif_widget
from util import getusername, exit

__author__ = "Julien Dubois"
__version__ = "0.1.0"

from os.path import join
from pygame.locals import K_LCTRL, K_ESCAPE


class Activity(object):
    def __init__(self, view):
        self.view = view
        self.events = []

    def update(self, deltatime):
        self.view.update()

    def destroy(self):
        self.view.destroy()


class Desktop_activity(Activity):
    def __init__(self, desktop_view):
        super().__init__(desktop_view)
        self.apps = []
        self.load_apps()
        self.load_icons()
        self.initEvents()

    def initEvents(self):
        lmgr = get_listener_manager()
        event = Event(exit)
        lmgr.add_key_down_event(event, K_LCTRL, K_ESCAPE)

    def load_apps(self):
        apps = Application.get_local_apps()
        path = Path.GAMES.format(user=getusername())
        for app_path in apps:
            app = Application(app_path)
            app.load_infos()
            self.apps.append(app)

    def load_icons(self):
        for app in self.apps:
            self.view.add_widget("%s_app_icon" % app.id, App_widget, (0, 0), \
            app)

    def add_notif(self, title, msg):
        self.view.add_widget("notif", Notif_widget, (0, 0), title, msg)
