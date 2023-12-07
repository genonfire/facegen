#!/usr/bin/env python
import os
from xml.etree import ElementTree as ET


def generate_xml(path):
    record = ET.Element('record')

    ET.SubElement(
        record,
        'boolean',
        attrib={
            'id': 'preload',
            'value': 'false'
        }
    )
    ET.SubElement(
        record,
        'boolean',
        attrib={
            'id': 'amap',
            'value': 'false'
        }
    )
    maps = ET.SubElement(
        record,
        'list',
        attrib={
            'id': 'maps'
        }
    )

    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith('.png'):
                name = entry.name.split('.png')[0]
                path = 'graphics/pictures/person/%s/portrait' % name

                ET.SubElement(
                    maps,
                    'record',
                    attrib={
                        'from': name,
                        'to': path
                    }
                )

                print(entry.name)

    ET.indent(record)
    ET.ElementTree(record).write('./config.xml')


if __name__ == '__main__':
    print('### Generating XML ###\n')
    generate_xml('./')
    print('\nDone.')
