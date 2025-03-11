from xml.dom.minidom import Document
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from soc1_app.models import member_detail,acc_group,account_head,vch_type,vch_trans,vch_control,vch_control_srno,mem_share_detail,int_cal_controll,div_cal_controll,loan_cal_controll,loan_repayment_sch,cd_cal_controll,cd_mem_list,loan_master
from datetime import date
import decimal
from django.core.paginator import Paginator

#from soc1_app.models import DateModel

# Create your views here.

def home(request):
    return render(request,'base.html')

def mem_detail(request):
        if request.method == 'POST':
            v_acc_name = request.POST['acc_name']
            v_opbal = request.POST['mem_opbal']
            v_grp_id = request.POST['group']   
            v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name
            
            acc_check =  account_head.objects.filter(acc_name=v_acc_name).exists()
#            print(acc_check)
            if not acc_check :
#                print("acc vipul")
                mymem = account_head(acc_name = v_acc_name, grp_id_id = v_grp_id , op_bal = v_opbal, grp_nm = v_grp_name)
                mymem.save()


            v_acc_id=account_head.objects.get(acc_name=v_acc_name).id

            v_mem_no = request.POST['mem_no']
            v_mem_name = request.POST['mem_name']
            v_mem_add = request.POST['mem_add']
            v_dob = request.POST['mem_dob']
            v_phone=request.POST['mem_phone']
            v_addhar=request.POST['mem_addhar']
            v_panno=request.POST['mem_pan']
            v_passport_no=request.POST['mem_Pass']
            v_bank_name=request.POST['mem_bank']
            v_bank_account=request.POST['mem_bankaccount']
            v_bank_ifsc=request.POST['mem_ifsc']
            v_nominee=request.POST['mem_nominee']
            v_nominee_phone=request.POST['mem_nomineephone']
            v_no_of_children=request.POST['mem_children']
            v_msex = request.POST['msex']
            if int(v_msex) == 1 :
                v_sex_val = 'Male'
            else :
                 v_sex_val= 'Female'

            mymem = member_detail(member_no = v_mem_no, name = v_mem_name, address = v_mem_add, dob =v_dob, phone = v_phone,
                                    addhar= v_addhar, panno =v_panno, passport_no =v_passport_no, bank_name = v_bank_name, bank_account = v_bank_account,
                                    bank_ifsc = v_bank_ifsc, nominee = v_nominee, nominee_phone =v_nominee_phone , no_of_children = v_no_of_children,acc_name = v_acc_name,
                                    op_bal  = v_opbal, grp_id_id = v_grp_id, grp_nm = v_grp_name, acc_id = v_acc_id,mem_sex = v_msex,mem_sex_val = v_sex_val)
            mymem.save()

        grp_data=acc_group.objects.all()
        mem_data=member_detail.objects.all()
        acc_detail=account_head.objects.all()
        dt=date.today()    
        return render(request,'Member_detail_new.html', {'grp_data':grp_data,'mem_data':mem_data,'acc_detail':acc_detail,'v_dt':dt})

def mem_list(request):
    mem_data =member_detail.objects.order_by("name")
    rec_cnt=member_detail.objects.order_by("name").count()
    return render(request,'member_list.html',{'mem_data':mem_data})

def mem_delete(request,member_no):
    mem_data = member_detail.objects.get(pk=member_no)
    mem_data.delete()
    return redirect('/memlist/')
    # return render(request,'member_list.html')

def mem_update(request,member_no):
    mem_data =member_detail.objects.get(pk=member_no)   
    grp_data=acc_group.objects.all()

    return render(request,'member_update.html',{'grp_data':grp_data,'mem_data':mem_data})

def domem_update(request,member_no):
    v_mem_no = request.POST.get('mem_no')
    v_mem_name = request.POST.get('mem_name')
    v_mem_add = request.POST.get('mem_add')
    v_dob = request.POST.get('mem_dob')
    v_phone=request.POST.get('mem_phone')
    v_addhar=request.POST.get('mem_addhar')
    v_panno=request.POST.get('mem_pan')
    v_passport_no=request.POST.get('mem_Pass')
    v_bank_name=request.POST.get('mem_bank')
    v_bank_account=request.POST.get('mem_bankaccount')
    v_bank_ifsc=request.POST.get('mem_ifsc')
    v_nominee=request.POST.get('mem_nominee')
    v_nominee_phone=request.POST.get('mem_nomineephone')
    v_no_of_children=request.POST.get('mem_children')
    v_opbal = request.POST['mem_opbal']
    mem_data =member_detail.objects.get(pk=member_no)
  
    mem_data.member_no = v_mem_no
    mem_data.name = v_mem_name
    mem_data.address = v_mem_add
    mem_data.dob = v_dob 
    mem_data.phone = v_phone
    mem_data.addhar = v_addhar
    mem_data.panno = v_panno
    mem_data.passport_no = v_passport_no
    mem_data.bank_name = v_bank_name
    mem_data.bank_account = v_bank_account
    mem_data.bank_ifsc = v_bank_ifsc
    mem_data.nominee = v_nominee
    mem_data.nominee_phone = v_nominee_phone
    mem_data.no_of_children = v_no_of_children
    mem_data.op_bal= v_opbal
    mem_data.save()
    
    return redirect('/memlist/')

def acc_add(request):
    grp_data=acc_group.objects.all()
    dt=date.today()
    return render(request,'acc_detail.html',{'grp_data':grp_data,'v_dt':dt})



def account_save(request):
    if request.method == 'POST':
          v_acc_name = request.POST['acc_name']
          v_opbal = request.POST['acc_opbal']
          v_grp_id = request.POST['group']   
          v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name
          acc_check =  account_head.objects.filter(acc_name=v_acc_name).exists()
#            print(acc_check)
          if not acc_check :
              mymem = account_head(acc_name = v_acc_name, grp_id_id = v_grp_id , op_bal = v_opbal, grp_nm = v_grp_name)
              mymem.save()
    
    grp_data=acc_group.objects.all()
    return render(request,'acc_detail.html',{'grp_data':grp_data})

def acc_list(request):
    vacc_data = account_head.objects.order_by("acc_name")
    return render(request,'acc_list.html',{'acc_data': vacc_data})

def acc_update(request,id):
    grp_data=acc_group.objects.all()
    acc_data =account_head.objects.get(id=id) 
    return render(request,'acc_edit.html',{'acc_data':acc_data,'grp_data':grp_data})

