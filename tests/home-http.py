*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://zostaw.cloud
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Mateusz Kowalkowski
