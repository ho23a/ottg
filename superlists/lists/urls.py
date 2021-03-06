from django.conf.urls import include, url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name="new_list"), #no slash for POST
    # url(r'^(\d+)/add_item$', views.add_item, name="add_item"),
    # (): capture group, \d: only match digits, .: any character
    url(r'^(\d+)/$', views.view_list, name="view_list"),
    url(r'^(\d+)/items/$', views.edit_list, name="edit_list"),
    url(r'^items/(\d+)/delete_item$', views.delete_item, name="delete_item"),

]
