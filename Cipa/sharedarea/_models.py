# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Appointment(models.Model):
    id_appointment = models.IntegerField(primary_key=True)
    schedule = models.DateField()
    observations = models.TextField()
    service = models.CharField(max_length=45)
    clinic = models.CharField(max_length=45)
    client_id_client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client_id_client')

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    quote = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    role_user = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    image_uri = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'auth_user'
    def __str__(self):
        return '%s' % (self.username)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'client'


class Comments(models.Model):
    id_comments = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    form_id_form = models.ForeignKey('Form', models.DO_NOTHING, db_column='form_id_form')

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Field(models.Model):
    id_field = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=250)
    field_number = models.IntegerField()
    form_type_id_form_type = models.ForeignKey('FormType', models.DO_NOTHING, db_column='form_type_id_form_type')
    field_type = models.IntegerField()
    field_placeholder = models.CharField(max_length=50, blank=True, null=True)
    field_identifier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Form(models.Model):
    id_form = models.AutoField(primary_key=True)
    record_id_record = models.ForeignKey('Record', models.DO_NOTHING, db_column='record_id_record')
    form_type_id_form_type = models.ForeignKey('FormType', models.DO_NOTHING, db_column='form_type_id_form_type')

    class Meta:
        managed = False
        db_table = 'form'


class FormHasField(models.Model):
    id_form_has_field = models.AutoField(primary_key=True)
    form_id_form = models.ForeignKey(Form, models.DO_NOTHING, db_column='form_id_form')
    field_id_field = models.ForeignKey(Field, models.DO_NOTHING, db_column='field_id_field')
    text_answer = models.TextField(blank=True, null=True)
    int_answer = models.IntegerField(blank=True, null=True)
    date_answer = models.DateField(blank=True, null=True)
    bool_answer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_has_field'



class FormHasFormTable(models.Model):
    id_form_has_form_table = models.AutoField(primary_key=True)
    form_id_form = models.ForeignKey(Form, models.DO_NOTHING, db_column='form_id_form')
    form_table_id_form_table = models.ForeignKey('FormTable', models.DO_NOTHING, db_column='form_table_id_form_table')
    answer_col_1 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_2 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_3 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_4 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_5 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_6 = models.CharField(max_length=45, blank=True, null=True)
    answer_col_7 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_has_form_table'


class FormTable(models.Model):
    id_form_table = models.AutoField(primary_key=True)
    form_table_name = models.CharField(max_length=50)
    field_number = models.IntegerField()
    form_type_id_form_type = models.ForeignKey('FormType', models.DO_NOTHING, db_column='form_type_id_form_type')
    field_type = models.IntegerField()
    number_columns = models.IntegerField()
    column1 = models.CharField(max_length=50, blank=True, null=True)
    column2 = models.CharField(max_length=50, blank=True, null=True)
    column3 = models.CharField(max_length=50, blank=True, null=True)
    column4 = models.CharField(max_length=50, blank=True, null=True)
    column5 = models.CharField(max_length=50, blank=True, null=True)
    column6 = models.CharField(max_length=50, blank=True, null=True)
    column7 = models.CharField(max_length=50, blank=True, null=True)
    form_table_identifier = models.CharField(max_length=50, blank=True, null=True)

    def column_list(self):
	return [self.column1, self.column2, self.column3, self.column4, self.column5, self.column6, self.column7]

    class Meta:
        managed = False
        db_table = 'form_table'


class FormType(models.Model):
    id_form_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=45)
    multiple = models.IntegerField(blank=True, null=True)
    is_file = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_type'



class Induction(models.Model):
    id_induction = models.IntegerField(primary_key=True)
    module_1 = models.IntegerField()
    module_2 = models.IntegerField()
    module_3 = models.IntegerField()
    module_4 = models.IntegerField()
    approved_date = models.DateField(blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'induction'


class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    record_type = models.CharField(max_length=45, blank=True, null=True)
    student = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    professor = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True, related_name='professor')
    client_id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client_id_client', blank=True, null=True)
    record_date = models.DateField()

    def my_id(self):
	return '%d-%d-%d' % (self.record_date.year, self.record_date.month, self.client_id_client.id_client)

    class Meta:
        managed = False
        db_table = 'record'

    

class Test(models.Model):
    id_test = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    max_val = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'test'

    def __str__(self):
        return '%s' % (self.name)


