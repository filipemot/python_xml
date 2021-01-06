
# Criação de Xml com python

As vezes surge a necessidade de criar um arquivo XML, essa criação com o Python é feita de maneira bem simples. Criei um código simples para exemplificar como criar um arquivo xml com uma determinada estrutura.

No exemplo iremos mostrar como criar um xml com a seguinte estrutura:

    <?xml version="1.0" encoding="UTF-8"?>  
    <root>  
	    <lista>  
		    <values>  
			    <value1>4</value1>  
			    <value2>5</value2>  
			    <value3>6</value3>  
			    <value4>7</value4>  
			</values>  
			<values>  
				<value1>4</value1>  
				<value2>5</value2>  
				<value3>6</value3>  
				<value4>7</value4>  
			</values>  
		</lista>  
	</root>

Para criar o xml iremos utiliza a a biblioteca do python xml.etree.ElementTree. No código temos três funções que serão necessárias para criação do xml. Abaixo segue a responsabilidade de cada método: 


**create_xml -** Método "main" para criação do xml, esse método tem a função de chamar o método create_list_results e de gravar o arquivo xml



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

**create_list_results -** Tem a função de criar o "nó" lista e chamar o método create_child_values

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

**create_child_values** - Tem a função de criar o "nó" values 

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

Para criar o xml iremos chamar a função create_xml, passando a pasta que será importada e a lista de dados

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

Após executar será criado na pasta D:\\Demos_Pessoais\\python_xml um arquivo xml, como o nome teste.xml

