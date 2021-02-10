import logging
import re
import threading

import pulsar
from pulsar.schema.schema import JsonSchema

from ..models import CourseRun, Course, Organization, Program
from .handlers import (
    discovery_course_change_handler,
    discovery_course_delete_handler,
    discovery_courserun_change_handler,
    discovery_courserun_delete_handler,
    discovery_organization_change_handler,
    discovery_organization_delete_handler,
    discovery_program_change_handler,
    discovery_program_delete_handler,
)
from .schema import (
    CourseSchema,
    CourseRunSchema,
    OrganizationSchema,
    ProgramSchema
)

log = logging.getLogger(__name__)

TOPIC_HANDLERS = [
    ("discovery_course_change", discovery_course_change_handler, CourseSchema),
    ("discovery_course_delete", discovery_course_delete_handler, CourseSchema),
    ("discovery_courserun_change", discovery_courserun_change_handler, CourseRunSchema),
    ("discovery_courserun_delete", discovery_courserun_delete_handler, CourseRunSchema),
    ("discovery_organization_change", discovery_organization_change_handler, OrganizationSchema),
    ("discovery_organization_delete", discovery_organization_delete_handler, OrganizationSchema),
    ("discovery_program_change", discovery_program_change_handler, ProgramSchema),
    ("discovery_program_delete", discovery_program_delete_handler, ProgramSchema),
]

def event_listener(topic, handler, schema):
    client = pulsar.Client("pulsar://edx.devstack.pulsar:6650")
    consumer = client.subscribe(
        topic=topic,
        subscription_name=f"creds-disco-sub-{topic}",
        schema=JsonSchema(schema)
    )
    while True:
        msg = consumer.receive()
        handler(msg)
        consumer.acknowledge(msg)
    client.close()

for (topic, handler, schema) in TOPIC_HANDLERS:
    event_thread = threading.Thread(target=event_listener, args=(topic, handler, schema), daemon=True)
    event_thread.start()
