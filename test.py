#!/usr/bin/env python
import os
import sys
import pathlib

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    env_file = os.path.join(pathlib.Path(__file__).parent.absolute(), 'core/.env.ci')
    os.environ['ENV_PATH'] = env_file
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
