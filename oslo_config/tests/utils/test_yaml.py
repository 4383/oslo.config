#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import textwrap
from oslotest import base

from oslo_config.utils import yaml


class ExceptionsTestCase(base.BaseTestCase):

    def test_constructor_error(self):
        payload = "!!python/object/apply:os.system ['uname -a']"
        with self.assertRaises(yaml.ConstructorError):
            yaml.load(payload)

    def test_contructor_error_false(self):
        payload = '''!!python/object/apply:os.system ['echo "Hello"']'''
        result = yaml.load(payload, is_safe=False)
        self.assertEqual('Hello', result)

    def test_parser_error(self):
        payload = textwrap.dedent('''
            - foo: bar
            - list: 
              - [one, two]
              - {check: yaml, in: test}
            baz
        ''')
        with self.assertRaises(yaml.ParserError):
            yaml.load(payload)