def doacc_update(request,id):
      if request.method == 'POST':
          v_acc_name = request.POST['acc_name']
          v_opbal = request.POST['acc_opbal']
          v_grp_id = request.POST['group']   
          v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name
          
          acc_data =account_head.objects.get(id=id)
          
          acc_data.acc_name=v_acc_name
          acc_data.op_bal=v_opbal
          acc_data.grp_id_id=v_grp_id
          acc_data.grp_nm=v_grp_name
          acc_data.save()
          vacc_data = account_head.objects.order_by("acc_name")
          return render(request,'acc_list.html',{'acc_data': vacc_data})

def acc_delete(request,id):
    vacc_data = account_head.objects.get(pk=id)
    vacc_data.delete()
    return redirect('/acclist/')

def trans_add(request,id):
    # Voucher No generation code
    trty_data=vch_type.objects.get(trans_type=id)
    v_vch_control=vch_control.objects.get(pk=id)
    v_no = v_vch_control.st_no+1
    v_vch_control.st_no=v_no
    v_vch_control.save()
    
    vch_control_srno(tr_type = id , st_no =v_no,stsr_no =  0).save()
    v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
    v_sr = v_vch_control_srno.stsr_no+1
    
    v_vch_control_srno.stsr_no=v_sr
    v_vch_control_srno.save()
    
    v_srno_1 = (v_no*1000)+v_sr
    #End Voucher Generation code

    acc_data=account_head.objects.all()
    dt=date.today()  

    vch_trans(trans_type = id, vch_no = v_no, vch_no_srno = v_srno_1, vch_date = dt,srno = v_sr).save()
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
    v_trans_detail=vch_trans.objects.filter(vch_no = v_no)
    return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans,'v_trans_detail':v_trans_detail,'sv_ty':1})


def trans_edit(request,vch_no):
    cnt=vch_trans.objects.filter(vch_no=vch_no).count()
    v_cn_val = request.POST['cn_val']

    if int(v_cn_val) == 3 :
            v_vch_no_srno_2 = request.POST['vch_no_2']
            
    vv_cn_val=v_cn_val
    cnt=vch_trans.objects.filter(vch_no=vch_no).count()

    
    if int(v_cn_val) > 3 : 
        v_srno_1 = (vch_no*1000)+1
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        tr_ty=v_trans.trans_type
        dt=v_trans.vch_date
        tr_ty=v_trans.trans_type
        v_vchno=v_trans.vch_no
        trty_data=vch_type.objects.get(trans_type=tr_ty)
        acc_data=account_head.objects.all()
        v_trans_detail=vch_trans.objects.filter(vch_no_srno = vv_cn_val)
    else :        
        v_srno_1 = (vch_no*1000)+1
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        tr_ty=v_trans.trans_type

        v_dt = request.POST['mem_dob']
        v_acc_id = request.POST['acc_name']
        v_vch_no_srno =  request.POST['vch_no']
        acc_data=account_head.objects.get(id=v_acc_id)

        ac_name=acc_data.acc_name
        v_trans.vch_date = v_dt 
        v_trans.vch_acc_id = v_acc_id
        v_trans.vch_acc_head= ac_name

        if (tr_ty == 1 and cnt == 1) :
            v_trans.vch_dc="D"
            v_trans.save()
        if (tr_ty == 2 and cnt == 1) :
            v_trans.vch_dc="C"
            v_trans.save()
        if (tr_ty == 3 and cnt == 1) :
            v_trans.vch_dc="C"
            v_trans.save()

        if cnt>1 :
                v_vch_no_srno_2 = request.POST['vch_no_2']
                v_acc_id_2 = request.POST['acc_name1']
                v_acc_opbal =request.POST['acc_opbal']
                acc_data=account_head.objects.get(id=v_acc_id_2)
                ac_name2=acc_data.acc_name
                v_trans=vch_trans.objects.get(vch_no_srno=v_vch_no_srno_2)
                
                v_trans.vch_date = v_dt 
                v_trans.vch_acc_id = v_acc_id_2
                v_trans.vch_acc_head = ac_name2
                v_trans.vch_amt = v_acc_opbal
                if tr_ty == 1  :
                    v_trans.vch_dc="C"
                    v_trans.save()
                if tr_ty == 2  :
                    v_trans.vch_dc="D"
                    v_trans.save()
                if tr_ty == 3  :
                    v_trans.vch_dc="D"
                    v_trans.save()

        else :
                pass
                
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        dt=v_trans.vch_date
        tr_ty=v_trans.trans_type
        v_vchno=v_trans.vch_no

        v_trans1=vch_trans.objects.filter(vch_no=v_vchno)
        v_amt=0.0
        for x in v_trans1 :
            if (x.vch_no_srno-(x.vch_no*1000))>1 :
                    amt =x.vch_amt
                    v_amt = v_amt + amt

        trty_data=vch_type.objects.get(trans_type=tr_ty)
        acc_data=account_head.objects.all()

        v_srno_1 = (v_vchno*1000)+1
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        v_trans.vch_amt = v_amt
        v_trans.save()
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)

#        print(v_cn_val)
            
        if (int(v_cn_val) == 1) :
#                print("vipul")
                v_vch_control_srno = vch_control_srno.objects.get(pk =v_vchno)
                v_sr = v_vch_control_srno.stsr_no+1
                v_vch_control_srno.stsr_no=v_sr
                v_vch_control_srno.save()
                v_srno_2 = (v_vchno*1000)+v_sr
                vch_trans(trans_type = tr_ty, vch_no = v_vchno, vch_no_srno = v_srno_2, vch_date = dt,srno = v_sr).save()
                
        v_trans_detail=vch_trans.objects.filter(vch_no = v_vchno)

    return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans,'v_trans_detail':v_trans_detail, 'v_dt':dt,'v_no':v_vchno,'v_srno_1':v_srno_1})


def trans_edit1(request,vch_no):
#    print("edit1")
#    print(vch_no)
    v_trans_detail=vch_trans.objects.get(vch_no_srno=vch_no)

#    print(v_trans_detail)

    v_srno_1 = (v_trans_detail.vch_no*1000)+1
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
    tr_ty=v_trans.trans_type
    trty_data=vch_type.objects.get(trans_type=tr_ty)
    acc_data=account_head.objects.all()
#    print(vch_no)

    return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans,'v_trans_detail':v_trans_detail})


