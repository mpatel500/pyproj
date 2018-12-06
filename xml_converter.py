from xml.dom import minidom

class XmlConverter():

    def __init__(self):
        self.__data = {}
        self.__mydoc = minidom.parse('project.xml')
        self.__items = self.__mydoc.getElementsByTagName("Cube")
        self.__length = len(self.__items)
    
    def get_xml_item_number(self):
        return self.__length -1
    
    def get_dictionary_size(self):
        return len(self.__data)
    
    def get_dictionary(self):
        return self.__data

    def make_dict_from_xml(self):
        i = 1
        while i < self.__length:
            line = ({self.__items[i].attributes['currency'].value : float(self.__items[i].attributes['rate'].value)})
            self.__data.update(line)
            i += 1
        return self.__data

    def get_value_using_key_from_dict(self,symbol):
        return self.__data[str(symbol)]

    


'''
info = XmlConverter()
print(info.make_dic_from_xml())
'''
            

