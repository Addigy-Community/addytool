#!/usr/bin/python
# -*- coding: utf-8 -*-
"""`endpoint` is a module of addytool used to interact with Addigy's API endpoints.

    Published endpoints are abstracted in Python and designed to be useful to
    in Python. Calls to enpoints are made via :mod:`requests`, and output is
    printed as a Python types. API keys are stored using :mod:`keyring`, which
    will use keychain if on macOS.
    """

import requests, keyring, json

class Endpoint(object):
    """Use GET, POST, PUT, and DELETE methods with Addigy endpoints.

    <Subclass>.__init__ pass endpoint_url to Endpoint.__init__, and subclass
    methods pass params, json, etc.
    """
    __version = '0.0.1'

    def __init__(self, endpoint_url, client_id = None, client_secret = None):
        """Initializes variables shared across subclasses.

        Headers can be used to auth all endpoints. Base URL is consistent
        except for file manager endpoints. Concatenates base_url and endpoint
        URL to form full path to endpoint.
        """
        if client_id is None:
            client_id = str(keyring.get_password('Addigy', 'ClientID'))
        if client_secret is None:
            client_secret = str(keyring.get_password('Addigy', 'ClientSecret'))
        self.base_url = "https://prod.addigy.com/"
        self.url = str(self.base_url + endpoint_url)
        self.headers = {
            'client-id': client_id,
            'client-secret': client_secret,
            }

    def get(self, params = None, files = None):
        """Call API endpoint with GET

        Args:
            params (str): Optionally, define any parameters
        Returns:
            Python list of decoded JSON Objects. JSON Objects are converted to
            Python dictionaries.
        """

        response = requests.get(self.url, params = params, \
          headers = self.headers)
        return json.loads(response.text)

    def post(self, data = None, json_data = None):
        """Call API endpoint with POST.

        Args:
            data (str): Optionally, define any parameters
            json (str): Optionally,
        Returns:
            Python list of decoded JSON Objects. JSON Objects are converted to
            Python dictionaries.
        """

        response = requests.post(self.url, headers = self.headers, data = data, json = json_data)
        return json.loads(response.text)

    def put(self):
        """Call API endpoint with PUT.

        Args:
            data (str): Optionally, define any parameters
            json (str): Optionally,
        Returns:
            Python list of decoded JSON Objects. JSON Objects are converted to
            Python dictionaries.
        """

        response = requests.put(self.url, headers = self.headers, data = data)
        return json.loads(response.text)

    def delete(self, json_data = None):
        """Call API endpoint with DELETE.

        Args:
            data (str):
        Returns:
        """

        response = requests.delete(self.url, headers = self.headers, json = json_data)
        return json.loads(response.text)

class Alerts(Endpoint):
    'Request api/alerts endpoint with GET method'

    def __init__(self):
        'Proxies Endpoint.__init__ and initializes unique variables.'
        Endpoint.__init__(self, endpoint_url="api/alerts")

    def get(self, status = None, per_page = None, page = None):
        """List received alerts.

        Args:
            status (str): Status of the alert. Possible values are: 'Unattended',
                'Acknowledged' and 'Resolved'. By default, the call will include ALL
                the alerts.
            per_page (int): Objects to be retrieved per page. By default, the number
                of objects returned per page is 20. The maximum number of objects
                that can be retrieved per page is 100. Invalid values and values
                greater than 100 will be ignored and turned to the default.
            page (int): To scroll through the pages, add the parameter page. The
                page numbers starts with 1.
        Returns:
            Listed item output example:
                    {u'_id': u'<UUID>',
                     u'actionid': u'<UUID>',
                     u'agentid': u'<UUID>',
                     u'category': u'<CATEGORY>',
                     u'created_on': 1542693878.0,
                     u'emails': [u'jdoe@example.com'],
                     u'fact': u'Gatekeeper Enabled',
                     u'level': u'warning',
                     u'name': u'GateKeeper Disabled',
                     u'orgid': u'<UUID>',
                     u'remediationstatus': u'Done',
                     u'remenabled': True,
                     u'remtime': 15,
                     u'resolveddate': 1542693887,
                     u'resolveduseremail': u'System',
                     u'selector': u'=',
                     u'status': u'Resolved',
                     u'value': False,
                     u'valuetype': u'boolean'}
        """
        params ={}
        if status is not None:
            params['status'] = status
        if per_page is not None:
            params['per_page'] = per_page
        if page is not None:
            params['page'] = page
        return Endpoint.get(self, params=params)

    def post(self):
        '`Alerts` endpoint does not support the POST method.'
        return None

    def put(self):
        '`Alerts` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Alerts` endpoint does not support the DELETE method.'
        return None

