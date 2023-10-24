*** Settings ***
Documentation     Open Page using SeleniumLibrary.
Library           Browser

*** Variables ***
${URL}      https://home-page-home-page-1:8080
${BROWSER}        chromium
${Options}        options=add_argument("--ignore-certificate-errors")
${HEADLESS}       ${True}


*** Test Cases ***
Suite setup
    New Browser    ${BROWSER}  
    New Context    ignoreHTTPSErrors=${True}
    New Page    ${URL}
    Title Should Be    Mateusz Kowalkowski
    [Teardown]    Close Browser

