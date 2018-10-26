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

from io import FileIO
import tempfile
import textwrap
from oslotest import base

from oslo_config.utils import yaml


class ExceptionsLoadTestCase(base.BaseTestCase):

    def test_constructor_error(self):
        payload = "!!python/object/apply:os.system ['uname -a']"
        self.assertRaises(yaml.ConstructorError, yaml.load, payload)

    def test_contructor_error_false(self):
        payload = '''!!python/object/apply:os.system ['echo "hello"']'''
        result = yaml.load(payload, is_safe=False)
        self.assertEqual(0, result)

    def test_scanner_error(self):
        payload = textwrap.dedent('''
            - foo: bar
            - list:
              - [one, two]
              - {check: yaml, in: test}
            baz
        ''')
        self.assertRaises(yaml.ScannerError, yaml.load, payload)

    def test_parser_error(self):
        payload = textwrap.dedent('''
                - foo: bar
            - list:
            - [one, two]
            - {check: yaml, in: test}
        ''')
        self.assertRaises(yaml.ParserError, yaml.load, payload)


class ExceptionsDumpTestCase(base.BaseTestCase):

    def test_representer_error(self):
        class Test:
            pass
        payload = {"one": "one", "two": Test()}
        self.assertRaises(yaml.RepresenterError, yaml.dump, payload)

    def test_serializer_error(self):
        tmp_file = tempfile.TemporaryFile(mode='rb')
        #type(tmp_file)
        f = FileIO(tmp_file.name, mode='wb', closefd=True)
        payload = {'key': tmp_file.close()}
        payload = ""
        yaml.dump(payload)
        self.assertRaises(yaml.SerializerError, yaml.dump, payload, False)
