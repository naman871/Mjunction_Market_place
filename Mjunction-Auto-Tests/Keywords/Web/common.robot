*** Settings ***
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
    Wait Until Element Is Visible    ${textbox.username.text}    ${LONG_WAIT}
    Comment    To enter username
    SeleniumLibrary.Input Text    ${textbox.username.text}    ${username}
    Comment    To enter password
    SeleniumLibrary.Input Text    ${textbox.password.text}    ${password}
    Comment    Click on login button
    SeleniumLibrary.Click Element    ${button.login}
    Comment    Validate home page is displayed

Launch Browser and navigate to URL
    [Arguments]    ${url}    ${browser_name}
    Launch Browser    ${url}    ${browser_name}
    Maximize Browser Window
    Wait Until Time    2

Select Dropdown values

Launch Browser
    [Arguments]    ${url}    ${browser_name}
    Run Keyword If    '${browser_name}'=='Chrome' or '${browser_name}'=='chrome'    SeleniumLibrary.Open Browser    ${url}    Chrome
    Run Keyword If    '${browser_name}'=='Firefox' or '${browser_name}'=='firefox'    SeleniumLibrary.Open Browser    ${url}    Firefox

Read data from Excel
    [Arguments]    ${testcaseid}    ${sheet_name}
    ${test_data}    CustomLibrary.Get Ms Excel Row Values Into Dictionary Based On Key    ${TEST_DATA_FOLDER}/TestData.xlsx    ${testcaseid}    ${sheet_name}
    Set Global Variable    ${test_data}
    [Return]    ${test_data}
