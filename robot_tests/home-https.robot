*** Settings ***
Documentation     Open Page using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${URL}      https://home-page-home-page-1:8080
${BROWSER}        Chrome


*** Test Cases ***
Open Page
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    Open Browser    url=${URL}    browser=${BROWSER}    options=add_argument('--ignore-certificate-errors')
    Title Should Be    Mateusz Kowalkowski
