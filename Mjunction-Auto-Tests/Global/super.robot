*** Settings ***
Library           SeleniumLibrary    run_on_failure=SeleniumLibrary.CapturePageScreenshot
Library           Collections
Library           FakerLibrary
Resource          common_variables.robot
Resource          ../Keywords/Web/common.robot
Resource          ../ObjectRepository/Web/buttons.robot
Resource          ../ObjectRepository/Web/checkBox.robot
Resource          ../ObjectRepository/Web/dropDown.robot
Resource          ../ObjectRepository/Web/labels.robot
Resource          ../ObjectRepository/Web/radioButton.robot
Resource          ../ObjectRepository/Web/textBox.robot
Resource          ../Keywords/Web/Login.robot
Library           ../Library/CustomLibrary.py