class TestDemograficResult(models.Model):
    id_test_demografic_result = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    relationship = models.CharField(max_length=6)
    test_result_id_test_result = models.ForeignKey('TestResult', models.DO_NOTHING, db_column='test_result_id_test_result')

    class Meta:
        managed = False
        db_table = 'test_demografic_result'


class TestOrganizationGeneralForm(models.Model):
    id_test_organization_general_form = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    marital_status = models.CharField(max_length=45)
    education = models.CharField(max_length=45)
    job = models.CharField(max_length=45)
    working_time = models.CharField(max_length=45)
    organization_size = models.CharField(max_length=45)
    organization_type = models.CharField(max_length=45)
    test_result_id_test_result = models.ForeignKey('TestResult', models.DO_NOTHING, db_column='test_result_id_test_result')

    class Meta:
        managed = False
        db_table = 'test_organization_general_form'


class TestQuestions(models.Model):
    id_test_questions = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=150)
    test_id_test = models.ForeignKey(Test, models.DO_NOTHING, db_column='test_id_Test')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_questions'
    def __str__(self):
        return '%d %s %s' % (self.id_test_questions, self.test_id_test, self.question)


class TestResult(models.Model):
    id_test_result = models.IntegerField(primary_key=True)
    resultado = models.TextField(blank=True, null=True)
    test_id_test = models.ForeignKey(Test, models.DO_NOTHING, db_column='test_id_test')
    generated_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_result'


class UploadForm(models.Model):
    id_upload_form = models.AutoField(primary_key=True)
    link = models.TextField(blank=True, null=True)
    record_id_record = models.ForeignKey(Record, models.DO_NOTHING, db_column='record_id_record')
    form_type_id_form_type = models.ForeignKey(FormType, models.DO_NOTHING, db_column='form_type_id_form_type')

    class Meta:
        managed = False
        db_table = 'upload_form'


class UserEducationExperience(models.Model):
    id_user_education_experience = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=150)
    first_date = models.TextField()  # This field type is a guess.
    last_date = models.TextField()  # This field type is a guess.
    education_type = models.IntegerField()
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_education_experience'


class UserHasTest(models.Model):
    test_result_id_test_result = models.ForeignKey(TestResult, models.DO_NOTHING, db_column='test_result_id_test_result')
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_has_test'
        unique_together = (('test_result_id_test_result', 'auth_user'),)


class UserSkills(models.Model):
    id_user_skills = models.AutoField(primary_key=True)
    computer_skill = models.IntegerField(blank=True, null=True)
    learning_skill = models.IntegerField(blank=True, null=True)
    ethic_skill = models.IntegerField(blank=True, null=True)
    responsability_skill = models.IntegerField(blank=True, null=True)
    strategy_skill = models.IntegerField(blank=True, null=True)
    professional_growth_skill = models.IntegerField(blank=True, null=True)
    professional_relationships_skill = models.IntegerField(blank=True, null=True)
    interpersonal_relationships_skill = models.IntegerField(blank=True, null=True)
    knowledge_skill = models.IntegerField(blank=True, null=True)
    problem_solver_skill = models.IntegerField(blank=True, null=True)
    effective_communication_skill = models.IntegerField(blank=True, null=True)
    control_skill = models.IntegerField(blank=True, null=True)
    adaptability_skill = models.IntegerField(blank=True, null=True)
    creativity_skill = models.IntegerField(blank=True, null=True)
    decision_making_skill = models.IntegerField(blank=True, null=True)
    emotional_skill = models.IntegerField()
    opportunity_identification_skill = models.IntegerField(blank=True, null=True)
    team_work_skill = models.IntegerField(blank=True, null=True)
    leadership_skill = models.IntegerField(blank=True, null=True)
    conflict_manage_skill = models.IntegerField(blank=True, null=True)
    proactivity = models.IntegerField(blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_skills'


class UserWorkExperience(models.Model):
    id_user_experience = models.IntegerField(primary_key=True)
    organization_typen_name = models.CharField(max_length=150)
    job_position = models.CharField(max_length=150)
    first_date = models.TextField()  # This field type is a guess.
    last_date = models.TextField()  # This field type is a guess.
    auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_work_experience'

class Documents(models.Model):
	id_documents = models.AutoField(primary_key=True)
	author = models.TextField()
	link = models.TextField()
	keywords = models.TextField()
	title = models.TextField()
	uploaded_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='uploaded_by')

	class Meta:
		managed = False
		db_table = 'documents'

	def __str__(self):
		return '%s - %s' % (self.title, self.author)
