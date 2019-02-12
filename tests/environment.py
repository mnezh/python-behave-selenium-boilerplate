import os
import yaml
from tests.lib import get_app


def load_config():
    file_name = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(file_name) as input:
        return yaml.load(input)


def before_all(context):
    context.config = load_config()
    context.app = get_app(context.config)


def after_all(context):
    context.app.shutdown()
