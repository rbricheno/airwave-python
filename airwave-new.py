import requests
import xml.etree.ElementTree as etree

airwave_user="myapiuser"
airwave_password="TopSecret"
airwave_url="https://airwave.my.domain.com"

def airwave_get_tokens():
    session = requests.Session()
    payload = {'destination': '/',
               'login': 'Log In',
               'credential_0': airwave_user,
               'credential_1': airwave_password}
    r = session.post(airwave_url + '/LOGIN', verify=False, data=payload)
    return session.cookies, r.headers['X-BISCOTTI']

def airwave_get_xml(cookies, biscotti, xml):
    headers = {'Content-Type': 'application/xml',
               'X-BISCOTTI': biscotti}
    r = requests.get(airwave_url + '/' + xml, verify=False, cookies=cookies, headers={'X-BISCOTTI': biscotti})
    print(r.status_code)
    print(r.text)
    return etree.fromstring(r.text)

cookies, delicious_biscotti = airwave_get_tokens()

folder_list_root = airwave_get_xml(cookies, delicious_biscotti, 'folder_list.xml')

folders = []
for child in folder_list_root:
    folder_id = child.attrib['id']
    folder_name = child.findall('name')[0].text

    try:
        folder_parent_id = child.findall('parent_id')[0].text
    except IndexError:
        folder_parent_id = None

    print('folder_id: ' + str(folder_id) + ', folder_name: ' + str(folder_name) + ', folder_parent_id: ' + str(folder_parent_id))