def vch_save(request,vch_no):
    cnt=vch_trans.objects.filter(vch_no=vch_no).count()
    v_srno_1 = (vch_no*1000)+1
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
    tr_ty=v_trans.trans_type

    v_dt = request.POST['mem_dob']
    v_acc_id = request.POST['acc_name']
    v_vch_no_srno =  request.POST['vch_no']
    acc_data=account_head.objects.get(id=v_acc_id)
    ac_name=acc_data.acc_name

    v_trans.vch_date = v_dt 
    v_trans.vch_acc_id = v_acc_id
    v_trans.vch_acc_head = ac_name
    if (tr_ty == 1 and cnt == 1) :
       v_trans.vch_dc="D"
    v_trans.save()

    if cnt>1 :
         v_vch_no_srno_2 = request.POST['vch_no_2']
         v_acc_id_2 = request.POST['acc_name1']
         v_acc_opbal =request.POST['acc_opbal']
         acc_data=account_head.objects.get(id=v_acc_id_2)
         ac_name2=acc_data.acc_name
         v_trans=vch_trans.objects.get(vch_no_srno=v_vch_no_srno_2)
         v_trans.vch_date = v_dt 
         v_trans.vch_acc_id = v_acc_id_2
         v_trans.vch_acc_head = ac_name2
         v_trans.vch_amt = v_acc_opbal

         if tr_ty == 1  :
              v_trans.vch_dc="C"
         v_trans.save()

    else :
        pass
        
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
    dt=v_trans.vch_date
    tr_ty=v_trans.trans_type
    v_vchno=v_trans.vch_no

    v_trans1=vch_trans.objects.filter(vch_no=v_vchno)
    v_amt=0.0
    for x in v_trans1 :
        if (x.vch_no_srno-(x.vch_no*1000))>1 :
            amt =x.vch_amt
            v_amt = v_amt + amt
            
    
    trty_data=vch_type.objects.get(trans_type=tr_ty)
    acc_data=account_head.objects.all()

    v_srno_1 = (v_vchno*1000)+1
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
    v_trans.vch_amt = v_amt
    v_trans.save()
    v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)

    # v_vch_control_srno = vch_control_srno.objects.get(pk =v_vchno)
    # v_sr = v_vch_control_srno.stsr_no+1
    # v_vch_control_srno.stsr_no=v_sr
    # v_vch_control_srno.save()
    # v_srno_2 = (v_vchno*1000)+v_sr

    # vch_trans(trans_type = tr_ty, vch_no = v_vchno, vch_no_srno = v_srno_2, vch_date = dt).save()

    v_trans_detail=vch_trans.objects.filter(vch_no = v_vchno)
    return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans,'v_trans_detail':v_trans_detail})


    # print("vipul")
    # trty_data=vch_type.objects.all()
    # acc_data=account_head.objects.all()
    # # tr_ty = Document.getElementById('tr_id').value
    # tr_ty=trty_data.trans_type

    # print(id)
    # mvch_no=5
    # rec_cheK=vch_trans.objects.filter(vch_no=mvch_no,trans_type=1).exists()
    # if  rec_cheK:
    #     pass
    # else:
    #     vch_trans.objects.create(vch_no=mvch_no,trans_type=1)

    # v_trans=vch_trans.objects.all()

    # return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans})

def int_cal(request):
        if request.method == 'POST':
            v_acc_id = request.POST['acc_name']
            v_int_month = request.POST['int_month']
            v_int_year = request.POST['int_year']
            v_int_rate = request.POST['int_rate']
            m_yrmn=int(v_int_year)*100+int(v_int_month)
#            print(m_yrmn)
            rec_cheK=int_cal_controll.objects.filter(yrmn=m_yrmn).exists()
            if not rec_cheK :
#                    print(rec_cheK)
                    days=30
                    leap = 0
                    if int(v_int_year) % 400 == 0:
                        leap = 1
                    elif int(v_int_year) % 100 == 0:
                        leap = 0
                    elif int(v_int_year) % 4 == 0:
                        leap = 1
                    if int(v_int_month) == 2:
                        days = 28 + leap

                    v_month=int(v_int_month)    
                    m_list = [1,3,5,7,8,10,12]
                    if v_month in m_list:
                        days = 31

#                    print(days)
#                    print(v_int_month)
                    
                    v_dt = date(int(v_int_year), int(v_int_month), days)
#                   print(v_dt.strftime("%m"))
#                   print(v_dt)
            
                    acc_data1=account_head.objects.get(id=v_acc_id)
                    ac_name=acc_data1.acc_name        

                    # Voucher No generation code
                    trty_data=vch_type.objects.get(trans_type=3)
                    v_vch_control=vch_control.objects.get(pk=3)
                    v_no = v_vch_control.st_no+1
                    v_vch_control.st_no=v_no
                    v_vch_control.save()
                    
                    vch_control_srno(tr_type = 3 , st_no =v_no,stsr_no =  0).save()
                    v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                    v_sr = v_vch_control_srno.stsr_no+1
                    
                    v_vch_control_srno.stsr_no=v_sr
                    v_vch_control_srno.save()
                    
                    v_srno_1 = (v_no*1000)+v_sr
                    #End Voucher Generation code

                    vch_trans(trans_type = 3, vch_no = v_no, vch_no_srno = v_srno_1, vch_date = v_dt, vch_acc_head = ac_name, vch_acc_id = v_acc_id, vch_dc = "D", vch_amt = 0, srno = v_sr ).save()
                    int_cal_controll.objects.create(yrmn=m_yrmn,int_rt=v_int_rate,tr_type = 3,vch_no=v_no )

                    mem_det = member_detail.objects.filter()

                    vch_amt_d=0
                    for mem in mem_det :
                        mem_acc_id=mem.acc_id
                        if mem_acc_id != None :
     #                       print(mem_acc_id)
                            mem_acc_data=account_head.objects.get(id=mem_acc_id)
                            mem_acc_name=mem_acc_data.acc_name
                            mem_opbal=mem_acc_data.op_bal
                            v_trans1=vch_trans.objects.filter(vch_acc_id=mem_acc_id)  
                            for vch_data in v_trans1 :
                                if  vch_data.vch_date <= v_dt :
                                    # print(vch_data.vch_date)
                                    # print(v_dt)
                                    if vch_data.vch_dc == "D":
                                        mem_opbal = mem_opbal - vch_data.vch_amt
                                    else:
                                        mem_opbal = mem_opbal + vch_data.vch_amt
      #                      print(mem_opbal)
                            if mem_opbal > 0 :
                                mem_int_amt = round(((float(mem_opbal) * float(v_int_rate)) / 100),0)
                                v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                                v_sr = v_vch_control_srno.stsr_no+1
                                v_vch_control_srno.stsr_no=v_sr
                                v_vch_control_srno.save()
                                v_srno_2 = (v_no*1000)+v_sr
                            
                                vch_amt_d =vch_amt_d + mem_int_amt

                                vch_trans(trans_type = 3, vch_no = v_no, vch_no_srno = v_srno_2, vch_date = v_dt, vch_acc_head = mem_acc_name, vch_acc_id = mem_acc_id, vch_dc = "C", vch_amt = mem_int_amt,srno = v_sr).save()

                                v_srno_1 = (v_no*1000)+1
                                # print(vch_amt_d)
                                # print(v_srno_1)
                                v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
                                v_trans.vch_amt = vch_amt_d
                                v_trans.save()

        acc_data=account_head.objects.all()
        return render(request,'interest_cal.html',{'acc_data':acc_data})


