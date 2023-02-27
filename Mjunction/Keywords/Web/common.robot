*** Settings ***
Library           SeleniumLibrary
Library           ExcelLibrary
Resource          ../../Global/super.robot

*** Keywords ***
Login to application
    [Arguments]    ${user_name}    ${password}
    Comment    To launch the browser and navigate to the url
    Launch Browser and navigate to URL    ${URL}    ${BROWSERNAME}
    Comment    To Enter username and password
    Enter Username and Password    ${user_name}    ${password}

Enter Username and Password
    [Arguments]    ${username}    ${password}
    Comment    To enter username
    SeleniumLibrary.Input Text    ${textbox.username.text}    ${username}
    Comment    To enter password
    SeleniumLibrary.Input Text    ${textbox.password.text}    ${password}
    Comment    Click on login button
    SeleniumLibrary.Click Element    ${button.login}
    Comment    Validate home page is displayed

Launch Browser and navigate to URL
    [Arguments]    ${url}    ${browser_name}
    Comment    To launch the browser
    Open Browser    ${url}    ${browser_name}
    Comment    To Maximize the browser window
    Maximize Browser Window

Select Dropdown values
