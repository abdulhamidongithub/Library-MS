from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinashga/', sinashga),
    path('', bosh_sahifa),
    path('mashq/', mashq),
    path('students/', hamma_talabalar),
    path('books/', hamma_kitoblar),
    path('talaba/<int:son>/', talaba),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('talaba_edit/<int:son>/', student_tahrirlash),
    path('talaba_tas/<int:son>/', talaba_tasdiqlash),
]