def div_cal(request):
        if request.method == 'POST':
            v_acc_id = request.POST['acc_name']
            v_int_year = request.POST['int_year']
            v_int_rate = request.POST['int_rate']
#            print(m_yrmn)
            rec_cheK=div_cal_controll.objects.filter(yrmn=v_int_year).exists()
            if not rec_cheK :
                    v_dt = date(int(v_int_year), 3, 31)
                    st_dt = date((int(v_int_year)-1),4,1)
                    acc_data1=account_head.objects.get(id=v_acc_id)
                    ac_name=acc_data1.acc_name        
                    # Voucher No generation code
                    trty_data=vch_type.objects.get(trans_type=3)
                    v_vch_control=vch_control.objects.get(pk=3)
                    v_no = v_vch_control.st_no+1
                    v_vch_control.st_no=v_no
                    v_vch_control.save()
                    vch_control_srno(tr_type = 3 , st_no =v_no,stsr_no =  0).save()
                    v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                    v_sr = v_vch_control_srno.stsr_no+1
                    v_vch_control_srno.stsr_no=v_sr
                    v_vch_control_srno.save()
                    v_srno_1 = (v_no*1000)+v_sr
                    #End Voucher Generation code
                    vch_trans(trans_type = 3, vch_no = v_no, vch_no_srno = v_srno_1, vch_date = v_dt, vch_acc_head = ac_name, vch_acc_id = v_acc_id, vch_dc = "D", vch_amt = 0, srno = v_sr ).save()
                    div_cal_controll.objects.create(yrmn=v_int_year,int_rt=v_int_rate,tr_type = 3,vch_no=v_no )
                    mem_det = member_detail.objects.all()
                    vch_amt_d=0
                    for mem in mem_det :
                        mem_acc_id=mem.acc_id
                        v_mem_no= mem.member_no
                        if mem_acc_id != None :
        #                    print(mem_acc_id)
                            mem_acc_data=account_head.objects.get(id=mem_acc_id)
                            mem_acc_name=mem_acc_data.acc_name
                            mem_share_det = mem_share_detail.objects.filter(mem_no=v_mem_no)
                            mem_share_opbal = 0
                            mem_div_amt = 0
#                            v_trans1=vch_trans.objects.filter(vch_acc_id=mem_acc_id)  
                            for share_data in mem_share_det :
                                if  share_data.det_date < st_dt :
                                    mem_share_opbal = mem_share_opbal + share_data.no_of_share
                                elif share_data.det_date >= st_dt :
                                    m_month = int(share_data.det_date.strftime("%m"))
                                    if m_month >= 4 :
                                           m_mn_cal= 13- int(m_month) + 3
                                    else:
                                           m_mn_cal = int(m_month)
                                    mem_div_amt = mem_div_amt + round((float(int(share_data.no_of_share) * (float(v_int_rate)/12) * m_mn_cal)/100),0)
#                                   print(m_mn_cal)
#                                   print(share_data.no_of_share)
#                                   print(round(mem_div_amt,2))
                            mem_div_amt = mem_div_amt + (float(mem_share_opbal) * float(v_int_rate)) / 100
                            if mem_div_amt > 0 :
                                 
                                v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                                v_sr = v_vch_control_srno.stsr_no+1
                                v_vch_control_srno.stsr_no=v_sr
                                v_vch_control_srno.save()
                                v_srno_2 = (v_no*1000)+v_sr
                                vch_amt_d =vch_amt_d + round(mem_div_amt,2)
                                vch_trans(trans_type = 3, vch_no = v_no, vch_no_srno = v_srno_2, vch_date = v_dt, vch_acc_head = mem_acc_name, vch_acc_id = mem_acc_id, vch_dc = "C", vch_amt = mem_div_amt, srno = v_sr).save()
                                v_srno_1 = (v_no*1000)+1
                                # print(vch_amt_d)
                                # print(v_srno_1)
                                v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
                                v_trans.vch_amt = vch_amt_d
                                v_trans.save()

        acc_data=account_head.objects.all()
        return render(request,'div_cal.html',{'acc_data':acc_data})

def loan_cal(request):
        error_msg=""
        if request.method == 'POST':
            v_mem_no       =  request.POST['mem_name']
            v_loan_amt     = request.POST['loan_amt']
            v_loan_Month   = request.POST['loan_Month']
            v_int_rate     = request.POST['int_rate']
            loan_date      = request.POST['loan_stdt']
            v_acc_id       = request.POST['acc_name']
#            v_grp_id       = request.POST['group'] 

#            print(v_mem_no)
            v_mem_name  = member_detail.objects.get(member_no=v_mem_no).name
#            print(v_mem_name)
            # v_mem_no = mem_dt.member_no

            rec_cheK=loan_cal_controll.objects.filter(mem_no=v_mem_no).exists()
            if not rec_cheK :
#                     acc_check=account_head.objects.filter(acc_name=v_acc_name).exists() 
#                     print(acc_check)
                     acc_check=account_head.objects.get(id=v_acc_id)
                     v_acc_name = acc_check.acc_name
                     v_grp_id = acc_check.grp_id_id
                     v_grp_name = acc_check.grp_nm
