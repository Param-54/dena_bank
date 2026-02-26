from django.contrib import admin
from django.urls import path, include
from soc1_app import views
#from .views import date_format


urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.mainlogin, name="main"),

   path('home/', views.home, name="home"),
   
   path('home/memdetail/', views.mem_detail, name="detail"),
   path('home/memlist/',views.mem_list, name="list"),
   path('home/mem_del/<int:member_no>/',views.mem_delete, name="del"),
   path('home/mem_update/<int:member_no>/',views.mem_update, name="update"),
   path('do_update/<int:member_no>/',views.domem_update, name="do_update"),


   path('home/accad/', views.acc_add, name="accadd"),
   path('accsave/', views.account_save, name="accsave"),
   path('home/acclist/',views.acc_list, name="acclist"),   
   path('home/acc_update/<int:id>/',views.acc_update, name="accupdate"),
   path('doacc_update/<int:id>/',views.doacc_update, name="do_accupdate"),
   path('home/acc_del/<int:id>/',views.acc_delete, name="acc_del"),

   path('home/paymentad/<int:id>/', views.trans_add, name="paymentadd"),
   path('vch_edit/<int:vch_no>/', views.trans_edit, name="vch_edit"),
   path('vch_edit1/<int:vch_no_srno>/', views.trans_edit1, name="vch_edit1"),
   path('vch_sv/<int:vch_no_srno>/', views.vch_save, name="vch_sv"),

   path('home/intcal/', views.int_cal, name="intcal"),
   path('home/divcal/', views.div_cal, name="divcal"),
   path('home/loancal/', views.loan_cal, name="loancal"),

   path('home/intcal_n/', views.int_cal_n, name="intcal_n"),

   path('home/intrepview/', views.int_cal_view, name="intrepview"),
   path('home/intviewshow/', views.int_cal_view_list, name="intviewshow"),

   path('home/divrepview/', views.div_cal_view, name="divrepview"),
   path('home/divviewshow/', views.div_cal_view_list, name="divviewshow"),

   path('home/loanrepview/', views.loan_cal_view, name="loanrepview"),
   path('home/loanviewshow/', views.loan_cal_view_list, name="loanviewshow"),

   path('home/shareadd/<int:id>', views.mem_share_add, name="share_add"),
   path('home/sharelist/',views.share_list_view, name="sharelist"),
   path('do_shupdate/<int:share_srno>/',views.share_update, name="do_shupdata"),
   path('home/doshare_update/<int:share_srno>/',views.doshare_update, name="do_shareupdate"), 
   path('share_del/<int:share_srno>/',views.share_delete, name="share_del"),

   path('home/cdlistview/', views.cd_list_view, name="cdlistview"),
   path('home/cdlist/', views.cd_cal, name="cdlist"),
   path('cd_listupdate/<int:mem_yrmn>/',views.cd_listupdate, name="cd_listupdate"),
   path('cd_update/<int:mem_yrmn>/',views.cd_detupdate, name="cd_update"),
   path('cdvchpost/', views.cd_vch_post, name="cdvchpost"),
   path('cdvchcal/', views.cd_vch_cal, name="cdvchcal"),


   path('home/mem_loan_master/', views.mem_loan_master, name="mem_loan_master"),
   path('home/mem_loan_view/', views.mem_loan_view, name="mem_loan_view"),

   path('home/mem_loan_ad/<int:member_no>/', views.mem_loan_add, name="mem_loan_ad"),
   
   path('mem_loan_sv/', views.mem_loan_mas_sv, name="mem_loan_sv"),
   
   path('home/daybook_view/', views.daybook_view, name="daybook_view"),
   path('home/daybook_show/', views.daybook_list, name="daybook_show"),
   
   path('vch_tr_edit/<int:vch_no>/', views.vch_trans_edit, name="vch_tr_edit"),
   
   path('home/ledger_view/', views.ledger_view, name="ledger_view"),
   path('home/ledger_show/', views.ledger_list, name="ledger_show"),

   path('home/trail_view/', views.trail_view, name="trail_view"),
   path('home/trail_show/', views.trail_list, name="trail_show"),
   path('home/trail_led_view/<int:trail_acc_id>/', views.trail_led_list, name="trail_led_view"),
   path('trail_show_back/', views.trail_list_back, name="trail_show_back"),
   
   path('home/mem_incl/', views.member_inclu, name="mem_incl"),
   path('home/mem_inclusion_show/', views.member_inclu_show, name="mem_inclusion_show"),

   path('home/mem_exclu/', views.member_exclu, name="mem_exclu"),
   path('home/mem_exclu_show/', views.member_exclu_show, name="mem_exclu_show"),
 
   path('home/mem_complete_list/', views.member_complete_list, name="mem_complete_list"),
   path('home/mem_complete_detail/', views.member_complete_detail, name="mem_comp_detail"),


]