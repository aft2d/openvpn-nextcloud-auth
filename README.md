# OpenVPN Nextcloud auth

This is a small script that allows authentication of OpenVPN clients against an NextCloud instance.
(May also work with Owncloud, but never tested)


## Setup
### Script
Place the openvpn-nextcloud-auth.py script into the working directory of your OpenVPN server and configure the `base_url` in the script.

### OpenVPN
With the auth-user-pass-verify setting you can instruct OpenVPN to call this script each time a client tries to authenticate.
There are two ways how OpenVPN publishes the clients credentials to the script. Either with environment variables or with a temporary file.
The script supports both methods.

Update your OpenVPN configuration:

**Environment variables**:
```
auth-user-pass-verify openvpn-nextcloud-auth.py via-env
script-security 3
```
Adjusting the `script-security` setting is mandatory if you use the "environment variable" way, see https://community.openvpn.net/openvpn/ticket/747


**Temporary file**: (Recommended)
```
auth-user-pass-verify openvpn-nextcloud-auth.py via-file
```
