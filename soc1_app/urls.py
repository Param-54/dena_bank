from django.contrib import admin
from django.urls import path, include
from soc1_app import views
#from .views import date_format


urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.home, name="main"),
   path('memdetail/', views.mem_detail, name="detail"),
   path('memlist/',views.mem_list, name="list"),
   path('mem_del/<int:member_no>/',views.mem_delete, name="del"),
   path('mem_update/<int:member_no>/',views.mem_update, name="update"),
   path('do_update/<int:member_no>/',views.domem_update, name="do_update"),

   path('accad/', views.acc_add, name="accadd"),
   path('accsave/', views.account_save, name="accsave"),
   path('acclist/',views.acc_list, name="acclist"),   
   path('acc_update/<int:id>/',views.acc_update, name="accupdate"),
   path('doacc_update/<int:id>/',views.doacc_update, name="do_accupdate"),
   path('acc_del/<int:id>/',views.acc_delete, name="acc_del"),

   path('paymentad/<int:id>/', views.trans_add, name="paymentadd"),
   path('vch_edit/<int:vch_no>/', views.trans_edit, name="vch_edit"),
   path('vch_edit1/<int:vch_no_srno>/', views.trans_edit1, name="vch_edit1"),
   path('vch_sv/<int:vch_no_srno>/', views.vch_save, name="vch_sv"),

   path('intcal/', views.int_cal, name="intcal"),
   path('divcal/', views.div_cal, name="divcal"),
   path('loancal/', views.loan_cal, name="loancal"),
   
   path('intrepview/', views.int_cal_view, name="intrepview"),
   path('intviewshow/', views.int_cal_view_list, name="intviewshow"),

   path('divrepview/', views.div_cal_view, name="divrepview"),
   path('divviewshow/', views.div_cal_view_list, name="divviewshow"),

   path('loanrepview/', views.loan_cal_view, name="loanrepview"),
   path('loanviewshow/', views.loan_cal_view_list, name="loanviewshow"),

   path('shareadd/<int:id>', views.mem_share_add, name="share_add"),
   path('sharelist/',views.share_list_view, name="sharelist"),
   path('do_shupdate/<int:share_srno>/',views.share_update, name="do_shupdata"),
   path('doshare_update/<int:share_srno>/',views.doshare_update, name="do_shareupdate"), 
   path('share_del/<int:share_srno>/',views.share_delete, name="share_del"),

   path('cdlistview/', views.cd_list_view, name="cdlistview"),
   path('cdlist/', views.cd_cal, name="cdlist"),
   path('cd_listupdate/<int:mem_yrmn>/',views.cd_listupdate, name="cd_listupdate"),
   path('cd_update/<int:mem_yrmn>/',views.cd_detupdate, name="cd_update"),
   

]