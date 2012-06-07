from xml.etree import ElementTree
filename = 'pmc_sample.xml'
tree = ElementTree.parse(filename)
abstract = tree.getroot().findall('.//abstract/p')
for p in abstract:
  print p.text
