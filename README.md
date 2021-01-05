
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

 - create_xml - Método "main" para criação do xml, esse método tem a função de chamar o método create_list_results e de gravar o arquivo xml
 - create_list_results - Tem a função de criar o "nó" lista e chamar o método create_child_values
 -  create_child_values - Tem a função de criar o "nó" values 

O formato dos dados para o exemplo será:

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

Para criar o xml iremos chamar a função create_xml, passando a pasta que será importada e a lista de dados

    create_xml("D:\\Demos_Pessoais\\python_xml" , list_cleaner)

