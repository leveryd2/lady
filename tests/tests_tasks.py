# coding:utf-8
import unittest
import json
from tasks import collect_service_info


class TasksTestCase(unittest.TestCase):

    def test_collect_service_info(self):
        result = collect_service_info.delay('{"target":"127.0.0.1","options":"-n -P0 -p 80,5000,8080"}').get()
        jsondata = json.loads(result)
        self.assertTrue(len(jsondata) > 0)

