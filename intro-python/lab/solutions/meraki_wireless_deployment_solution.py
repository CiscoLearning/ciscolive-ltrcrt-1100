#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import time

baseurl = "https://api.meraki.com/api/v1"
headers = {'Authorization': 'Bearer 865f9754864292ccfe17354d4caf35db8ac5563c'}
org_id = "646829496481091262"


def create_network():
    url = f"{baseurl}/organizations/{org_id}/networks"
    payload = {
        "name": "Pod-99-Iskander",
        "productTypes": [
            "wireless"
        ],
        "tags": ["foo", "bar"],
        "timeZone": "America/Los_Angeles",
        "notes": "Creating a new network for Guest wireless"
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    network_id = response.json()["id"]
    # Pass the network_id to the claim_devices function
    claim_devices(network_id)


def claim_devices(network_id):
    url = f"{baseurl}/networks/{network_id}/devices/claim"
    payload = {
        "serials": [
            "QBSC-QMZT-CH57"
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    # Wait for 5 seconds for the devices to be claimed in the network
    time.sleep(5)
    # Pass the serial number to the configure_ap function
    for serial in response.json()['serials']:
        configure_ap(serial)


def configure_ap(serial):
    url = f"{baseurl}/devices/{serial}"
    payload = {
        "name": "Iskander-AP",
        "tags": [" recently-added "],
        "address": "1600 Pennsylvania Ave, DC",
        "notes": "This AP will be used for isolated guest wifi",
        "moveMapMarker": True
    }
    response = requests.put(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    # Pass the network_id to the configure_ssid function
    configure_ssid(response.json()['networkId'])


def configure_ssid(network_id):
    url = f"{baseurl}/networks/{network_id}/wireless/ssids/0"
    payload = {
        "number": 0,
        "name": "Guest WiFi",
        "enabled": True,
        "splashPage": "None",
        "ssidAdminAccessible": False,
        "radiusAccountingEnabled": False
    }
    response = requests.put(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    print("Network created successfully!!! Challenge complete! 🎉🎉🎉")


if __name__ == "__main__":
    create_network()