#        
#                     if not acc_check :
#                        print("vipul")
#                        v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name
#                        mymem = account_head(acc_name = v_acc_name, grp_id_id = v_grp_id ,  grp_nm = v_grp_name)
#                        mymem.save()
#                     print("jain")

#                     v_acc_id = account_head.objects.get(acc_name = v_acc_name).id
#                     v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name

#                     print(v_acc_id)
                     # Loan Account  generation code
                     trty_data=vch_type.objects.get(trans_type=8)
                     v_vch_control=vch_control.objects.get(pk=8)
                     v_no = v_vch_control.st_no+1
                     v_vch_control.st_no=v_no
                     v_vch_control.save()
            #         #End loan account Generation code
                     loan_cal_controll.objects.create(loan_ac_no=v_no,mem_no = v_mem_no, st_date = loan_date,tr_type = 8 ,mem_name = v_mem_name ,
                                                     vch_no=v_no,loan_amt = v_loan_amt, loan_mnth = v_loan_Month, int_rt=v_int_rate,mem_acc_id = v_acc_id,
                                                     mem_acc_name = v_acc_name, acc_grp_id = v_grp_id,  acc_grp_nm = v_grp_name, loan_status = 1 )
       
                     loan_det = loan_cal_controll.objects.get(loan_ac_no = v_no)
                     re_loan_mnth = int(loan_det.loan_mnth)
                     re_loan_ac_no = loan_det.loan_ac_no

                     m_month = int(loan_det.st_date.strftime("%m"))
                     m_year = int(loan_det.st_date.strftime("%Y"))
                     m_day = int(loan_det.st_date.strftime("%d"))
                    
                     re_st_date = loan_det.st_date
                     re_mem_no = loan_det.mem_no
                     re_mem_name = loan_det.mem_name
                     re_openning_loan_amt = loan_det.loan_amt
                     re_balance_loan_amt = re_openning_loan_amt
                     re_int_amt = 0
                     re_loan_int_amt=0
                     re_int_rt = loan_det.int_rt/12
                     re_principal_amt= round((re_openning_loan_amt/loan_det.loan_mnth),0)
                     re_mem_acc_id = loan_det.mem_acc_id
                     re_mem_acc_name = loan_det.mem_acc_name
#                     print(re_balance_loan_amt)
#                     print(re_int_rt)
                     for x in range(re_loan_mnth):
#                        re_int_amt = re_int_amt + round(((re_balance_loan_amt*re_int_rt)/100),2)
#                        re_int_amt = round(((re_balance_loan_amt*re_int_rt)/100),0)
                        re_int_amt = 1400
                        re_balance_loan_amt = re_balance_loan_amt - re_principal_amt
                        re_loan_int_amt = re_loan_int_amt + re_int_amt
 #                       print(re_loan_int_amt)
 
#                     re_loan_int_amt = round(re_int_amt/re_loan_mnth)
#                     re_emi_amt = re_principal_amt + re_loan_int_amt
                        re_emi_amt = re_principal_amt + re_int_amt
#                     for x in range(re_loan_mnth):
                        re_loan_ac_no_srno = ((re_loan_ac_no*1000)+(x+1))
  
                        if m_month >= 12 and m_day>=20:
                             m_month=1
                             m_year= m_year + 1 
                        else :
                            if m_day<=15:
                              m_day=20
                            else:
                              m_month = m_month + 1
                    
                        re_pay_date = date(m_year, m_month, 5)

                        m_yrmn=int(m_year)*100+int(m_month)

                        if x > 0 :
                            re_openning_loan_amt = re_openning_loan_amt - re_principal_amt
                        
                        loan_repayment_sch.objects.create(loan_ac_no_srno = re_loan_ac_no_srno,Loan_no = re_loan_ac_no,repayment_date = re_pay_date,
                                                          st_date = re_st_date, tr_type = 8, mem_no = re_mem_no,mem_name = re_mem_name, 
                                                          openning_loan_amt = re_openning_loan_amt,emi_amt = re_emi_amt, loan_int_amt = re_int_amt, 
                                                          monthly_prinipal_amt_deduction = re_principal_amt,loan_mnth = re_loan_mnth, int_rt = re_int_rt, emi_paid = 1 ,
                                                            mem_acc_id = re_mem_acc_id,mem_acc_name = re_mem_acc_name, yrmn = m_yrmn)
#                        loan_int_amt = re_loan_int_amt,
#                    loan_repayment_sch.objects.create(loan_ac_no_srno = re_loan_ac_no_srno,Loan_no = re_loan_ac_no,repayment_date = re_pay_date)               
            else :
                     error_msg="Loan Already processed"

#        print(error_msg)
        dt=date.today()    
        grp_data=acc_group.objects.all()
        acc_detail=account_head.objects.all()
        mem_det = member_detail.objects.all()
        return render(request,'loan_cal.html',{'mem_det':mem_det,'grp_data':grp_data,'acc_data':acc_detail,'v_dt':dt,'msg':error_msg})

def int_cal_view(request):
    int_cnt_data = int_cal_controll.objects.all()
    return render(request,'int_vch_view.html',{'int_cnt_data': int_cnt_data})

def int_cal_view_list(request):
    if request.method == 'POST':
        v_yrnm     = request.POST['acc_name']
        v_int_data = int_cal_controll.objects.get(yrmn = v_yrnm)
        v_vch_no= v_int_data.vch_no
        v_trans = vch_trans.objects.filter(vch_no= v_vch_no)
    return render(request,'int_vch_show.html',{'int_v_trans': v_trans})

def div_cal_view(request):
    div_cnt_data = div_cal_controll.objects.all()
    return render(request,'div_vch_view.html',{'div_cnt_data': div_cnt_data})

def div_cal_view_list(request):
    if request.method == 'POST':
        v_yrnm     = request.POST['acc_name']
       # print(v_yrnm)
        v_int_data = div_cal_controll.objects.get(yrmn = v_yrnm)
       # print(v_int_data)
        v_vch_no= v_int_data.vch_no
       # print(v_vch_no)
        v_trans = vch_trans.objects.filter(vch_no= v_vch_no)
    return render(request,'div_vch_show.html',{'div_v_trans': v_trans})

def loan_cal_view(request):
    loan_cnt_data = loan_cal_controll.objects.all()
    return render(request,'loan_vch_view.html',{'loan_cnt_data': loan_cnt_data})

