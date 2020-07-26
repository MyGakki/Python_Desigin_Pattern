# coding=utf-8
# author='HopePower'
# time='2020/7/26 22:59'
import xml.etree.ElementTree as etree
import json


class JSONConnector(object):
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
