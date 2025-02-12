from datetime import date
from django.db import models
from django.utils import timezone
from django.utils import formats


# Create your models here.
class acc_group(models.Model):
    grp_name = models.CharField(max_length=10)
class account_head(models.Model):
    acc_name = models.CharField(max_length=40)
    op_bal = models.FloatField()
    grp_nm = models.CharField(max_length=20)
    grp_id = models.ForeignKey(acc_group, on_delete=models.CASCADE, null=True) 
#    accmem_no = models.IntegerField()
    #grp_name =models.CharField(max_length=20 , null= True)   
    #country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

class member_detail(models.Model):
    member_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=70,null=True)
    phone =models.IntegerField(null=True)
    addhar=models.CharField(max_length=12,null=True)
    panno=models.CharField(max_length=10,null=True)
    driving_no=models.CharField(max_length=15,null=True)
    passport_no=models.CharField(max_length=15,null=True)
    bank_name=models.CharField(max_length=40,null=True)
    bank_account=models.CharField(max_length=16,null=True)
    bank_ifsc=models.CharField(max_length=15,null=True)
    nominee=models.CharField(max_length=50,null=True)
    nominee_phone=models.IntegerField(null=True)
    no_of_children=models.IntegerField(null=True)
    op_bal = models.IntegerField(null=True)
    acc_name = models.CharField(max_length=40)
    grp_nm = models.CharField(max_length=20)
    acc_id = models.IntegerField(null=True)
    grp_id = models.ForeignKey(acc_group, on_delete=models.CASCADE, null=True) 
    mem_sex = models.IntegerField(null=True)
    mem_sex_val = models.CharField(max_length=10)

class vch_type(models.Model):
    trans_type = models.IntegerField(primary_key=True)
    vch_type_name = models.CharField(max_length=10)

class vch_trans(models.Model):
    vch_no  = models.BigIntegerField()
    vch_date = models.DateField()
    vch_acc_head = models.CharField(max_length=40)
    vch_amt  = models.FloatField()
    trans_nm = models.CharField(max_length=50)
    trans_type = models.IntegerField()
    vch_acc_id = models.IntegerField()
    vch_no_srno = models.BigIntegerField(primary_key=True)
    vch_dc = models.CharField(max_length=1)

class vch_control(models.Model):
    tr_type  = models.IntegerField(primary_key=True)
    st_no   = models.BigIntegerField()
    stsr_no = models.BigIntegerField()
    yr      = models.IntegerField()

class vch_control_srno(models.Model):
    tr_type  = models.IntegerField()
    st_no    = models.BigIntegerField(primary_key=True)
    stsr_no  = models.BigIntegerField()
    yr       = models.IntegerField()

class int_cal_controll(models.Model):
    yrmn    = models.IntegerField(primary_key=True)
    tr_type  = models.IntegerField()
    vch_no   = models.BigIntegerField()
    int_rt   = models.FloatField()

class div_cal_controll(models.Model):
    yrmn     = models.IntegerField(primary_key=True)
    tr_type  = models.IntegerField()
    vch_no   = models.BigIntegerField()
    int_rt   = models.FloatField()

class mem_cont_control(models.Model):
    yrmn    = models.IntegerField(primary_key=True)
    tr_type  = models.IntegerField()
    vch_no   = models.BigIntegerField()
 

class mem_share_detail(models.Model):
    share_srno = models.IntegerField(primary_key=True)
    tr_type= models.IntegerField()
    mem_no = models.IntegerField()
    mem_name = models.CharField(max_length=40)
    det_date = models.DateField()
    no_of_share =models.IntegerField()

class loan_cal_controll(models.Model):
    loan_ac_no = models.BigIntegerField(primary_key=True)
    mem_no    = models.IntegerField()
    st_date = models.DateField()
    tr_type  = models.IntegerField()
    mem_name = models.CharField(max_length=40)
    vch_no   = models.BigIntegerField()
    loan_amt = models.BigIntegerField()
    loan_mnth = models.ImageField()
    int_rt   = models.FloatField()
    emi_amt = models.FloatField()
    loan_status = models.IntegerField()   
    mem_acc_id = models.IntegerField()
    mem_acc_name = models.CharField(max_length=40)
    acc_grp_id = models.IntegerField()
    acc_grp_nm = models.CharField(max_length=20)

class loan_repayment_sch(models.Model):
    loan_ac_no_srno = models.BigIntegerField(primary_key=True)
    #loan_ac_no_srno= Loan_ac_no+month+year
    Loan_no   = models.BigIntegerField()
    repayment_date = models.DateField()
    st_date = models.DateField()
    tr_type  = models.IntegerField()
    mem_no    = models.IntegerField()
    mem_name = models.CharField(max_length=40)
    openning_loan_amt = models.FloatField()
    emi_amt = models.FloatField()
    loan_int_amt = models.FloatField()
    monthly_prinipal_amt_deduction = models.BigIntegerField()
    balance_loan_amt = models.FloatField()
    loan_mnth = models.IntegerField()
    int_rt   = models.FloatField()
    emi_paid = models.IntegerField()   
    mem_acc_id = models.IntegerField()
    mem_acc_name = models.CharField(max_length=40)