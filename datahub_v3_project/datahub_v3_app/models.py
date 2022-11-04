from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# from django.contrib.postgres.fields import JSONField
try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField
# from django.contrib.auth.models import AbstractUser


class User(AbstractBaseUser):
   
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,unique=True,blank=False)
    phone_number = models.CharField(max_length=15,blank=False)
    password = models.CharField(max_length=255,blank=False)
    alternate_phonenumber = models.CharField(max_length=15,blank=True)
    addressline_one = models.CharField(max_length=100,blank=False)
    addressline_two = models.CharField(max_length=100,blank=True)
    countryor_city = models.CharField(max_length=100,blank=False)
    postalcode = models.CharField(max_length=100,blank=False)
    company_name = models.CharField(max_length=100,blank=True)
    company_type = models.CharField(max_length=100,blank=True)
    category = models.CharField(max_length=100,blank=False)
    username = None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

    class Meta:
        db_table = "register"


class Conn(models.Model):
    # connections_id=models.AutoField(auto_created=True,primary_key=True,serialize=True,verbose_name='ID')
    connection_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo_name =models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    key_param=JSONField()

    class Meta:
        db_table = "connections"


class pipiline_sch(models.Model):

    pipeline_schedule_desc = models.CharField(max_length=100)
    pipeline_schedule_name = models.CharField(max_length=100)
    pipeline_detail_name = models.CharField(max_length=100)
    pipeline_schedule_start_date = models.DateField()
    pipeline_schedule_end_date = models.DateField()
    pipeline_schedule_time= models.TimeField()
    pipeline_schedule_run_imme=models.BooleanField()
    pipeline_status=models.BooleanField(default=True)

     
    class Meta:
        db_table = "pipeline_sch"


class db_sql_table(models.Model):
    database_name = models.CharField(max_length=200)
    sequelize_query = models.CharField(max_length= 2000)
    sql_validation = models.CharField(max_length=200)
    sql_status = models.CharField(max_length=200) 
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)



    def str(self):
        return self.db_sql_table
 
    class Meta:
        db_table = "db_sql_extract"

class ScheduleDependency(models.Model):
    # s_no = models.CharField(max_length =10)
    pipeline_schedule_dependency_name = models.CharField(max_length=50)
    parent_schedule_name =  models.CharField(max_length=50)
    child_schedule_name =  models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.pipeline_schedule_dependency_name
 
    class Meta:
        db_table = 'scheduledependency'    

class pipline_table(models.Model):
   # Pipeline_name = models.CharField(max_length=100)
     pipeline_name= models.CharField(max_length=30, blank=True)
     Description = models.CharField(max_length=30, blank=True)
     configuration_name = models.CharField(max_length=30,blank=True)
     Start_date = models.DateField()
     End_date = models.DateField()
     is_active = models.BooleanField(default=True) 

     class Meta:
        db_table = 'pipeline'    

class pipline_details(models.Model):
    pipeline_detail_name = models.CharField(max_length=100)
    pipeline_dtls_desc = models.CharField(max_length=100,null=True)
    pipeline_id=models.ForeignKey(pipline_table, on_delete=models.CASCADE, blank=True, null=True,related_name='pipeline_id')
    sql_extract_name = models.ForeignKey(db_sql_table, on_delete=models.CASCADE, blank=True, null=True,related_name='sql_extract_name')
    source_table_name= models.CharField(max_length=100)
    target_table_name = models.CharField(max_length=100)    
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    last_modified_by = models.CharField(max_length=100,null=True)
    last_modified_on = models.DateField(auto_now=True,null=True)
    created_on= models.DateField(auto_now=True,null=True)
    created_by= models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=True,null=True)
    pipeline_dtls_truncate_load = models.CharField(max_length=100,null=True)
    pipeline_dtls_bench_mark_commit = models.CharField(max_length=100,null=True)
    pipeline_dtls_parallel_load_allowed = models.CharField(max_length=100,null=True)
    pipeline_dtls_parallel_thread_count = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'pipline_details'   


class con_detail(models.Model):

    connection_id =models.ForeignKey(Conn, on_delete=models.CASCADE, blank=True, null=True,related_name='connection_id')
    # connection_name = models.CharField(max_length=100)
    connection_detail = models.CharField(max_length=100)
    con_str=JSONField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    last_modified_by = models.CharField(max_length=100,null=True)
    last_modified_on = models.DateField(auto_now=True,null=True)
    created_on= models.DateField(auto_now=True,null=True)
    created_by= models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'con_detail' 


class db_conf(models.Model):
    config_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    source_connection_name= models.CharField(max_length=100)
    target_connection_name= models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True) 

    class Meta:
        db_table = 'db_conf' 

class role_api(models.Model):

    role_name = models.CharField(max_length=100)
    role_desc = models.CharField(max_length=100)
    role_start_date = models.DateField()
    role_end_date = models.DateField()
    role_status = models.BooleanField()

    class Meta:
        db_table = 'role' 

class role_detail_api(models.Model):

    role_name = models.CharField(max_length=100)
    role_detail_name = models.CharField(max_length=100)
    role_description = models.CharField(max_length=150)
    role_handling_pages = models.CharField(max_length=300)

    class Meta:
        db_table = 'role_detail' 
        
class users_role_view(models.Model):
    user_name=models.CharField(max_length=300)
    role_name=models.CharField(max_length=300)
    start_date=models.DateField(auto_now=True)
    end_date=models.DateField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        db_table = 'user_role' 
        