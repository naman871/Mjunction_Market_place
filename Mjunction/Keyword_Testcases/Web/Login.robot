*** Settings ***
Library           SeleniumLibrary
Library           ExcelLibrary
Resource          ../../Keywords/Web/common.robot    # This is a common keyword
Resource          ../../Global/super.robot

*** Test Cases ***
TC_01 Basic login
    Comment    Login to the Login to vedanta metalbazar application
    Login to application     ${URL}    ${BROWSERNAME}
    Comment
    Enter Username and Password    ${USER_NAME}    ${PASSWORD}
