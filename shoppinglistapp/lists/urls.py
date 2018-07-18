from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateShoppinglistView, DetailsView


urlpatterns = {
    url(r'^shoppinglists/$', CreateShoppinglistView.as_view(), name="create"),
    url(r'^shoppinglist/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)