# addytool: An API Wrapper for Addigy

Beware: `addytool` is a beta tool with capacity to do great harm to your Addigy environment. You are responsible for your own actions!

To more easily leverage Addigy's API, `addytool` abstracts the details of the API to allow admins to treat endpoints as Python objects. 

## Requirements
`addytool` stores your API creds in macOS's keychain using `keyring`. You'll also need `requests`. Both can be acquired through `pip`, untill `addytool` itself is in pip.

To get `pip`, run `sudo easy_install pip`.

Then...
`pip install --user keyring`
`pip install --user requests`


