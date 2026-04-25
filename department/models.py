from django.db import models

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=2, choices=[('UG', 'UG'), ('PG', 'PG')], default='UG')
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'department_department'

    def __str__(self):
        return self.dept_name