class Applications(Endpoint):
    'Request api/applications endpoint with GET method'

    def __init__(self):
        'Proxies Endpoint.__init__ and initializes unique variables.'
        Endpoint.__init__(self, endpoint_url="api/applications")

    def get(self):
        """Get map of installed applications per device.

        Args:
            None
        Returns:
            Listed item output example:
                "installed_applications" (dict):
                    "name" (str): Name of application
                    "path" (str): Path to application
                    "version" (str): CFBundleShortVersionString value
                "agentid" (str): agentid of device
        """
        return Endpoint.get(self)

    def post(self):
        '`Applications` endpoint does not support the POST method.'
        return None

    def put(self):
        '`Applications` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Applications` endpoint does not support the DELETE method.'
        return None

class CatalogPublic(Endpoint):
    'Request api/catalog/public endpoint with GET method'

    def __init__(self):
        'Proxies Endpoint.__init__ and initializes unique variables.'
        Endpoint.__init__(self, endpoint_url = "api/catalog/public")

    def get(self):
        """Returns a list of all public software items.

        Args:
            None
        Returns:
            Listed items include:
                "user_email" (str):
                "editid" (str, NoneType):
                "software_icon" (dict):
                    "filename" (str):
                    "md5_hash" (str):
                    "id" (str):
                    "provider" (str):
                    "file_name" (str):
                    "file_path" (str):
                "instructionId" (str):
                "type" (str):
                "category" (str):
                "status_on_skipped" (str):
                "icon" (str): "/path/to/icon"
                "public" (boolean): true or false
                "run_on_success" (boolean): true or false
                "commands" (dict):
                "base_identifier" (str): typically name of software
                "description" (str): Abitrary description
                "label" (str): "Custom Software - " + name
                "condition" (str): bash script run to determine
                "downloads" (dict):
                "price_per_device" (number): unknown
                "name" (str): Name as entered into Addigy with version in
                    parentheses
                "version" (str): Version as entered into Addigy (not
                    CFBundleShortVersionstr)
                "remove_script" (str): bash script to be run upon removal from
                    policy
                "policy_restricted" (boolean): true or false
                "installation_script" (str): bash script to be run for
                    installation
                "identifier" (str): base_identier-UUID
                "provider" (str): ansible-custom-software
                "orgid" (str): orgid UUID
        """
        return Endpoint.get(self)

    def post(self):
        '`CatalogPublic` endpoint does not support the POST method.'
        return None

    def put(self):
        '`CatalogPublic` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`CatalogPublic` endpoint does not support the DELETE method.'
        return None

