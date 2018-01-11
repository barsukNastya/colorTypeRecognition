from django.db import models
from django.http import HttpResponseRedirect
from colorful.fields import RGBColorField
import cv2
from random import choice
from string import ascii_letters
from django.conf import settings

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
  file = models.FileField()
  coords_of_eyes = models.TextField()
  coords_of_hair =  models.TextField()
  coords_of_face = models.TextField()
  # name is random string
  name = ''.join(choice(ascii_letters) for i in range(12))


  def define_face_parameters(self):
    self.define_face()
    self.define_eyes()
    self.define_eyes_color()


  def define_face(self):
    face_cascade = cv2.CascadeClassifier(settings.STATIC_ROOT + "/xml/haarcascade_frontalface_default.xml")
    
    img = cv2.imread(self.file.path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 6)
    
    if len(detected_faces) == 1:
      detected_face = detected_faces[0]
      x_coord = detected_face[0]
      y_coord = detected_face[1]
      width = detected_face[2]
      height= detected_face[3]

      cv2.rectangle(img, (x_coord, y_coord),(x_coord + width, y_coord + height), (0,255,0), 2)
      self.crop_gray_face_image = gray_img[y_coord: y_coord + height, x_coord: x_coord + width]
      self.crop_color_face_image = img[y_coord: y_coord + height, x_coord: x_coord + width]

      cv2.imwrite(settings.MEDIA_ROOT + '/' + self.name + '.jpg', self.crop_color_face_image)
    elif len(detected_faces) == 0:
      raise Exception('Face not recognized')
    else:
      raise Exception('More than one face is recognized')

      
  def define_eyes(self):
    eyes_cascade = cv2.CascadeClassifier(settings.STATIC_ROOT + "/xml/haarcascade_eye.xml")
    eyes = eyes_cascade.detectMultiScale(self.crop_gray_face_image, scaleFactor = 1.1, minNeighbors = 6)
    for index, (ex,ey,ew,eh) in enumerate(eyes):
      self.crop_eyes_image = self.crop_gray_face_image[ey: ey + eh, ex: ex + ew]
      cv2.rectangle(self.crop_gray_face_image, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
      eyes_storage_path = settings.MEDIA_ROOT + '/' + self.name + '_' + str(index) + '.jpg'
      cv2.imwrite(eyes_storage_path, self.crop_eyes_image)


  def define_eyes_color(self):
    from color_detector import ColorDetector
    cd_green = ColorDetector('color_dataset')
    mask = cd_green.get_mask(self.crop_eyes_image)
    print(cd_green.ranges)
