*** Settings ***
Documentation     Open Page using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${URL}      https://home-page-home-page-1:8080
${BROWSER}        Chrome
${Options}        options=add_argument(['--ignore-certificate-errors', '--allow-insecure-localhost'])

*** Test Cases ***
Open Page
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    Open Browser    ${URL}    ${BROWSER}    ${Options}
    Title Should Be    Mateusz Kowalkowski
