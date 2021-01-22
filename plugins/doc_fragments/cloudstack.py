# -*- coding: utf-8 -*-

# Copyright (c) 2015, René Moser <mail@renemoser.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard cloudstack documentation fragment
    DOCUMENTATION = r'''
options:
  api_key:
    description:
      - API key of the CloudStack API.
      - If not given, the C(CLOUDSTACK_KEY) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
    type: str
  api_secret:
    description:
      - Secret key of the CloudStack API.
      - If not set, the C(CLOUDSTACK_SECRET) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
    type: str
  api_url:
    description:
      - URL of the CloudStack API e.g. https://cloud.example.com/client/api.
      - If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
    type: str
  api_http_method:
    description:
      - HTTP method used to query the API endpoint.
      - If not given, the C(CLOUDSTACK_METHOD) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
      - Fallback value is C(get) if not specified.
    type: str
    choices: [ get, post ]
    default: get
  api_timeout:
    description:
      - HTTP timeout in seconds.
      - If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
      - Fallback value is 10 seconds if not specified.
    type: int
    default: 10
  api_region:
    description:
      - Name of the ini section in the C(cloustack.ini) file.
      - If not given, the C(CLOUDSTACK_REGION) env variable is considered.
    type: str
    default: cloudstack
  api_verify_ssl_cert:
    description:
      - CA authority cert file.
      - If not given, the C(CLOUDSTACK_VERIFY) env variable is considered.
      - As the last option, the value is taken from the ini config file, also see the notes.
      - Fallback value is C(null) if not specified.
    type: str
requirements:
  - python >= 2.6
  - cs >= 0.9.0
notes:
  - Ansible uses the C(cs) library's configuration method if credentials are not
    provided by the arguments C(api_url), C(api_key), C(api_secret).
    Configuration is read from several locations, in the following order.
    The C(CLOUDSTACK_ENDPOINT), C(CLOUDSTACK_KEY), C(CLOUDSTACK_SECRET) and
    C(CLOUDSTACK_METHOD). C(CLOUDSTACK_TIMEOUT) environment variables.
  - A detailed guide about cloudstack modules can be found in the L(CloudStack Cloud Guide,../scenario_guides/guide_cloudstack.html).
  - This module supports check mode.
'''
