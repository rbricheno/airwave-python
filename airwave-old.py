import requests
import xml.etree.ElementTree as etree

airwave_user="myapiuser"
airwave_password="TopSecret"
airwave_url="https://airwave.my.domain.com"

def airwave_get(xml_file):
    payload = {'destination': '/' + xml_file,
               'next_action': '',
               'credential_0': airwave_user,
               'credential_1': airwave_password}
    r = requests.post(airwave_url + '/LOGIN', verify=False, data=payload)

    return etree.fromstring(r.text)

folder_list_root = airwave_get('folder_list.xml')

folders = []
for child in folder_list_root:
    folder_id = child.attrib['id']
    folder_name = child.findall('name')[0].text

    try:
        folder_parent_id = child.findall('parent_id')[0].text
    except IndexError:
        folder_parent_id = None

    print('folder_id: ' + str(folder_id) + ', folder_name: ' + str(folder_name) + ', folder_parent_id: ' + str(folder_parent_id))

