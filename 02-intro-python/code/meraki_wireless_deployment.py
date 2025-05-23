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
headers = {} # TODO: Add your Meraki API key here
org_id = "" # TODO: Add your organization ID here


def create_network():
    url = f"{baseurl}/organizations/{org_id}/networks"
    payload = {
        # TODO: Add the required payload to create a new network
    }
    response =  # TODO: Make a POST request to create a new network using requests library
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    network_id = response.json()["id"]
    # Pass the network_id to the claim_devices function
    claim_devices(network_id)


def claim_devices(network_id):
    url = f"" # TODO: Add the URI to claim devices
    payload = {

        # TODO: Add the required payload for device serials
    }
    response = # TODO: Make a POST request to claim devices
    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    # Wait for 5 seconds for the devices to be claimed in the network
    time.sleep(5)
    # Pass the serial number to the configure_ap function
    for serial in response.json()['serials']:
        configure_ap(serial)


def configure_ap(serial):
    # TODO: Complete the function to configure the AP and pass the network_id to the configure_ssid function
    #
    #

    # Pass the network_id to the configure_ssid function if device config is successful
    if response.status_code == 200:
        configure_ssid(response.json()['networkId'])
    else:
        print("Skipping SSID config due to device config failure.")


def configure_ssid(network_id):
    # TODO: Complete the function to configure the SSID and print the success message
    #
    #

    print(f"Status Code: {response.status_code} - {response.reason}")
    print(response.json())
    print("Network created successfully!!! Challenge complete! 🎉🎉🎉")


if __name__ == "__main__":
    create_network() # Start the process to create a new network