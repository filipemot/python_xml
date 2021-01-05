import xml.etree.ElementTree as ET
import os


def create_xml(folder_export, file_name, list_cleaner ):
    """
    Create xml file
    :param str | folder_export:
        Url of folder export
    :param str | file_name:
        File name
    :param [{Cleaner}] | list_cleaner:
        List of type Cleaner with cleaner's information
    """
    root = ET.Element("root")

    create_list_results(root, list_cleaner)

    tree = ET.ElementTree(root)
    tree.write(os.path.join(folder_export,file_name), encoding='UTF-8', xml_declaration=True)

def create_list_results(root, list_cleaner):
    """
    Create child reference
    :param Object | root:
        Object reference of root xml's file
    :param [{Cleaner}] | list_cleaner:
        List of type Cleaner with cleaner's information
    """
    doc_root = ET.SubElement(root, "lista")

    for cleaner in list_cleaner:
        doc_child = ET.SubElement(doc_root, "values")
        create_child_values(doc_child, cleaner)

def create_child_values(doc_child, cleaner):
    """
    Create child values
    :param Object | doc_child:
        Object reference of child xml's file
    :param {Cleaner} | cleaner:
        The object of type Cleaner with values information
    """

    ET.SubElement(doc_child, "value1").text = str(cleaner['value1'])
    ET.SubElement(doc_child, "value2").text = str(cleaner['value2'])
    ET.SubElement(doc_child, "value3").text = str(cleaner['value3'])
    ET.SubElement(doc_child, "value4").text = str(cleaner['value4'])


def main():


    cleaner = {}
    cleaner['value1'] = "4"
    cleaner['value2'] = "5"
    cleaner['value3'] = "6"
    cleaner['value4'] = "7"

    list_cleaner = []
    list_cleaner.append(cleaner)

    cleaner = {}

    cleaner['value1'] = "4"
    cleaner['value2'] = "5"
    cleaner['value3'] = "6"
    cleaner['value4'] = "7"


    list_cleaner.append(cleaner)



    create_xml("D:\\Demos_Pessoais\\python_xml", "teste.xml" ,list_cleaner)


main()