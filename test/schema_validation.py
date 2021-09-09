import unittest

from jsonschema import validate

import mock
from logical.schema import schema


class TestSchemaValidation(unittest.TestCase):

    def test_parse_file(self):
        validate(instance=mock.site, schema=schema)


if __name__ == '__main__':
    unittest.main()
