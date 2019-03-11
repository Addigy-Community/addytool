#!/usr/bin/python
# -*- coding: utf-8 -*-
"""a Python package for managing Addigy more intelligently.

Copyright 2019 Cirrus Partners, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import endpoint, workflow

def __init__():
    """Runs validates tokens or provides two opportunities to update
    Keychain credentials in the case of a failed authentication.
    """

    if workflow.authenticate() is not True:
        warning = """WARNING: FAILED TO AUTHENTICATE!

        addytool will likely not function properly.
        """
        print(warning)

__init__()
