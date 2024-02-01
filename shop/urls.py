from django.urls import path
from .import views

urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="AboutUs"),
    path("contact/", views.contact,name="Contact"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("products/<int:myid>", views.prodView,name="ProductView"),
    path("checkout/", views.checkout,name="Checkout"),
    path("partner/", views.partner,name="PartnerUs"),
    path("handlerequest/", views.handlerequest,name="HandleRequest"),

    
    
    
]

