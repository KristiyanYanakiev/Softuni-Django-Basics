

from django.urls import path, include

from department.views import home_view, show_department_by_name, index, slug_view, path_view, uuid_view, \
    view_types_home_view, redirect_view, IndexView, dashboard_view, MyRedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('redirect/', MyRedirectView.as_view()),
    path('<int:pk>/', home_view, name='home'),
    path('redirect/<int:pk>/', redirect_view),


    path('view_types/', view_types_home_view),

    path('view_types/', include([
        path('<uuid:uuid>/', uuid_view),
        path('<int:id>/', index),
        path('<slug:slug>/', slug_view),
        path('<str:department_name>/', show_department_by_name),
        path('<path:path>/', path_view),
    ]))
]