class CustomSoftware(Endpoint):
    'Request api/custom-software endpoint with GET and POST methods'
    def __init__(self):
        'Proxies Endpoint.__init__ and initializes unique variables.'
        Endpoint.__init__(self, endpoint_url = "api/custom-software")

    def get(self, instruction_id = None, identifier = None):
        """Get a specific or all custom software. If no arguments are given, the
            entire custom software catalog will be returned.

        Args:
            "instructionid" (str): Optionally, the instructionid of a specific
                custom software version.
            "identifier" (str): Optionally, the identifier of a custom software
                item. This will return all versions of the software.
        Returns:
            Listed items include::
                "user_email" (str):
                "editid" (str, NoneType):
                "software_icon" (dict):
                    "filename" (str):
                    "md5_hash" (str):
                    "id" (str):
                    "provider" (str):
                    "file_name" (str):
                    "file_path" (str):
                "instructionId" (str):
                "type" (str):
                "category" (str):
                "status_on_skipped" (str):
                "icon" (str): "/path/to/icon"
                "public" (bool): True or False
                "run_on_success" (boolean): True or False
                "commands" (dict):
                "base_identifier" (str): typically name of software
                "description" (str): Abitrary description
                "label" (str): "Custom Software - " + name
                "condition" (str): bash script run to determine if install will
                    run on device.
                "downloads" (dict):
                "price_per_device" (int): unknown
                "name" (str): Name as entered into Addigy with version in
                    parentheses
                "version" (str): Version as entered into Addigy (not
                    CFBundleShortVersionString)
                "remove_script" (str): bash script to be run upon removal from
                    policy
                "policy_restricted" (boolean): true or false
                "installation_script" (str): bash script to be run for
                    installation
                "identifier" (str): base_identier-UUID
                "provider" (str): ansible-custom-software
                "orgid" (str): orgid UUID
                """
        params={}
        if instruction_id is not None:
            params['instructionid'] = instruction_id
        if identifier is not None:
            params['identifier'] = identifier
        return Endpoint.get(self, params = params)

    def post(self, identifier, version, update = False, downloads = [], \
            installation_script = None, conditional_script = None, \
            removal_script = None):
        """Create a new custom software item or software version.

        The action of updating or creating a new software item is determined by
        whether the `update` argument is `True`. The identifier is sent to
        create a new version of an existing software. The base_identifier is
        used to create a brand new item.

        Args:
            identifier (str): The identifier to update the custom software item.
                To create a new version of an existing software item, set
                  `update` arg to `True` and use the appropriate `identifier`
                  key value, as reported by a GET request to this endpoint.
                To create a band new piece of custom software, ignore the
                  `update` argument (which will default to `False`), and supply
                  the name of the custom software item as the identifier.
            version (str): The version of the custom software.
            update (bool): Defaults to `False`, indicating that the software in
                question is new.
            downloads (list): The download object returned from uploading the
                software item to the file-manager.
            installation_script (str): The script that will be run to install the
                software.
            condition (str): The condition that will be checked before running the
                installation script.
            remove_script (str): The script that will be run to remove the software.
        Returns:
            Python dictionary of decoded JSON object. Example:
                {u'version': u'0.0.0',
                 u'base_identifier': u'example fifty',
                 u'instructionId': u'<UUID>',
                 u'orgid': u'<UUID>',
                 u'category': u'General',
                 u'realm': u'prod',
                 u'editid': None,
                 u'status_on_skipped': u'finished',
                 u'installation_script': None,
                 u'label': u'Custom Software - example fifty (0.0.0)',
                 u'remove_script': None,
                 u'provider': u'ansible-custom-software',
                 u'type': u'software',
                 u'public': False,
                 u'software_icon': {
                    u'file_name': u'icon',
                    u'md5_hash': u'',
                    u'filename': u'/assets/assets/img/app-store-icon.png',
                    u'provider': u'web',
                    u'id': u'/assets/assets/img/app-store-icon.png',
                    u'file_path': u'/assets/assets/img/app-store-icon.png'},
                u'description': u'',
                u'downloads': [],
                u'_id': u'<UUID>',
                u'condition': None,
                u'icon': u'/assets/assets/img/app-store-icon.png',
                u'commands': [],
                u'policy_restricted': False,
                u'name': u'example fifty (0.0.0)',
                u'price_per_device': 0.0,
                u'run_on_success': True,
                u'identifier': u'example fifty-<UUID>',
                u'user_email': u'bmorales'}
        """
        __json_data = {
            'version': version,
            'downloads': downloads,
            'installation_script': installation_script,
            'condition': conditional_script,
            'remove_script': removal_script,
            }
        if update is True:
            __json_data['identifier'] = identifier
        else:
            __json_data['base_identifier'] = identifier

        return Endpoint.post(self, json_data = __json_data)

    def put(self):
        '`CustomSoftware` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`CustomSoftware` endpoint does not support the DELETE method.'
        return None

class Devices(Endpoint):
    'Request api/devices endpoint with GET method'
    def __init__(self):
        'Initializes unique variables.'

        return Endpoint.__init__(self, endpoint_url = "api/devices")

    def get(self):
        """Get list of devices for the organization.

        Args:
            None
        Returns:
            Python list of dictionaries with varied key/value pairings of
                various types.
        """
        return Endpoint.get(self)

    def post(self):
        '`Devices` endpoint does not support the POST method.'
        return None

    def put(self):
        '`Devices` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Devices` endpoint does not support the DELETE method.'
        return None

class DevicesCommands(Endpoint):
    def __init__(self):
        'Request api/devices/commands endpoint with POST method'
        Endpoint.__init__(self, endpoint_url = "api/devices/commands")

    def post(self, agents_ids, command):
        """Run command on devices.

        Args:
            agents_ids (list of str): List of agent ids to send the commands to.
            command (str): The command to be sent to the devices.
        Returns:
            actionids (list of obj)
                agentid (str):
                actionid (str):
            jobid (str):
            _id (str):
        """
        __json_data = {
            'agents_ids': agents_ids,
            'command': command
            }
        return Endpoint.post(self, json_data = __json_data)

    def get(self):
        '`DevicesCommands` endpoint does not support the GET method.'
        return None

    def put(self):
        '`DevicesCommands` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`DevicesCommands` endpoint does not support the DELETE method.'
        return None