def loan_cal_view_list(request):
    if request.method == 'POST':
        v_loan_ac_no    = request.POST['acc_name']
        v_cn_val= request.POST['cn_val']
        if int(v_cn_val) == 1 :
            v_pgno = 1    
        if int(v_cn_val) == 2 :
            v_pgno = request.POST['pg_no']    
        if int(v_cn_val) == 3 :
            v_pgno = request.POST['pg_no']
        
#        print(v_cn_val)
#        print(v_loan_ac_no)
        v_int_data = loan_cal_controll.objects.get(loan_ac_no = v_loan_ac_no)
        v_loan_name = v_int_data.mem_acc_name
 
    v_trans = Paginator(loan_repayment_sch.objects.filter(Loan_no= v_loan_ac_no),22)

    
    # if int(v_cn_val) == 1 :
    #          pg_no=1
    # else :
    #          pg_no = int(v_pgno)+1
    
   
    total_pg = v_trans.num_pages

    if int(v_cn_val) == 1 :
              pg_no=1
    if int(v_cn_val) == 3 :
            v_pgno = request.POST['pg_no']
            pg_no = int(v_pgno)+1
            if pg_no > total_pg :
                pg_no=total_pg
    if int(v_cn_val) == 2 :
            v_pgno = request.POST['pg_no']
            pg_no = int(v_pgno)-1
            if pg_no == 0:
                 pg_no=1

    first_page = v_trans.get_page(pg_no)
#    print(pg_no)
    return render(request,'loan_vch_show.html',{'loan_v_trans': first_page,'name':v_loan_name,'loan_ac':v_loan_ac_no,'tot_pg':total_pg,'pgno':pg_no})

#Share Details 

def mem_share_add(request,id):
        v_cn_val = 1
        if request.method == 'POST':
#            v_share_srno = request.POST['vch_no']
            v_mem_no = request.POST['acc_name']
            v_det_date = request.POST['mem_dob']
            v_no_of_share = request.POST['no_of_share']
            v_cn_val =  request.POST['cn_val']
            trty_data=vch_type.objects.get(trans_type=id)
            v_vch_control=vch_control.objects.get(pk=id)
            v_no = v_vch_control.st_no+1
            v_share_srno= v_no
            v_vch_control.st_no=v_no
            v_vch_control.save()
#            dt=date.today()  
#            mem_share_detail(share_srno = v_no, tr_type = id,  det_date = dt).save()
            mem_det1= member_detail.objects.get(member_no = v_mem_no)
            v_mem_nm = mem_det1.name
            mydata = mem_share_detail(share_srno = v_share_srno, tr_type = id , mem_no = v_mem_no, det_date = v_det_date,mem_name= v_mem_nm,no_of_share = v_no_of_share )
            mydata.save()
        # if int(v_cn_val) == 1 :
        #     trty_data=vch_type.objects.get(trans_type=id)
        #     v_vch_control=vch_control.objects.get(pk=id)
        #     v_no = v_vch_control.st_no+1
        #     v_vch_control.st_no=v_no
        #     v_vch_control.save()
        #     dt=date.today()  
        #     mem_share_detail(share_srno = v_no, tr_type = id,  det_date = dt).save()
        #     v_sharedetail =mem_share_detail.objects.get(share_srno=v_no)
        #     mem_det = member_detail.objects.all()
        #     return render(request,'share_detail.html',{'mem_det':mem_det,'sharedetail':v_sharedetail})
        # else :
#        v_sharedetail =mem_share_detail.objects.get(share_srno=v_share_srno)
        dt=date.today()  
        mem_det = member_detail.objects.all()
        return render(request,'share_detail.html',{'mem_det':mem_det,'det_date':dt})


def share_list_view(request):
    share_det = mem_share_detail.objects.all()
    return render(request,'share_list.html',{'share_data':share_det})

def share_update(request,share_srno):
    share_det = mem_share_detail.objects.get(pk= share_srno)
    mem_det   = member_detail.objects.all()
    return render(request,'share_edit.html',{'mem_det':mem_det,'sh_data':share_det})


def doshare_update(request,share_srno):
      if request.method == 'POST':
            v_mem_no = request.POST.get('acc_name')
            v_det_date = request.POST.get('mem_dob')
            v_no_of_share = request.POST.get('no_of_share')
            v_cn_val =  request.POST['cn_val']
            v_share_srno = share_srno

            mem_det1= member_detail.objects.get(pk = v_mem_no)
            v_mem_nm = mem_det1.name

            share_det = mem_share_detail.objects.get(pk= share_srno)
            share_det.det_date=v_det_date
            share_det.no_of_share=v_no_of_share
            share_det.mem_no = v_mem_no
            share_det.mem_name = v_mem_nm
            share_det.save()
            share_det = mem_share_detail.objects.all()
            return render(request,'share_list.html',{'share_data':share_det})

def share_delete(request,share_srno):
    share_det = mem_share_detail.objects.get(pk= share_srno)
    share_det.delete()
    share_det = mem_share_detail.objects.all()
    return render(request,'share_list.html',{'share_data':share_det})

def cd_list_view(request):
    mem_det   = member_detail.objects.all()
    return render(request,'Member_cdlist.html',{'mem_det':mem_det})


