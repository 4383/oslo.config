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

import yaml
from yaml.constructor import ConstructorError as BaseConstructorError
from yaml.parser import ParserError as BaseParserError
from yaml.scanner import ScannerError as BaseScannerError
from yaml.representer import RepresenterError as BaseRepresenterError
from yaml.serializer import SerializerError as BaseSerializerError


class ConstructorError(BaseConstructorError):
    pass


class ParserError(BaseParserError):
    pass


class ScannerError(BaseScannerError):
    pass


class RepresenterError(BaseRepresenterError):
    pass


class SerializerError(BaseSerializerError):
    pass


def load(stream, is_safe=True):
    try:
        if is_safe:
            return yaml.safe_load(stream)
        return yaml.load(stream)
    except BaseParserError:
        raise ParserError()
    except BaseScannerError:
        raise ScannerError()
    except BaseConstructorError:
        raise ConstructorError()


def dump(stream, is_safe=True):
    try:
        if is_safe:
            return yaml.safe_dump(stream)
        return yaml.dump(stream)
    except BaseSerializerError:
        raise SerializerError()
    except BaseRepresenterError:
        raise RepresenterError()
