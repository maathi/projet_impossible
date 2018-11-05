#!/usr/bin/python

import pygame
import pygame.camera
from pygame.locals import *
import time
pygame.init()
pygame.camera.init()

def snap():
	camlist = pygame.camera.list_cameras()
	if camlist:
		cam = pygame.camera.Camera(camlist[0],(320,240))
		cam.start()
		return cam.get_image()
	return None
print snap()
