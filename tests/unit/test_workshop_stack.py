import json
import pytest

from aws_cdk import core
from workshop.workshop_stack import WorkshopStack


def get_template():
    app = core.App()
    WorkshopStack(app, "workshop")
    return json.dumps(app.synth().get_stack("workshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
