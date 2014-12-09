__author__ = 'inozemcev'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^create/$', 'card.views.create_card', name='create_card'),
    url(r'^create/success/$', 'card.views.success_created', name='success_created'),
    url(r'^edit/(?P<card_id>\d+)/$', 'card.views.edit_card', name='edit_card'),
    url(r'^edit/success/(?P<card_id>\d+)/$', 'card.views.success_edit_card', name='success_edit_card'),
    url(r'^list/$', 'card.views.cards_list', name='cards_list'),
    url(r'^delete/(?P<card_id>\d+)/$', 'card.views.delete_card', name='delete_card'),
    url(r'^create_eptitude/(?P<card_id>\d+)/$', 'card.views.create_eptitude', name='create_eptitude'),
    url(r'^edit_eptitude/(?P<card_id>\d+)/(?P<eptitude_id>\d+)/$', 'card.views.edit_eptitude', name='edit_eptitude'),
    url(r'^create_race/(?P<card_id>\d+)/$', 'card.views.create_race', name='create_race'),
    url(r'^create_subrace/(?P<card_id>\d+)/$', 'card.views.create_subrace', name='create_subrace'),
    url(r'^create_card/$', 'card.views.create_card', name ='create_card'),
    url(r'^create_book/$', 'card.views.create_book', name ='create_book'),
    url(r'^edit_book/(?P<book_id>\d+)/$', 'card.views.edit_book', name ='edit_book'),
    url(r'^add_book_owner/(?P<book_id>\d+)/$', 'card.views.add_book_owner', name ='add_book_owner'),
    url(r'^remove_book_owner/(?P<book_id>\d+)/(?P<hero_id>\d+)/$', 'card.views.remove_book_owner', name ='remove_book_owner'),
    url(r'^books/list/$', 'card.views.books_list', name='books_list'),
    url(r'^delete_book/(?P<book_id>\d+)/$', 'card.views.delete_book', name ='delete_book'),
    url(r'^book/(?P<book_id>\d+)/$', 'card.views.book_cards', name ='book'),
    url(r'^create_card_for_book/(?P<book_id>\d+)/$', 'card.views.create_card_for_book', name ='create_card_for_book'),
    )
