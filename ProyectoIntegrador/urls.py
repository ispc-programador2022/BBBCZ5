from django.urls import path
from ProyectoIntegrador import views

urlpatterns = [
    path ( '', views.blog_inicio , name = 'blog-inicio'),
    path ( 'about/', views.blog_about , name = 'blog_about'),
    path ( 'buscar/', views.blog_buscar_pais , name = 'blog_buscar_pais'),
    path('world-data', views.importWorldPopulationData, name= 'importWorldPopulationData'),
    path('scrapping', views.scrapping, name= 'scrapping'),
    

]