class DevicesOnline(Endpoint):
    'Request api/devices/online endpoint with GET method'

    def __init__(self):
        'Initialize unique variables.'
        self.endpoint_url = "api/devices/online"
        Endpoint.__init__(self, endpoint_url = "api/devices/online")

    def get(self):
        """Get devices currently online for the organization.

        Args:
            None
        Returns:
            Python list of dictionaries with varied key/value pairings of
                device facts for online devices.
        """
        return Endpoint.get(self)

    def post(self):
        '`DevicesOnline` endpoint does not support the POST method.'
        return None

    def put(self):
        '`DevicesOnline` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`DevicesOnline` endpoint does not support the DELETE method.'
        return None

class DevicesOutput(Endpoint):
    def __init__(self):
        'Request api/devices/output endpoint with GET method'
        Endpoint.__init__(self, endpoint_url = "api/devices/output")

    def get(self, actionid, agentid):
        """Get output of a command.

        Args:
            actionid (str): The Action ID of the command that was sent.
            agentid (str): The Agent ID of the device that the command was run on.
        Returns:
            stderr (str):
            stdout (str):
            exitstatus (int):
        """
        params = {
            'actionid': actionid,
            'agentid': agentid
            }

        return Endpoint.get(self, params = params)

    def post(self):
        '`DevicesOutput` endpoint does not support the POST method.'
        return None

    def put(self):
        '`DevicesOutput` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`DevicesOutput` endpoint does not support the DELETE method.'
        return None

class FileUpload(object):
    'Request https://file-manager-prod.addigy.com/api/upload/url endpoint \
    with GET method. Request resulting URL with POST method.'

    def __init__(self):
        'Initializes unique variables.'
        self.client_id = str(keyring.get_password('Addigy', 'ClientID'))
        self.client_secret = str(keyring.get_password('Addigy', 'ClientSecret'))
        self.headers = {
            'client-id': self.client_id,
            'client-secret': self.client_secret,
            }
        self.base_url = 'https://file-manager-prod.addigy.com/'
        self.endpoint_url = 'api/upload/url'
        self.url = str(self.base_url + self.endpoint_url)


    def get(self):
        """Get devices currently online for the organization.

        Args:
            None
        Returns:
            URL (str)
        """
        self.response = requests.get(self.url, headers=self.headers)
        return self.response.text[1:-1] #Splice to omit outer quotes

    def post(self, file, url = None):
        """Upload a file to Addigy.

        Args:
            file (str): path to a file on the local machine
            url (str): Optionally, a URL provided by .get().
        Returns:
            Dictionary containing data similar to the following example:
                u'{"id":<UNIQUE_ID>",
                   "orgid":"<UUID>",
                   "user_email":"<STRING>",
                   "content_type":"text/plain",
                   "filename":"upload.txt",
                   "size":6,
                   "md5_hash":"b1946ac92492d2347c6235b4d2611184",
                   "created":"<TIME_STAMP>",
                   "provider":"cloud-storage"}'
        """
        files = {'file': open(file, 'rb')}

        if url == None:
            __file_upload = FileUpload()
            url = __file_upload.get()

        self.response = requests.post(url, headers=self.headers, files=files)
        return self.response.text

    def put(self):
        '`FileUpload` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`FileUpload` endpoint does not support the DELETE method.'
        return None

