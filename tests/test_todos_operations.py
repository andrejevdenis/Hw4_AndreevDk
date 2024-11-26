import os.path

from selene import browser, have, be

def test_complete_todo():
    browser.element('[id="firstName"]').type('Fedor')
    browser.element('[id="lastName"]').type('Lomovoy')
    browser.element('[id="userEmail"]').type('fedyaosminog@ramb.com')
    browser.element('[for="gender-radio-1"]').click() #Male
    browser.element('[id="userNumber"]').type('1000000000').press_tab()
    browser.element('[id="dateOfBirthInput"]').type(23-10-2000).press_enter()

    browser.element('[id="subjectsInput"]').type('M')
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsInput"]').type('Co')
    browser.element('[id="react-select-2-option-0"]').click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('[id="uploadPicture"]').set_value(os.path.abspath("../tests/Octopus.jpg"))

    browser.element('[id="currentAddress"]').type('Moscow, Bulkina 65-39')

    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-0"]').click()

    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()

    browser.element('[id="submit"]').click()
    browser.element('[class="modal-header"]').should(have.text('Thanks for submitting the form'))