def cd_cal(request):
        if request.method == 'POST':
            v_int_month = request.POST['int_month']
            v_int_year = request.POST['int_year']
            m_yrmn=int(v_int_year)*100+int(v_int_month)
            rec_cheK=cd_cal_controll.objects.filter(yrmn=m_yrmn).exists()
            if not rec_cheK :
                    days=30
                    leap = 0
                    if int(v_int_year) % 400 == 0:
                        leap = 1
                    elif int(v_int_year) % 100 == 0:
                        leap = 0
                    elif int(v_int_year) % 4 == 0:
                        leap = 1
                    if int(v_int_month) == 2:
                        days = 28 + leap
                    m_month=int(v_int_month)
                    m_list = [1,3,5,7,8,10,12]
                    if m_month in m_list:
                        days = 31
                    
                    v_dt = date(int(v_int_year), int(v_int_month), days)
                    cd_cal_controll.objects.create(yrmn=m_yrmn,tr_type = 2)
                    mem_det = member_detail.objects.all()

                    vch_amt_d=0
                    for mem in mem_det :
                        mem_acc_id=mem.acc_id
                        if mem_acc_id != None :
     #                       print(mem_acc_id)
     #                       cd_mem_list
                            cd_yrmn= m_yrmn*1000000+int(mem.member_no) 
                            m_loan_acc_id = 0
                            m_emi_pri = 0
                            m_emi_int= 0
                            loan_det_check = loan_repayment_sch.objects.filter(yrmn=m_yrmn , mem_no = mem.member_no).exists() 
     #                       print(loan_det_check)
                            if loan_det_check :
                               loan_det_sch = loan_repayment_sch.objects.get(yrmn=m_yrmn,mem_no = mem.member_no)
     #                           print(loan_det_sch)
                               m_loan_acc_id = loan_det_sch.mem_acc_id
                               m_emi_pri = loan_det_sch.monthly_prinipal_amt_deduction
                               m_emi_int= loan_det_sch.loan_int_amt
                            
                            cd_mem_list(mem_yrmn=cd_yrmn,yrnm = m_yrmn ,mem_no =mem.member_no,mem_name = mem.name, cd_amt = 1000, acc_id = mem_acc_id,loan_acc_id =m_loan_acc_id,
                                        emi_pri= m_emi_pri, emi_int = m_emi_int).save()
    #                        cd_mem_list.save()

        cdlist_data=cd_mem_list.objects.filter(yrnm = m_yrmn)
        return render(request,'cdlist_show.html',{'cdlist_data':cdlist_data,'yr':m_yrmn})

def cd_listupdate(request,mem_yrmn):
    m_mem_yrmn =  mem_yrmn
#    m_amt = request.GET['acc_opbal']
#    print(m_yrmn)
#    print(m_amt)
    cdlist_data=cd_mem_list.objects.get(mem_yrmn = m_mem_yrmn)
#    print(cdlist_data)
    return render(request,'cdlist_edit.html',{'cdlist_data':cdlist_data,'yr':m_mem_yrmn})

def cd_detupdate(request,mem_yrmn):
    m_mem_yrmn=mem_yrmn
    if request.method == 'POST':
        m_cd_mem_no = request.POST['cd_mem_no']
        m_cd_mem_name = request.POST['cd_mem_name']
        m_cd_mem_amt = request.POST['cd_mem_amt']
        m_cd_emi_pri = request.POST['cd_emi_pri']
        m_cd_emi_int = request.POST['cd_emi_int']
        m_yrmn = request.POST['cn_val']
        cdlist_data=cd_mem_list.objects.get(mem_yrmn = m_mem_yrmn)
        cdlist_data.mem_no=m_cd_mem_no
        cdlist_data.mem_name=m_cd_mem_name
        cdlist_data.mem_amt = m_cd_mem_amt
        cdlist_data.emi_pri = m_cd_emi_pri
        cdlist_data.emi_int = m_cd_emi_int
        cdlist_data.save()

    cdlist_data=cd_mem_list.objects.filter(yrnm = m_yrmn)
    return render(request,'cdlist_show.html',{'cdlist_data':cdlist_data,'yr':m_yrmn})

def cd_vch_post(request):
    error_msg=""
    if request.method == 'POST':
       m_yrmn = request.POST['cn_val']

    rec_cheK=cd_cal_controll.objects.get(yrmn=m_yrmn)
    vv_no=rec_cheK.vch_no
    if  (vv_no == 1 ) :
        error_msg="Voucher Already Post"
        cdlist_data=cd_mem_list.objects.filter(yrnm = m_yrmn)
        return render(request,'cdlist_show.html',{'cdlist_data':cdlist_data,'yr':m_yrmn,'msg':error_msg})
    else :         
        acc_data=account_head.objects.all()
        return render(request,'cd_vch_post.html',{'acc_data':acc_data,'yr':m_yrmn,'msg':error_msg})
     
         
def cd_vch_cal(request):
        error_msg=""
        if request.method == 'POST':
            v_bnk_acc_id = request.POST['bnk_acc_name']
            v_int_acc_id = request.POST['int_acc_name']
            v_int_month = request.POST['int_month']
            v_vch_dt = request.POST['mem_dob']
            m_yrmn=int(v_int_month)
#            print(m_yrmn)
            rec_cheK=cd_cal_controll.objects.get(yrmn=v_int_month)
#            print(rec_cheK)
            vv_no=rec_cheK.vch_no
#            print(vv_no)
            if  (int(vv_no) == 0 ) :
#                    print("vipul")
                    acc_data1=account_head.objects.get(id=v_bnk_acc_id)
                    bnk_ac_name=acc_data1.acc_name        
                    acc_data1=account_head.objects.get(id=v_int_acc_id)
                    int_ac_name=acc_data1.acc_name        
                    cd_data = cd_mem_list.objects.filter(yrnm = m_yrmn)
                    # Voucher No generation code
                    for cd_det in cd_data :
                        v_mem_yrmn = cd_det.mem_yrmn
#                        print("vipul1")
                        v_loan_id = cd_det.loan_acc_id
                        cr_amt=0
                        if cd_det.cd_amt != 0 :
                            v_vch_control=vch_control.objects.get(pk=2)
                            v_no = v_vch_control.st_no+1
                            v_vch_control.st_no=v_no
                            v_vch_control.save()
                            vch_control_srno(tr_type = 2 , st_no =v_no,stsr_no =  0).save()
                            v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                            v_sr = v_vch_control_srno.stsr_no+1
                            v_vch_control_srno.stsr_no=v_sr
                            v_vch_control_srno.save()
                            v_srno_1 = (v_no*1000)+v_sr
                            if (cd_det.loan_acc_id != 0) and (cd_det.emi_pri != 0) :
