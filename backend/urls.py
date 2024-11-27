from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/submit-form/",
        views.submit_form,
        name="patient_create_view",
    ),
    path('api/post-comment/',
          views.post_comment,
            name='post_comment_view'),
    path('api/comments/', views.get_comments, name='get_comments'),
    path('api/prescriptions/', views.get_prescriptions, name='get_prescriptions'),
    path('api/deliveryinfo/', views.get_deliveryinfo, name='get_deliveryinfo'),
    path('api/', include('app.urls')),
    path('', RedirectView.as_view(url='/admin/')),
    path('api/auth/', include('app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
