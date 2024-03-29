import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Hello!</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attribute:', tree.find('email').get('hide'))
