from django.db import models
from datetime import datetime

from location.models import Country, State, District, Taluk
from department.models import Department

class CommunityMaster(models.Model):
    community_id = models.AutoField(primary_key=True)
    community_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'community_master'

    def save(self, *args, **kwargs):
        if self.community_name:
            self.community_name = self.community_name.upper()
        super(CommunityMaster, self).save(*args, **kwargs)

    def __str__(self):
        return self.community_name

class ApplicationMaster(models.Model):
    APPLICATION_TYPE_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    
    app_id = models.AutoField(primary_key=True)
    application_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    application_type = models.CharField(max_length=2, choices=APPLICATION_TYPE_CHOICES)
    
    name = models.CharField(max_length=100, null=True, blank=True)
    name_tamil = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=20, null=True, blank=True)
    
    aadhaar_no = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    community = models.ForeignKey(CommunityMaster, on_delete=models.SET_NULL, null=True, blank=True, db_column='community_id')
    caste = models.CharField(max_length=50, null=True, blank=True)
    
    mother_tongue = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    
    email = models.EmailField(max_length=100, null=True, blank=True)
    student_mobile = models.CharField(max_length=15, null=True, blank=True)
    parent_mobile = models.CharField(max_length=15, null=True, blank=True)
    
    applicant_user = models.ForeignKey('ApplicantUser', on_delete=models.CASCADE, null=True, blank=True, db_column='applicant_user_id', related_name='applications')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'application_master'

    def save(self, *args, **kwargs):
        if not self.application_no:
            prefix = self.application_type  # 'UG' or 'PG'
            year = str(datetime.now().year)[2:] # '26'
            
            # Find last number for this prefix and year
            last_app = ApplicationMaster.objects.filter(
                application_no__startswith=f"{prefix}{year}"
            ).order_by('-application_no').first()
            
            if last_app:
                try:
                    last_no = int(last_app.application_no[4:])
                    new_no = str(last_no + 1).zfill(3)
                except (ValueError, IndexError):
                    new_no = '001'
            else:
                new_no = '001'
            
            self.application_no = f"{prefix}{year}{new_no}"
        super(ApplicationMaster, self).save(*args, **kwargs)

    def __str__(self):

        return f"{self.application_no} - {self.name}"

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('Present', 'Present'),
        ('Permanent', 'Permanent'),
        ('Communication', 'Communication'),
    ]
    
    address_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='addresses', db_column='app_id')
    
    address_type = models.CharField(max_length=15, choices=ADDRESS_TYPE_CHOICES)
    address = models.TextField(null=True, blank=True)
    
    taluk = models.ForeignKey(Taluk, on_delete=models.SET_NULL, null=True, blank=True, db_column='taluk_id')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, db_column='district_id')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, db_column='state_id')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, db_column='country_id')
    
    pincode = models.CharField(max_length=10, null=True, blank=True)
    other_district = models.CharField(max_length=100, null=True, blank=True)
    other_taluk = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'application_address'

class ParentDetails(models.Model):
    parent_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='parent_details', db_column='app_id')
    
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_occupation = models.CharField(max_length=100, null=True, blank=True)
    father_qualification = models.CharField(max_length=100, null=True, blank=True)
    father_phone = models.CharField(max_length=15, null=True, blank=True)
    
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_occupation = models.CharField(max_length=100, null=True, blank=True)
    mother_qualification = models.CharField(max_length=100, null=True, blank=True)
    mother_phone = models.CharField(max_length=15, null=True, blank=True)
    
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_relationship = models.CharField(max_length=50, null=True, blank=True)
    guardian_occupation = models.CharField(max_length=100, null=True, blank=True)
    guardian_contact = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'application_parent'

class CoursePreference(models.Model):
    course_pref_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='course_preferences', db_column='app_id')
    
    course_type = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    preference_order = models.IntegerField(null=True, blank=True)
    mode = models.CharField(max_length=20, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, db_column='dept_id')

    class Meta:
        db_table = 'application_course'

class AdditionalInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='additional_info', db_column='app_id')
    
    physically_challenged = models.BooleanField(default=False)
    ex_serviceman_child = models.BooleanField(default=False)
    tamil_origin = models.BooleanField(default=False)
    
    sports_details = models.TextField(null=True, blank=True)
    ncc_details = models.TextField(null=True, blank=True)
    nss_details = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'application_additional_info'

class UGMarks(models.Model):
    PART_CHOICES = [
        ('Part I', 'Part I'),
        ('Part II', 'Part II'),
        ('Part III', 'Part III'),
    ]
    
    ug_marks_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='ug_marks', db_column='app_id')
    
    subject = models.CharField(max_length=100, null=True, blank=True)
    marks_secured = models.IntegerField(null=True, blank=True)
    max_marks = models.IntegerField(null=True, blank=True)
    
    part = models.CharField(max_length=10, choices=PART_CHOICES)

    class Meta:
        db_table = 'application_ug_marks'

class PGAcademicRecord(models.Model):
    pg_record_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='pg_records', db_column='app_id')
    
    qualification = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    
    subject = models.CharField(max_length=100, null=True, blank=True)
    marks_obtained = models.IntegerField(null=True, blank=True)
    max_marks = models.IntegerField(null=True, blank=True)
    
    month_year_of_passing = models.CharField(max_length=20, null=True, blank=True)
    attempts = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'application_pg_academic_record'

class StatusMaster(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'application_status_master'

    def save(self, *args, **kwargs):
        if self.status_name:
            self.status_name = self.status_name.upper()
        super(StatusMaster, self).save(*args, **kwargs)

    def __str__(self):
        return self.status_name

class ApplicationStatus(models.Model):
    app_status_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(ApplicationMaster, on_delete=models.CASCADE, related_name='status_history', db_column='app_id')
    status = models.ForeignKey(StatusMaster, on_delete=models.CASCADE, db_column='status_id')
    
    remarks = models.TextField(null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'application_status'

import bcrypt

class ApplicantUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'application_users'

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self):
        return self.email
