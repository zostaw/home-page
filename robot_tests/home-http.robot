*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://127.0.0.1:8080

*** Test Cases ***
Valid Login
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    Open Browser    ${LOGIN URL}    
    Title Should Be    Mateusz Kowalkowski