class Maintenance(Endpoint):
    'Request api/maintenance endpoint with GET method'
    def __init__(self):
        'Initialize unique variables.'
        Endpoint.__init__(self, endpoint_url = "api/maintenance")

    def get(self, per_page = None, page = None):
        """List completed maintenance.

        Args:
            per_page (int): Objects to be retrieved per page. By default, the number
                of objects returned per page is 20.The maximum number of objects
                that can be retrieved per page is 100. Invalid values and values
                greater than 100 will be ignored and turned to the default.
            page (int): To scroll through the pages, add the parameter page. The
                page numbers starts with 1.
        Returns:
            Example dictionary items:
                "jobtime" (int): time in minutes to perform manually
                "trycount" (int): number of attemps
                "maxtrycount" (int): max number of attempts
                "promptuser" (bool): true or false
                "_id" (str): Device ID
                "exitcode" (int): exit code of maintenance
                "jobid" (str): jobid UUID
                "maintenancetype" (str): "maintenance",
                "scheduledtime" (str):
                "status" (str): "finished",
                "orgid" (str): "98uh65rt-74t3-oi97-yt43-67u78ujhte53",
                "actiontype" (str): "maintenance",
                "scheduled_maintenance_id" (str): "59i8liyy676499ooi8u76yt8",
                "maintenancename" (str): "Say Hello Job",
                "agentid" (str): "014x11c3-b5dy-4n38-92fb-34th6ju782st"
        """
        params = {}
        if per_page != None:
            params['per_page'] = per_page
        if page != None:
            params['page'] = page
        return Endpoint.get(self, params = params)

    def post(self):
        '`Maintenance` endpoint does not support the POST method.'
        return None

    def put(self):
        '`Maintenance` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Maintenance` endpoint does not support the DELETE method.'
        return None

class Policies(Endpoint):
    'Request api/policies endpoint with GET and POST methods'

    def __init__(self):
        'Initialize unique variables.'
        Endpoint.__init__(self, endpoint_url = "api/policies")

    def get(self):
        """Get list of policies for the organization.
        Args:
            None
        Returns:
            Listed item output example:
                "parent" (str): "98uh65rt-74t3-oi97-yt43-67u78ujhte53",
                "policyId" (str): "76yh84t0-ju74-bh45-jd6b-ok87y4gc83gt",
                "icon" (str): "fa fa-university",
                "color" (str): "#000000",
                "creation_time" (int): 1468261319,
                "download_path" (str): URL of policy"
                "name" (str): Name of Policy
                "orgid" (str): orgid UUID
        """
        return Endpoint.get(self)

    def post(self, name = None, parent_id = None, icon = 'fa fa-university', color = '#000000'):
        """Create a policy in the organization.

        Args:
            name (str): policy name
            parent_id(str): Optionally, the policy_id of the parent policy. If no
                parent_id is provided the policy will be created as root level
                policy
            icon (str): Optionally, font awesome icon for the policy. Available
                icons are: 'fa fa-user', 'fa fa-users', 'fa fa-trophy', 'fa
                fa-university', 'fa fa-database', 'fa fa-desktop', 'fa
                fa-building-o'. (Default is 'fa fa-university')
            color (str): Color for the policy icon in hex format. (Default is
                #000000)
        Returns:
            Listed item output example:
                {u'color': u'#000000',
                 u'creation_time': 1550934942,
                 u'download_path': u'https://prod.addigy.com/download/addigy_agent/<UUID>/<UUID>',
                 u'icon': u'fa fa-university',
                 u'name': u'New Policy',
                 u'orgid': u'<UUID>',
                 u'parent': None,
                 u'policyId': u'<UUID>'}
        """
        data = {
            'name': name,
            'parent_id': parent_id,
            'icon': icon,
            'color': color,
            }
        return Endpoint.post(self, data = data)

    def put(self):
        '`Policies` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Policies` endpoint does not support the DELETE method.'
        return None

class PoliciesDetails(Endpoint):
    def __init__(self):
        'Request api/alerts endpoint with GET method'
        Endpoint.__init__(self, endpoint_url = "api/policies/details")

    def get(self, policy_id, provider = 'ansible-profile'):
        """List deployed instructions details in policy

        Args:
            policy_id (string): The policy_id from which to get the details.
            provider (string): Optionally, the provider for the instruction.
                Possible values are: 'ansible-profile'.
        Returns:
            JSON(object):
                "deployed_instructions" (object):
                    "status" (string):
                    "msg" (string):
                    "instructionid" (string):
                    "orgid" (string):
                    "agentid" (string):
        """
        params={}
        params['policy_id'] = policy_id
        params['provider'] = provider

        return Endpoint.get(self, params = params)

    def post(self):
        '`PoliciesDetails` endpoint does not support the POST method.'
        return None

    def put(self):
        '`PoliciesDetails` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`PoliciesDetails` endpoint does not support the DELETE method.'
        return None

