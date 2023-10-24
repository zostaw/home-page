*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://localhost:8080/
${BROWSER}        Chrome
${Options}        options=add_argument("--ignore-certificate-errors")

*** Test Cases ***
Valid Login
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    Open Browser    ${LOGIN URL}    ${BROWSER}    ${Options}
    Title Should Be    Mateusz Kowalkowski
