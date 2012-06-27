# -*- coding: utf-8 -*- 

import xml.dom.minidom

def getchild(root, level):
	print root.tagName
	for node in root.childNodes:
		if node.nodeType == node.ELEMENT_NODE:
			print "  "*level,
			i = level + 1
			getchild(node, i)




if __name__ == "__main__":

	dom = xml.dom.minidom.parse("pmc_sample.xml")
#	print dom.documentElement.tagName
	getchild(dom.documentElement, 0)

#    print dom.documentElement.tagName
#    for node in dom.documentElement.childNodes:
#        if node.nodeType == node.ELEMENT_NODE:
#            print "  " + node.tagName
#
#            for node2 in node.childNodes:
#                if node2.nodeType == node2.ELEMENT_NODE:
#                    print "    " + node2.tagName
#
#                    for node3 in node2.childNodes:
#                        if node3.nodeType == node3.TEXT_NODE:
#                            print "      " + node3.data
	print ""

	for url in dom.getElementsByTagName("url"):
		print url.firstChild.data