class PoliciesDevices(Endpoint):
    def __init__(self):
        'Request api/alerts endpoint with GET method'
        Endpoint.__init__(self, endpoint_url = "api/policies/devices")

    def get(self, policy_id):
        """List devices in policy

        Args:
            policy_id (string): The policy_id from which to get the devices.
        Returns:
            Python list of libraries containing device facts.
        """

        params = {
            'policy_id': policy_id,
            }

        return Endpoint.get(self, params = params)

    def post(self, policy_id, agent_id):
        """Add device to a policy. If device already in a policy the policy will be overridden.

        Args:
            policy_id (str): The poicy id to which the device will be assigned.
            agent_id (str): The agent id of the device which should be assigned.
        Returns:
            Empty string.
        """
        data = {
            'policy_id': policy_id,
            'agent_id': agent_id,
            }
        return Endpoint.post(self, data = data)

    def put(self):
        '`PoliciesDevices` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`PoliciesDevices` endpoint does not support the DELETE method.'
        return None

class PoliciesInstructions(Endpoint):
    def __init__(self):
        'Request api/alerts endpoint with GET method'
        Endpoint.__init__(self, endpoint_url = "api/policies/instructions")

    def get(self, policy_id, provider = 'ansible-profile'):
        """List instructions in policy

        Args:
            policy_id (str): The policy_id from which to get the details.
            provider (str): Optionally, the provider for the instruction.
                Possible values are: 'ansible-profile'.
        Returns:
            Python list of dictionaries with varied key/value pairings of
                various types.
        """

        params = {
            'policy_id': policy_id,
            'provider': provider
            }

        return Endpoint.get(self, params = params)

    def post(self, policy_id, instruction_id):
        """Add instruction to a policy. This endpoint accepts parameters in JSON
            format.

        Args:
            policy_id (str): The policy_id of the policy to which the instruction
                will be assigned.
            instruction_id (str): The instruction_id which will be assigned.
        Returns:
            (str): Instruction already in policy
            (str): ok
        """
        __json_data = {
            'policy_id': policy_id,
            'instruction_id': instruction_id,
            }
        return Endpoint.post(self, json_data = __json_data)

    def delete(self, policy_id, instruction_id):
        """Remove instruction from a policy

        Args:
            policy_id (str): The policy_id of the policy from which to remove
                the instruction from.

            instruction_id (str): The instruction_id for the instruction to be
                removed from the policy.
        Returns:
            'ok'
        """
        __json_data = {
            'policy_id': policy_id,
            'instruction_id': instruction_id,
            }

        return Endpoint.delete(self, json_data = __json_data)

    def put(self):
        '`PoliciesInstructions` endpoint does not support the PUT method.'
        return None

class Profiles(Endpoint):
    'Request api/profiles endpoint with GET method'
    def __init__(self):
        'Initialize unique variables.'
        Endpoint.__init__(self, endpoint_url = "api/profiles")

    def get(self, __instruction_id = None):
        """Get list of profiles for the organization. If instruction_id is
            passed as GET parameter, returns only that instruction.

        Args:
            instruction_id (string): Optionally, return only that instruction
        Returns:
            Varied key/value pairings of various types.
        """
        if __instruction_id is not None:
            params ={
                'instruction_id': __instruction_id
                }

        return Endpoint.get(self, __instruction_id)

    def delete(self, instruction_id = None):
        """Delete profile

        Args:
            instruction_id (str): Instruction ID of the profile to delete.
        Returns:
            'ok' or 'Instruction not found'
        """

        __json_data = {
            'instruction_id': instruction_id,
            }

        return Endpoint.delete(self, json_data = __json_data)

    def post(self, ):
        """See: 'https://addigy.freshdesk.com/support/solutions/articles/8000057842'

        """

class Validate(Endpoint):
    'Test API Token Authentication'
    def __init__(self, client_id = None, client_secret = None):
        'Initializes unique variables.'
        __client_id = client_id
        __client_secret = client_secret
        Endpoint.__init__(self, endpoint_url="api/validate", \
          client_id = __client_id, client_secret = __client_secret)

    def post(self):
        """Test if client_id and client_secret properly authenticate

        Args:
            None
        Returns:
            True or False
        """
        self.response = requests.post(self.url, headers=self.headers)
        if str(self.response.status_code) == '200':
            return True
        else:
            # print(str(self.response.status_code) + ': ' + self.response.text)
            return False

    def get(self):
        '`Validate` endpoint does not support the GET method.'
        return None

    def put(self):
        '`Validate` endpoint does not support the PUT method.'
        return None

    def delete(self):
        '`Volidate` endpoint does not support the DELETE method.'
        return None