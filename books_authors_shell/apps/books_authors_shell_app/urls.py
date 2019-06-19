from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^book/(?P<id>\d+)$', views.book_description),
    url(r'^add_book$', views.add_book),
    url(r'^authors$', views.authors),
    url(r'^create_authors$', views.create_author),
    url(r'^add_author/$', views.add_author),
    url(r'^author/(?P<id>\d+)$', views.author_description),
    url(r'^add_author_to_book$', views.add_author_to_book),
]