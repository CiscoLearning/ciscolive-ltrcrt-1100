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
from prettytable import PrettyTable

baseurl = "https://api.meraki.com/api/v1"
headers = {'Authorization': 'Bearer 865f9754864292ccfe17354d4caf35db8ac5563c'}
orgid = "" # Step 1 - Identify the OrgId and add it here
neworkid = "" # Step 2 - Identify the networkId and add it here

url = f"{baseurl}/organizations/{orgid}/networks/{neworkid}/devices"


def get_meraki_devices():
    response = # Step 3 - Make a GET request to the URL
               #
               #
    devices = response.json()
    device_info = []
    for device in devices:
        device_info.append({
            "name": device["name"],
            "serial": device["serial"],
            "mac": device["mac"],
            "model": device["model"]
        })
    # Step 4 - call the print_report function to print the report
    #
    #

def print_report(devices):
    table = PrettyTable()
    table.field_names = ["Name", "Serial", "Mac", "Model", ]
    for device in devices:
        table.add_row(
            [device["name"],
             device["serial"],
             device["mac"],
             device["model"]]
        )
    print(table)


if __name__ == "__main__":
    get_meraki_devices()