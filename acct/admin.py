from django.contrib import admin
from acct.models import (acct_attribute, Student, Staff, Enrollment, ClassName,
                             Subject, Transcript, Fees, Parent, Teaches)

class ClassificationModelAdmin(admin.ModelAdmin):
	list_display = ['classification', 'gender', 'timestamp']
	class Meta:
		model = acct_attribute
admin.site.register(acct_attribute, ClassificationModelAdmin)

admin.site.register(Parent)

admin.site.register(Teaches)

admin.site.register(Student)

class StaffModelAdmin(admin.ModelAdmin):
	list_display = ['position', 'timestamp']
	class Meta:
		model = Staff
admin.site.register(Staff, StaffModelAdmin)

class SubjectModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'timestamp']
	class Meta:
		model = Subject
admin.site.register(Subject, SubjectModelAdmin)

class ClassNameModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'timestamp']
	class Meta:
		model = ClassName
admin.site.register(ClassName, ClassNameModelAdmin)

class EnrollmentModelAdmin(admin.ModelAdmin):
	list_display = ['student', 'timestamp']
	class Meta:
		model = Enrollment
admin.site.register(Enrollment, EnrollmentModelAdmin)

class FeeModelAdmin(admin.ModelAdmin):
	list_display = ['student_id', 'status', 'timestamp']
	class Meta:
		model = Fees
admin.site.register(Fees, FeeModelAdmin)

class TranscriptModelAdmin(admin.ModelAdmin):
	list_display = ['mark', 'grade', 'timestamp']
	class Meta:
		model = Transcript
admin.site.register(Transcript, TranscriptModelAdmin)