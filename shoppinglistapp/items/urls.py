from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateItemView, DetailsView


urlpatterns = {
    url(r'^items/$', CreateItemView.as_view(), name="createItem"),
    url(r'^item/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="itemdetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)