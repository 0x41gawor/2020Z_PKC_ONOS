import requests
import json
from Model.Link import Link
from Model.Host import Host
from Model.Switch import Switch
from Model.Intent import Intent


class Connection:

    def __init__(self):
        self._url = "http://127.0.0.1:8181/onos/v1"
        self._payload = ""
        self._headers = {}

    # Return - list of Link objects
    def get_links(self):
        self._url = "http://127.0.0.1:8181/onos/v1/links"
        self._payload = ''
        self._headers = {
            'Authorization': "Basic a2FyYWY6a2FyYWY=",
            'cache-control': "no-cache",
            'Postman-Token': "5fb2a6f2-a250-4c3f-be4b-f3cc8368b497"
            }
        response = requests.request("GET", self._url, data=self._payload, headers=self._headers)
        links = json.loads(response.text)["links"]  # list of dicts
        list_of_links = []
        for var in links:  # var is a dict
            list_of_links.append(Link(var))  # Add new Link object to the list
        return list_of_links

    # Return - list of Host objects
    def get_hosts(self):
        self._url = "http://127.0.0.1:8181/onos/v1/hosts"
        self._payload = ''
        self._headers = {
            'Authorization': "Basic a2FyYWY6a2FyYWY=",
            'cache-control': "no-cache",
            'Postman-Token': "2a4b4d29-f7ae-4a18-86b5-97537009e257"
        }
        response = requests.request("GET", self._url, data=self._payload, headers=self._headers)
        hosts = json.loads(response.text)["hosts"]  # list of dicts
        list_of_hosts = []
        for var in hosts:
            list_of_hosts.append(Host(var))  # Add new Host object to the list
        return list_of_hosts

    # Return - list of Switch objects
    def get_switches(self):
        self._url = "http://127.0.0.1:8181/onos/v1/devices"
        self._payload = ''
        self._headers = {
            'Authorization': "Basic a2FyYWY6a2FyYWY=",
            'cache-control': "no-cache",
            'Postman-Token': "ea0d16b1-ec3e-4fbb-909c-1d8ebf60c8b9"
            }
        response = requests.request("GET", self._url, data=self._payload, headers=self._headers)
        devices = json.loads(response.text)["devices"]  # list of dicts
        list_of_switches = []
        for var in devices:
            list_of_switches.append(Switch(var))  # Add new Host object to the list
        return list_of_switches

    # Return - tuple(str, str, list of Intent objects)
    def get_monitored_intents(self):
        self._url = "http://127.0.0.1:8181/onos/v1/imr/imr/monitoredIntents"
        self._payload = ''
        self._headers = {
            'Authorization': "Basic a2FyYWY6a2FyYWY=",
            'cache-control': "no-cache",
            'Postman-Token': "ebe8e928-4499-41ac-ae1f-c3a8f666361a"
            }

        response = requests.request("GET", self._url, data=self._payload, headers=self._headers)
        tmp = json.loads(response.text)["response"][0]
        id = tmp["id"]
        name = tmp["name"]
        intents = tmp["intents"]
        list_of_intents = []
        for var in intents:
            list_of_intents.append(Intent(var))  # Add new Intent object to the list
        return id, name, list_of_intents
