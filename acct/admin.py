from django.contrib import admin
from acct.models import (acct_attribute, student, staff, enrollment, className,
                             subjectName, transcript, fees)

class ClassificationModelAdmin(admin.ModelAdmin):
	list_display = ['classification', 'gender', 'timestamp']
	class Meta:
		model = acct_attribute
admin.site.register(acct_attribute, ClassificationModelAdmin)

admin.site.register(student)

class StaffModelAdmin(admin.ModelAdmin):
	list_display = ['position', 'timestamp']
	class Meta:
		model = staff
admin.site.register(staff, StaffModelAdmin)

class SubjectNameModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'timestamp']
	class Meta:
		model = subjectName
admin.site.register(subjectName, SubjectNameModelAdmin)

class ClassNameModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'timestamp']
	class Meta:
		model = className
admin.site.register(className, ClassNameModelAdmin)

class EnrollmentModelAdmin(admin.ModelAdmin):
	list_display = ['rootid', 'timestamp']
	class Meta:
		model = enrollment
admin.site.register(enrollment, EnrollmentModelAdmin)

class FeeModelAdmin(admin.ModelAdmin):
	list_display = ['student_id', 'status', 'timestamp']
	class Meta:
		model = fees
admin.site.register(fees, FeeModelAdmin)

class TranscriptModelAdmin(admin.ModelAdmin):
	list_display = ['mark', 'grade', 'timestamp']
	class Meta:
		model = transcript
admin.site.register(transcript, TranscriptModelAdmin)