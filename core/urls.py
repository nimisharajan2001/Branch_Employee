from django.urls import re_path
from django.conf.urls.static import static

from base_app import views
from core import settings

urlpatterns = [

    
    
    re_path(r'^Superadmin_index$', views.Superadmin_index, name='Superadmin_index'),
    re_path(r'^Superadmin_Branch$', views.Superadmin_Branch, name='Superadmin_Branch'),
    re_path(r'^Superadmin_AddBranch$', views.Superadmin_AddBranch, name='Superadmin_AddBranch'),
    re_path(r'^Superadmin_Dash$', views.Superadmin_Dash, name='Superadmin_Dash'),
    re_path(r'^Superadmin_employees$', views.Superadmin_employees, name='Superadmin_employees'),
    re_path(r'^Superadmin_edepartments/(?P<id>\d+)/$', views.Superadmin_edepartments, name='Superadmin_edepartments'),
    re_path(r'^Superadmin_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?',views.Superadmin_projectman, name='Superadmin_projectman'),
    re_path(r'^Superadmin_ViewTrainers/(?P<id>\d+)/(?:(?P<did>\d+))?',views.Superadmin_ViewTrainers, name='Superadmin_ViewTrainers'),
    re_path(r'^Superadmin_View_Trainerprofile/(?P<id>\d+)/$', views.Superadmin_View_Trainerprofile, name='Superadmin_View_Trainerprofile'),
    re_path(r'^Superadmin_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.Superadmin_View_Currenttraineesoftrainer, name='Superadmin_View_Currenttraineesoftrainer'),
    re_path(r'^Superadmin_View_Currenttraineeprofile/(?P<id>\d+)/$', views.Superadmin_View_Currenttraineeprofile, name='Superadmin_View_Currenttraineeprofile'),
    re_path(r'^Superadmin_proname/(?P<id>\d+)/$', views.Superadmin_proname, name='Superadmin_proname'),
    re_path(r'^Superadmin_View_Currenttraineetasks/(?P<id>\d+)/$', views.Superadmin_View_Currenttraineetasks, name='Superadmin_View_Currenttraineetasks'),
    re_path(r'^Superadmin_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.Superadmin_ViewCurrenttraineeattendancesort, name='Superadmin_ViewCurrenttraineeattendancesort'),
    re_path(r'^Superadmin_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.Superadmin_View_Previoustraineesoftrainer, name='Superadmin_View_Previoustraineesoftrainer'),
    re_path(r'^Superadmin_View_Currenttraineeattendance/(?P<id>\d+)/$', views.Superadmin_View_Currenttraineeattendance, name='Superadmin_View_Currenttraineeattendance'),
    re_path(r'^Superadmin_View_Previoustraineeprofile/(?P<id>\d+)/$', views.Superadmin_View_Previoustraineeprofile, name='Superadmin_View_Previoustraineeprofile'),
    re_path(r'^Superadmin_View_Previoustraineetasks/(?P<id>\d+)/$', views.Superadmin_View_Previoustraineetasks, name='Superadmin_View_Previoustraineetasks'),
    re_path(r'^Superadmin_View_Previoustraineeattendance/(?P<id>\d+)/$', views.Superadmin_View_Previoustraineeattendance, name='Superadmin_View_Previoustraineeattendance'),
    re_path(r'^Superadmin_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.Superadmin_ViewPrevioustraineeattendancesort, name='Superadmin_ViewPrevioustraineeattendancesort'),
    re_path(r'^Superadmin_View_Trainerattendance/(?P<id>\d+)/$', views.Superadmin_View_Trainerattendance, name='Superadmin_View_Trainerattendance'),
    re_path(r'^Superadmin_proinvolve/(?P<id>\d+)/$', views.Superadmin_proinvolve, name='Superadmin_proinvolve'),
    re_path(r'^Superadmin_ViewTrainerattendancesort/(?P<id>\d+)/$', views.Superadmin_ViewTrainerattendancesort, name='Superadmin_ViewTrainerattendancesort'),
    re_path(r'^Superadmin_promanatten/(?P<id>\d+)/$', views.Superadmin_promanatten, name='Superadmin_promanatten'),
    re_path(r'^Superadmin_promanattendsort/(?P<id>\d+)/$', views.Superadmin_promanattendsort, name='Superadmin_promanattendsort'),
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)