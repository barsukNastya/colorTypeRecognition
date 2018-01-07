from django.contrib import admin
from .models import HairColor, EyesColor, SkinColor, ColorType, Photo

admin.site.register(HairColor)
admin.site.register(EyesColor)
admin.site.register(SkinColor)
admin.site.register(ColorType)
admin.site.register(Photo)