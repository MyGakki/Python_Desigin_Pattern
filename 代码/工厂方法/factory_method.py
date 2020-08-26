# coding=utf-8
# author='HopePower'
# time='2020/7/26 22:59'
import xml.etree.ElementTree as etree
import json


class JSONConnector(object):
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(object):
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('无法连接到{}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve
    return factory


def main():
    # splite_factory = connect_to('data/person.sq3')
    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                     'lastName', 'Liar'))
    print 'found: {} persons'.format(len(liars))
    for liar in liars:
        print 'first name: {}'.format(liar.find('firstName').text)
        print 'last name: {}'.format(liar.find('lastName').text)
        for p in liar.find('phoneNumbers'):
            print 'phone number ({}):'.format(p.attrib['type']), p.text

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print 'found: {} donuts'.format(len(json_data))
    for dount in json_data:
        print 'name'.format(dount['name'])
        print 'price: ${}'.format(dount['ppu'])
        for t in dount['topping']:
            print 'topping: {} {}'.format(t['id'], t['type'])


if __name__ == '__main__':
    main()
