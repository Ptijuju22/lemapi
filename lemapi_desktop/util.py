# -*- coding: utf-8 -*-

__author__ = "Julien Dubois"
__version__ = "0.1.0"

import copy

from lemapi.api import get_audio_player, get_gui, get_save_path
from lemapi.constants import App, Path
from lemapi.util import read_json, write_json, exit as l_exit
from lemapi.system_instance import Instance

from os.path import join


def load_settings():
	print("[lemapi] [INFO] [load_settings] Loading LemAPI settings")
	content = read_json(join(get_save_path(0), "settings.json"))

	if content:
		Instance.settings = content
	else:
		print("[lemapi] [WARNING] [load_settings] An error occurred while " \
			+ "loading LemAPI settings! Using default settings")
		Instance.settings = copy.deepcopy(App.DEFAULT_SETTINGS)


def save_settings():
	print("[lemapi] [INFO] [save_settings] Saving LemAPI settings")
	if not write_json(join(get_save_path(0), "settings.json"), Instance.settings):
		print("[lemapi] [WARNING] [save_settings] An error occurred while " \
		+ "saving LemAPI settings!")


def load_images():
	print("[lemapi] [INFO] [load_images] Loading images to RAM")
	resources = read_json(join(Path.IMAGES, "resources.json"))
	gui = get_gui()

	if resources:
		for resource in resources:
			gui.load_image(join(Path.IMAGES, *resource))
	else:
		print("[lemapi] [WARNING] [load_images] No resources.json file found!")


def load_sounds():
	print("[lemapi] [INFO] [load_sounds] Loading sounds to RAM")
	resources = read_json(join(Path.SOUNDS, "resources.json"))
	ap = get_audio_player()

	if resources:
		for resource in resources:
			ap.load_sound(join(Path.SOUNDS, *resource))
	else:
		print("[lemapi] [WARNING] [load_sounds] No resources.json file found!")


def load_musics():
	print("[lemapi] [INFO] [load_musics] Loading musics to RAM")
	resources = read_json(join(Path.MUSICS, "resources.json"))
	ap = get_audio_player()

	if resources:
		for resource in resources:
			ap.load_music(join(Path.MUSICS, *resource))
	else:
		print("[lemapi] [WARNING] [load_musics] No resources.json file found!")


def exit():
	save_settings()
	l_exit()
