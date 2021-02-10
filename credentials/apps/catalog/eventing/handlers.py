import logging
from datetime import datetime

from django.contrib.sites.models import Site

from ..models_api import (
    create_or_update_course,
    create_or_update_courserun,
    create_or_update_organization,
    create_or_update_program,
    delete_course,
    delete_courserun,
    delete_organization,
    delete_program,
)

log = logging.getLogger(__name__)

###
def discovery_course_change_handler(msg):
    course = msg.value()
    log.info(f"discovery_course_change_handler:: {course}")
    create_or_update_course(
        uuid=course.uuid,
        key=course.key,
        title=course.title,
        authoring_organizations=course.authoring_organizations,
    )

def discovery_course_delete_handler(msg):
    course = msg.value()
    log.info(f"discovery_course_delete_handler:: {course}")
    delete_course(course.uuid)

###
def discovery_courserun_change_handler(msg):
    courserun = msg.value()
    log.info(f"discovery_courserun_change_handler:: {courserun}")

    create_or_update_courserun(
        uuid=courserun.uuid,
        title=courserun.title,
        key=courserun.key,
        start_date=datetime.fromtimestamp(courserun.start_date),
        end_date=datetime.fromtimestamp(courserun.end_date),
    )

def discovery_courserun_delete_handler(msg):
    courserun = msg.value()
    log.info(f"discovery_courserun_delete_handler:: {courserun}")
    delete_courserun(courserun.uuid)

###
def discovery_organization_change_handler(msg):
    organization = msg.value()
    log.info(f"discovery_organization_change_handler:: {organization}")
    create_or_update_organization(
        uuid=organization.uuid,
        key=organization.key,
        name=organization.name,
        certificate_logo_image_url=organization.certificate_logo_url
    )

def discovery_organization_delete_handler(msg):
    organization = msg.value()
    log.info(f"discovery_organization_delete_handler:: {organization}")
    delete_organization(organization.uuid)

###
def discovery_program_change_handler(msg):
    program = msg.value()
    log.info(f"discovery_program_change_handler:: {program}")
    create_or_update_program(
        uuid=program.uuid,
        title=program.title,
        course_runs=program.course_runs,
        authoring_organizations=program.authoring_organizations,
        type=program.type_localized,
        type_slug=program.type_slug,
        total_hours_of_effort=program.hours_of_effort,
        status=program.status
    )

def discovery_program_delete_handler(msg):
    program = msg.value()
    log.info(f"discovery_program_delete_handler:: {program}")
    delete_program(program.uuid)
