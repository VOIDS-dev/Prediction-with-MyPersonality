
import xml.etree.ElementTree

from xml.dom.minidom import *
from userData import user
import xml.dom.minidom as Dom 

def outputResult(singleUser, outputFile):
    
    doc = Dom.Document() 
    root_node = doc.createElement("") 
    root_node.setAttribute("user id", singleUser.id)
    root_node.setAttribute("age_group", singleUser.age_group)
    root_node.setAttribute("gender", str(singleUser.gender))
    root_node.setAttribute("extrovert", str(singleUser.extrovert))
    root_node.setAttribute("neurotic", str(singleUser.neurotic))
    root_node.setAttribute("agreeable", str(singleUser.agreeable))
    root_node.setAttribute("conscientious", str(singleUser.conscientious))
    root_node.setAttribute("open", str(singleUser.open))
    doc.appendChild(root_node)

    f = open(outputFile + "/" +singleUser.id+ ".xml" , "w") 
    root_node.writexml(f,addindent='', newl='\n') 
    f.close() 

    
    
    return
    