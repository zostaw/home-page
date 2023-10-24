*** Settings ***
Documentation     Open Page using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${URL}      https://home-page-home-page-1:8080
${BROWSER}        Chrome
${Options}        options=add_argument("--ignore-certificate-errors")


*** Test Cases ***
Suite setup
    New Browser    ${BROWSER}  ${HEADLESS}  
    args=['--allow-insecure-localhost']
    New Context    ignoreHTTPSErrors=${True}   bypassCSP=${True}

Open Page
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***

Welcome Page Should Be Open
    New Page    ${URL}
    Title Should Be    Mateusz Kowalkowski
