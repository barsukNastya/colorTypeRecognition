from django.db import models
from django.http import HttpResponseRedirect
from colorful.fields import RGBColorField
import cv2, os
import numpy as np
from PIL import Image

class HairColor(models.Model):
  name = models.TextField()
  rgb_color = RGBColorField()
  img = models.ImageField()

class EyesColor(models.Model):
  name = models.TextField()
  rgb_color = RGBColorField()
  img = models.ImageField()

class SkinColor(models.Model):
  name = models.TextField()
  rgb_color = RGBColorField()
  img = models.ImageField()

class ColorType(models.Model):
  name = models.TextField()
  hairs_colors = models.ManyToManyField(HairColor)
  eyes_colors = models.ManyToManyField(EyesColor)
  skins_colors = models.ManyToManyField(SkinColor)


class Photo(models.Model):
  file_field = models.FileField()
  coords_of_eyes = models.TextField()
  coords_of_hair =  models.TextField()
  coords_of_face = models.TextField()

  def define_eyes_color(self):
    pass

  def define_face(self, uploaded_photo):
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    recognizer = cv2.createLBPHFaceRecognizer(1,8,8,8,123)

    gray = Image.open(uploaded_photo).convert('L')
    image = np.array(gray, 'uint8')
    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    cv2.imshow("", image[y: y + h, x: x + w])
    cv2.waitKey(50)