import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.repo_name }}'

namespace = '{{ cookiecutter.namespace }}'


if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)
    sys.exit(1)


if not re.match(MODULE_REGEX, namespace):
    print('ERROR: %s is not a valid Python namespace name!' % namespace)
    # exits with status 1 to indicate failure
    sys.exit(1)
