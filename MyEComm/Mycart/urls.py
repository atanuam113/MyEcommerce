from . import views
from django.urls import path
from django.conf.urls.static import static
urlpatterns = [
 path("",views.index,name="ShopHome"),
 path("about/",views.about,name="aboutus"),
 path("contact/",views.contact,name="contactus"),
 path("tracker/",views.tracker,name="tracker"),
 path("search/",views.search,name="search"),
 path("productview/<int:myid>",views.productview,name="productview"),
 path("checkout/",views.checkout,name="checkout"),
 path("CategoryItem/<int:mycat>",views.CategoryItem,name ="CategoryItem"),
]