#                             v_loan_id = cd_det.loan_acc_id
                                 m_amt = cd_det.emi_pri
                                 cr_amt = cr_amt + m_amt
                                 v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                                 v_sr = v_vch_control_srno.stsr_no+1
                                 v_vch_control_srno.stsr_no=v_sr
                                 v_vch_control_srno.save()
                                 v_srno_2 = (v_no*1000)+v_sr
                                 acc_data1=account_head.objects.get(id=v_loan_id)
                                 loan_ac_name=acc_data1.acc_name        
                                 vch_trans(trans_type = 2, vch_no = v_no, vch_no_srno = v_srno_2, vch_date = v_vch_dt, vch_acc_head = loan_ac_name, vch_acc_id = v_loan_id, vch_dc = "C", vch_amt = m_amt, srno = v_sr  ).save()
                                 #***********************INTEREST ENTERy
                            if (cd_det.loan_acc_id != 0) and (cd_det.emi_int != 0):
                                 m_amt = cd_det.emi_int
                                 cr_amt = cr_amt + m_amt
                                 v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                                 v_sr = v_vch_control_srno.stsr_no+1
                                 v_vch_control_srno.stsr_no=v_sr
                                 v_vch_control_srno.save()
                                 v_srno_2 = (v_no*1000)+v_sr
                                 vch_trans(trans_type = 2, vch_no = v_no, vch_no_srno = v_srno_2, vch_date = v_vch_dt, vch_acc_head = int_ac_name, vch_acc_id = v_int_acc_id, vch_dc = "C", vch_amt = m_amt, srno = v_sr  ).save()
                                 #***********************INTEREST ENTERy
                            if (cd_det.acc_id != 0) and (cd_det.cd_amt != 0) :
                                 v_cd_id = cd_det.acc_id
                                 m_amt = cd_det.cd_amt
                                 cr_amt = cr_amt + m_amt
                                 v_vch_control_srno = vch_control_srno.objects.get(pk =v_no)
                                 v_sr = v_vch_control_srno.stsr_no+1
                                 v_vch_control_srno.stsr_no=v_sr
                                 v_vch_control_srno.save()
                                 v_srno_2 = (v_no*1000)+v_sr
                                 acc_data1=account_head.objects.get(id=v_cd_id)
                                 loan_ac_name=acc_data1.acc_name        
                                 vch_trans(trans_type = 2, vch_no = v_no, vch_no_srno = v_srno_2, vch_date = v_vch_dt, vch_acc_head = loan_ac_name, vch_acc_id = v_cd_id, vch_dc = "C", vch_amt = m_amt , srno = v_sr ).save()
                    
                            if (cr_amt !=0 ) :
                                vch_trans(trans_type = 2, vch_no = v_no, vch_no_srno = v_srno_1, vch_date = v_vch_dt, vch_acc_head = bnk_ac_name, vch_acc_id = v_bnk_acc_id, vch_dc = "D", vch_amt = cr_amt, srno = v_sr  ).save()
                                cd_data1 = cd_mem_list.objects.get(mem_yrmn = v_mem_yrmn)
                                cd_data1.vch_no = v_no
                                cd_data1.save()
            else :
                error_msg="Voucher Already Post"
        
            rec_cheK.vch_no = 1                       
            rec_cheK.save()
        acc_data=account_head.objects.all()
        return render(request,'cd_vch_post.html',{'acc_data':acc_data,'yr':v_int_month,'msg':error_msg})

def mem_loan_master(request):   
    mem_det   = member_detail.objects.all()
    return render(request,'mem_loan_mas.html',{'mem_det':mem_det})

def mem_loan_view(request):   
    error_msg=''
    if request.method == 'POST':
        v_loan_mem_no = request.POST['mem_name']
        error_msg=member_detail.objects.get(member_no = v_loan_mem_no).name
        loan_mas_data_check = loan_master.objects.filter(loan_mem_no = v_loan_mem_no).exists()
        if loan_mas_data_check :
                mem_det = member_detail.objects.filter(member_no = v_loan_mem_no )
                loan_mas_data = loan_master.objects.filter(loan_mem_no = v_loan_mem_no)
                return render(request,'loan_mster_list.html',{'mem_det':mem_det,'loan_mas_data':loan_mas_data,'nm':error_msg})
        else :
                mem_det=member_detail.objects.all()
                error_msg +='  [The Member has no loan Account]'
                return render(request,'mem_loan_mas.html',{'mem_det':mem_det,'msg':error_msg})

def mem_loan_add(request):   
    grp_data=acc_group.objects.all()
    mem_det   = member_detail.objects.all()
    return render(request,'loan_mas_add.html',{'mem_det':mem_det,'grp_data':grp_data})

def mem_loan_mas_sv(request):
        error_msg=""
        if request.method == 'POST':
            v_mem_no      =  request.POST['mem_name']
            v_acc_nm      = request.POST['acc_name']
            v_grp_id      = request.POST['group'] 
            v_mem_name  = member_detail.objects.get(member_no=v_mem_no).name
            v_grp_name = acc_group.objects.get(id=v_grp_id).grp_name
            mymem = account_head(acc_name = v_acc_nm, grp_id_id = v_grp_id ,  grp_nm = v_grp_name)
            mymem.save()
            v_acc_id = account_head.objects.get(acc_name=v_acc_nm).id
#            print(v_acc_nm)
#            print(v_acc_id)

            loan_mas = loan_master(loan_mem_no = v_mem_no,loan_mem_nm = v_mem_name, loan_acc_id = v_acc_id, loan_acc_nm = v_acc_nm, disb_amt = 0 , loan_int =0 , out_amt = 0, out_int =0, loan_status = 1)
            loan_mas.save()

        grp_data=acc_group.objects.all()
        mem_det   = member_detail.objects.all()
        return render(request,'loan_mas_add.html',{'mem_det':mem_det,'grp_data':grp_data})

def daybook_view(request):
        dt=date.today()    
        return render(request,'daybookview.html',{'v_dt':dt})

def daybook_list(request):
        error_msg=""
        if request.method == 'POST':
            v_vch_dt= request.POST['vch_stdt']
            daybook_data = vch_trans.objects.filter(vch_date = v_vch_dt, srno=1)
        
        return render(request,'daybooklist.html',{'day_data':daybook_data,'v_dt':v_vch_dt})


def vch_trans_edit(request,vch_no):
        error_msg=""
#        v_trans_detail=vch_trans.objects.get(vch_no_srno=vch_no)
#    print(v_trans_detail)
        v_srno_1 = (vch_no*1000)+1
        m_vchno=vch_no
        print(m_vchno)
        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        tr_ty=v_trans.trans_type
        trty_data=vch_type.objects.get(trans_type=tr_ty)
        acc_data=account_head.objects.all()
        v_trans_detail=vch_trans.objects.filter(vch_no = m_vchno)
        print(v_trans_detail)
#        v_srno_1 = (v_trans_detail.vch_no*1000)+1
#        v_trans=vch_trans.objects.get(vch_no_srno=v_srno_1)
        return render(request,'transaction_entry.html',{'trty_data':trty_data,'acc_data':acc_data,'v_trans':v_trans,'v_trans_detail':v_trans_detail,'sv_ty':tr_ty,'v_srno_1':v_srno_1})
