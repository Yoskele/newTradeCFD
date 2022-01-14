from django.conf.urls import url
from django.urls import include, path, re_path

from .import views

app_name = 'website'

urlpatterns = [
	path('', views.index, name="index"),
	path('ravaror', views.ravaror, name="ravaror"),
	path('forex-valuta', views.forex, name="forex-valuta"),
	path('handla/kryptovaluta', views.krypto, name="krypto"),
	path('cfd-handel', views.cfdHandel, name="cfdHandel"),
	path('day-trading', views.dayTrading, name="dayTrading"),
	path('cfd-maklare', views.brokers, name="brokers"),
	path('handla/<slug>', views.articleDetail, name='articleDetail'),
	path('recension/<slug>', views.articleDetail, name='brokerDetail'),
	path('artikel/<slug>', views.articleDetail, name='articleDetail'),
	path('artiklar', views.articles, name='articles'),
	# path('robots.txt', views.robots_txt, name='RobotTextFile'),
]

 