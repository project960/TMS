
from django.db import models


class ALogTable(models.Model):
    slno = models.AutoField(primary_key=True)
    admin_name = models.CharField(blank=True, null=True)
    login = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(blank=True, null=True)
    user_type = models.CharField(blank=True, null=True)
    minor_job_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    import_file = models.TextField(blank=True, null=True)
    import_timestamp = models.DateTimeField(blank=True, null=True)
    export_file = models.TextField(blank=True, null=True)
    export_timestamp = models.DateTimeField(blank=True, null=True)
    logout = models.DateTimeField(blank=True, null=True)
    log_duration = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a_log_table'


class AdminTable(models.Model):
    a_id = models.CharField(primary_key=True, max_length=20)
    a_email = models.CharField(unique=True, max_length=254)
    a_name = models.CharField(unique=True, max_length=100)
    a_password = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'admin_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CorpusTable(models.Model):
    language_profeciency = models.CharField()
    corpus_id = models.TextField(primary_key=True)
    target_lang = models.CharField()

    class Meta:
        managed = False
        db_table = 'corpus_table'


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
    id = models.BigAutoField(primary_key=True)
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


class FileImport(models.Model):
    original_file_name = models.CharField(blank=True, null=True)
    generated_file_name = models.CharField(blank=True, null=True)
    import_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_import'


class JobTable(models.Model):
    sen_id = models.AutoField(primary_key=True)
    source_data = models.CharField()
    t_target_data = models.CharField(blank=True, null=True)
    r_target_data = models.CharField(blank=True, null=True)
    batch_id = models.IntegerField()
    minor_job_id = models.IntegerField(blank=True, null=True)
    major_job_id = models.IntegerField()
    t_flag = models.CharField(max_length=1)
    r_flag = models.CharField(max_length=1)
    corpus_id = models.TextField()
    priority = models.CharField()
    t_assigned = models.CharField(max_length=1)
    r_assigned = models.CharField(max_length=1)
    t_rating = models.IntegerField(blank=True, null=True)
    t_reviews = models.CharField(blank=True, null=True)
    r_reviews = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_table'


class MajorTable(models.Model):
    major_id = models.IntegerField(primary_key=True)
    language = models.CharField()

    class Meta:
        managed = False
        db_table = 'major_table'


class RLogTable(models.Model):
    slno = models.AutoField(primary_key=True)
    r = models.ForeignKey('ReviewerTable', models.DO_NOTHING, blank=True, null=True)
    batch_range = models.CharField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    login = models.DateTimeField(blank=True, null=True)
    logout = models.DateTimeField(blank=True, null=True)
    log_duration = models.DateTimeField(blank=True, null=True)
    module_access_timestamp = models.DateTimeField(blank=True, null=True)
    module_submission_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_log_table'


class RegistrationTable(models.Model):
    user_name = models.CharField()
    email = models.CharField(primary_key=True)
    password = models.CharField()
    user_type = models.CharField()
    language_profeciency = models.CharField()
    org_details = models.BinaryField(blank=True, null=True)
    flag = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'registration_table'


class ReviewerTable(models.Model):
    r_id = models.CharField(primary_key=True, max_length=20)
    r_name = models.CharField()
    password = models.CharField()
    email = models.CharField()
    language_profeciency = models.CharField()
    major_job_id = models.IntegerField(blank=True, null=True)
    minor_job_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    batch_range = models.CharField(blank=True, null=True)
    corpus_id = models.TextField(blank=True, null=True)
    job_assigned = models.CharField(max_length=1)
    completed_batches = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer_table'


class TLogTable(models.Model):
    slno = models.AutoField(primary_key=True)
    t_id = models.CharField(blank=True, null=True)
    batch_range = models.CharField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    login = models.DateTimeField(blank=True, null=True)
    logout = models.DateTimeField(blank=True, null=True)
    log_duration = models.DateTimeField(blank=True, null=True)
    module_access_timestamp = models.DateTimeField(blank=True, null=True)
    module_submission_timestamp = models.DateTimeField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log_table'


class TranslatorTable(models.Model):
    t_id = models.CharField(primary_key=True, max_length=20)
    t_name = models.CharField()
    password = models.CharField()
    email = models.CharField()
    language_profeciency = models.CharField()
    major_job_id = models.IntegerField(blank=True, null=True)
    minor_job_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    batch_range = models.CharField(blank=True, null=True)
    t_review = models.CharField(blank=True, null=True)
    corpus_id = models.TextField(blank=True, null=True)
    job_assigned = models.CharField(max_length=1)
    completed_batches = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'translator_table'
