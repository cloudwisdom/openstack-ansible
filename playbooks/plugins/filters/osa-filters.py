# Copyright 2015, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# (c) 2015, Kevin Carter <kevin.carter@rackspace.com>

import hashlib


"""Filter usage:

Simple filters that may be useful from within the stack
"""


def bit_length_power_of_2(value):
    """Return the smallest power of 2 greater than a numeric value.

    :param value: Number to find the smallest power of 2
    :type value: ``int``
    :returns: ``int``
    """
    return 2 ** (int(value) - 1).bit_length()


def string_2_int(string):
    """Return the an integer from a string.

    The string is hashed, converted to a base36 int, and the modulo of 10240
    is returned.

    :param string: string to retrieve an int from
    :type string: ``str``
    :returns: ``int``
    """
    # Try to encode utf-8 else pass
    try:
        string = string.encode('utf-8')
    except AttributeError:
        pass
    hashed_name = hashlib.sha256(string).hexdigest()
    return int(hashed_name, 36) % 10240


class FilterModule(object):
    """Ansible jinja2 filters."""

    @staticmethod
    def filters():
        return {
            'bit_length_power_of_2': bit_length_power_of_2,
            'string_2_int': string_2_int
        }