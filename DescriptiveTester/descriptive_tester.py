from typing import Optional
import pandas as pd
import json

class DescriptiveTester:
    '''
        Provides utilities to perform excel based descriptive api testing.
    '''
    
    def __init__(self, excel_path: str, data_path: str, 
                    config_path: Optional[str] = None, 
                    variables_path: Optional[str] = None) -> None:
        '''
            Args:
            ----
            - excel_path: Full path to the excel file.
            - data_path: Full path to the data directory containing header, 
                body & expected output.
            - config_path: Full path to the configuration file.
            - variables_path: Full path to the variables file.
            
            Returns:
            -------
            - None
        '''
        
        #? Getting Excel File
        self.__excel = pd.read_excel(excel_path)
        
        #? Setting Data Folder Path
        self.__data_dir = data_path
        
        #? Reading Configs if Provided
        self.__configs = {}
        self.__has_configs = False
        if config_path is not None:
            self.__has_configs = True
            with open(config_path, 'r') as ro:
                self.__configs = json.load(ro)
        
        #? Reading Variables
        self.__variables = {}
        self.__has_variables = False
        if variables_path is not None:
            self.__has_variables = True
            with open(variables_path, 'r') as ro:
                self.__variables = json.load(ro)
        