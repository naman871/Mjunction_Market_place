from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.BuiltIn import BuiltIn
import xlrd
import calendar
import time

class CustomLibrary(object):

        def __init__(self):
                pass
        @property
        def _sel_lib(self):
            return BuiltIn().get_library_instance('SeleniumLibrary')

        @property
        def _driver(self):
            return self._sel_lib.driver

        def open_chrome_browser(self,url):
            """Return the True if Chrome browser opened """
            selenium = BuiltIn().get_library_instance('SeleniumLibrary')
            try:
                options = webdriver.ChromeOptions()
                options.add_argument("disable-extensions")
                options.add_argument('--ignore-ssl-errors=yes')
                options.add_argument('--ignore-certificate-errors')
                options.add_experimental_option('prefs', {
                    'credentials_enable_service': False,
                    'profile': {
                        'password_manager_enabled': False
                    }
                })
                options.add_experimental_option("excludeSwitches",["enable-automation","load-extension"])
                selenium.create_webdriver('Chrome',chrome_options=options)
                selenium.go_to(url)
                return True
            except:
                return False
        
        def javascript_click_by_xpath(self,xpath):
            element = self._driver.find_element_by_xpath(xpath) 
            self._driver.execute_script("arguments[0].click();", element)
        
        def wait_until_time(self,arg):
            time.sleep(int(arg))

        def get_current_date(self):
            """ Returns the current date in the format month date year"""
            cdate = datetime.now()
            return cdate.strftime("%d/%m/%Y")
        
        def wait_until_element_clickable(self,locator):
            """ An Expectation for checking that an element is either invisible or not present on the DOM."""
            if locator.startswith("//") or locator.startswith("(//"):
               WebDriverWait(self._driver, 60).until(EC.element_to_be_clickable((By.XPATH, locator)))
            else:
               WebDriverWait(self._driver, 60).until(EC.element_to_be_clickable((By.ID, locator)))               
        
        def get_ms_excel_row_values_into_dictionary_based_on_key(self,filepath,keyName,sheetName=None):
            """Returns the dictionary of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            dictVar={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return dictVar
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            dictVar={}
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                rowValues=worksheet.row_values(int(rowNo))
                if str(rowValues[0])!=str(keyName):
                    continue
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    if(str(cell_data)=="" or str(cell_data)==None):
                        continue                    
                    cell_data=self.get_unique_test_data(cell_data)
                
                    dictVar[str(headersList[rowIndex])]=str(cell_data)
            return dictVar

        def get_all_ms_excel_row_values_into_dictionary(self,filepath,sheetName=None):
            """Returns the dictionary of values all row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            all_row_dict={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return all_row_dict
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                each_row_dict={}
                rowValues=worksheet.row_values(int(rowNo))
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    if(str(cell_data)=="" or str(cell_data)==None):
                        continue
                    cell_data=self.get_unique_test_data(cell_data)
                    each_row_dict[str(headersList[rowIndex])]=str(cell_data)
                all_row_dict[str(rowValues[0])]=each_row_dict
            return all_row_dict

        def get_all_ms_excel_matching_row_values_into_dictionary_based_on_key(self,filepath,keyName,sheetName=None):
            """Returns the dictionary of matching row values from the MS Excel file based on key"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            all_row_dict={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return all_row_dict
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            headersList=worksheet.row_values(int(0))
            indexValue=1
            for rowNo in range(1,int(noofrows)):
                rowValues=worksheet.row_values(int(rowNo))
                if str(rowValues[0])!=str(keyName):
                    continue
                each_row_dict={}
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    if(str(cell_data)=="" or str(cell_data)==None):
                        continue
                    cell_data=self.get_unique_test_data(cell_data)
                    each_row_dict[str(headersList[rowIndex])]=str(cell_data)
                all_row_dict[str(indexValue)]=each_row_dict
                indexValue+=1
            return all_row_dict

        def get_unique_test_data(self,testdata):
            """Returns the unique if data contains unique word """
            ts = time.strftime("%Y%m%d_%H%M%S")
            unique_string=str(ts)
            testdata=testdata.replace("UNIQUE",unique_string)
            testdata=testdata.replace("Unique",unique_string)
            testdata=testdata.replace("unique",unique_string)
            return testdata

        def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
            """Returns the True if the specified work sheets exist in the specifed MS Excel file else False"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            sStatus=False        
            if sheetName==None:
                return True
            else:
                for sname in snames:
                    if sname.lower()==sheetName.lower():
                        wsname=sname
                        sStatus=True
                        break
                if sStatus==False:
                    print ("Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: " +str(filepath))
            return sStatus



 
        
