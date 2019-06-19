from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^books$', views.books),
    url(r'^books/(?P<id>\d+)$', views.books_id),
    url(r'^add_book$', views.add_book),
    url(r'^authors$', views.authors),
    url(r'^add_author/$', views.add_author),
    url(r'^authors/$', views.authors_id),
]