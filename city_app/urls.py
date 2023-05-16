from django.urls import path, include
from rest_framework import routers

from city_app.views import (PlaceViewSet, PlacesByCategory, PlacesByCity,
                            PlaceByAdressSearching, PlaceByTitleSearching)

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, 'places')
# router.register(r'by-category', PlacesByCategory, 'by_category')

urlpatterns = [
    path('', include(router.urls)),

    path('api/places/category/<int:category_id>', PlacesByCategory.as_view()),
    path('api/places/city/<int:city_id>', PlacesByCity.as_view()),

    path('api/places/adress/', PlaceByAdressSearching.as_view()),
    path('api/places/title/', PlaceByTitleSearching.as_view()),
]
