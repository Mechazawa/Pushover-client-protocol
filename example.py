#!/usr/bin/env python
# coding=utf-8

import urllib2
import json
from urllib import urlencode
from datetime import datetime
from time import sleep

baseurl = "https://api.pushover.net/1"


class PooshyClient(object):
    def __init__(self):
        self.secret = ""
        self.device = ""
        pass

    def login(self, email, password):
        try:
            data = urlencode({"email": email, "password": password})
            response = json.load(urllib2.urlopen(baseurl + "/users/login.json", data))
            self.secret = response['secret']
        except urllib2.HTTPError:
            return False
        return True

    def registerdevice(self, name, uuid, providerdeviceid="PythonDevice", force=False):
        if not self.secret:
            raise Exception("Not authenticated")

        data = urlencode({
            "name": name, "uuid": uuid,
            "provider_device_id": providerdeviceid,
            "on_gcm": 1, "force": 1 if force else 0,
            "secret": self.secret, "os": "A"
        })
        response = json.load(urllib2.urlopen(baseurl + "/devices.json", data))
        self.device = uuid
        return response['status'] == 1

    def messages(self):
        """
        Get a list of the messages

        :return: Message
        :raise Exception:
        """
        if not self.secret:
            raise Exception("Not authenticated")
        if not self.device:
            raise Exception("No device set")

        data = urlencode({
            "secret": self.secret,
            "device_id": self.device
        })
        response = json.load(urllib2.urlopen(baseurl + "/messages.json?" + data))
        return [Message(l, self.device, self.secret) for l in response['messages']]

    def markallread(self):
        data = urlencode({
            "secret": self.secret,
            "message": 99999
        })
        return json.load(urllib2.urlopen(baseurl + "/devices/%s/update_highest_message.json" % self.device, data))['status'] == 1


class Message(object):
    def __init__(self, msg, uuid, secret):
        self.id = msg['id']
        self.message = msg['message']
        self.app = msg['app']
        self.aid = msg['aid']
        self.icon = msg['icon'] or False
        self.datetime = datetime.utcfromtimestamp(msg['date'])
        self.timestamp = msg['date']
        self.priority = msg['priority']
        self.acknowledged = msg['acked'] == 1
        self.umid = msg['umid']
        self.title = msg.get('title', False)
        self._uuid = uuid
        self._secret = secret


print "Logging in"
poosh = PooshyClient()
poosh.login("email", "password")
poosh.registerdevice("Python", "python")

while True:
    msg = poosh.messages()
    for p in msg:
        print "[%i %s] %s" % (p.id, p.title or p.app, p.message)
    poosh.markallread()
    sleep(5) # Be nice to their server
