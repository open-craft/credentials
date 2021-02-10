from django.contrib.sites.models import Site

from .models import Course, CourseRun, Organization, Program

###
def create_or_update_course(uuid, **kwargs):
    authoring_org_uuids = kwargs.get("authoring_organizations")
    authoring_orgs = Organization.objects.filter(uuid__in=authoring_org_uuids)
    del kwargs["authoring_organizations"]

    obj, _ = Course.objects.update_or_create(
        site=Site.objects.get(id=1),
        uuid=uuid,
        defaults=kwargs
    )
    obj.owners.set(authoring_orgs)

def delete_course(uuid):
    Course.objects.get(uuid=uuid).delete()

###
def create_or_update_courserun(uuid, **kwargs):
    obj, created = CourseRun.objects.update_or_create(
        site=Site.objects.get(id=1),
        uuid=uuid,
        defaults=kwargs
    )

def delete_courserun(uuid):
    CourseRun.objects.get(uuid=uuid).delete()

###
def create_or_update_organization():
    obj, created = Organization.objects.update_or_create(
        site=Site.objects.get(id=1),
        uuid=uuid,
        defaults=kwargs
    )

def delete_organization(uuid):
    Organization.objects.get(uuid=uuid).delete()

###
def create_or_update_program(uuid, **kwargs):
    course_run_uuids = kwargs.get("course_runs")
    course_runs = CourseRun.objects.filter(uuid__in=course_run_uuids)
    del kwargs["course_runs"]

    authoring_org_uuids = kwargs.get("authoring_organizations")
    authoring_orgs = Organization.objects.filter(uuid__in=authoring_org_uuids)
    del kwargs["authoring_organizations"]

    obj, _ = Program.objects.update_or_create(
        site=Site.objects.get(id=1),
        uuid=uuid,
        defaults=kwargs
    )

    obj.course_runs.set(course_runs)
    obj.authoring_organizations.set(authoring_orgs)

def delete_program(uuid):
    Program.objects.get(uuid=uuid).delete()
