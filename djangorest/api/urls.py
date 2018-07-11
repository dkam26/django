from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateShoppinglistView, DetailsView, CreateUserView

urlpatterns = {
    url(r'^shoppinglists/$', CreateShoppinglistView.as_view(), name="create"),
    url(r'^shoppinglist/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^user/$', CreateUserView.as_view(), name="createuser"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
