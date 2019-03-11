#!/usr/bin/python
# -*- coding: utf-8 -*-
"""`workflow` leverages the endpoint module to complete common tasks.


    """

import endpoint, keyring, getpass

def authenticate():
    """"Validates token or provides two opportunities to update
    Keychain credentials in the case of a failed authentication.
    """

    validate = endpoint.Validate()

    if validate.post() is True:
        return True
    else:
        print('Addigy API tokens either invalid or non-existent. Gathering now...')
        for attempt in range(0, 2):
            client_id = getpass.getpass(prompt='Client ID: ')
            client_secret = getpass.getpass(prompt='Client Secret: ')
            validate = endpoint.Validate(client_id, client_secret)
            if validate.post() is True:
                keyring.set_password('Addigy', 'ClientID', client_id)
                keyring.set_password('Addigy', 'ClientSecret', client_secret)
                return True
            else:
                print('Authentication failed.')

        return False
