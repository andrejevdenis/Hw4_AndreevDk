import os.path

from selene import browser, have, be

def test_complete_todo():
    browser.element('[id="firstName"]').type('Fedor')
    browser.element('[id="lastName"]').type('Lomovoy')
    browser.element('[id="userEmail"]').type('fedyaosminog@ramb.com')
    browser.element('[for="gender-radio-1"]').click() #Male
    browser.element('[id="userNumber"]').type('1000000000').press_tab()
    browser.element('[class="react-datepicker__month-select"]').element('[value="9"]').click()
    browser.element('[class="react-datepicker__year-select"]').element('[value="2000"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--023"]').click()

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
    browser.element('[class="table-responsive"]').should(have.text('Fedor Lomovoy'))
    browser.element('[class="table-responsive"]').should(have.text('fedyaosminog@ramb.com'))
    browser.element('[class="table-responsive"]').should(have.text('Male'))
    browser.element('[class="table-responsive"]').should(have.text('1000000000'))
    browser.element('[class="table-responsive"]').should(have.text('23 October,2000'))
    browser.element('[class="table-responsive"]').should(have.text('Maths, Computer Science'))
    browser.element('[class="table-responsive"]').should(have.text('Sports, Reading, Music'))
    browser.element('[class="table-responsive"]').should(have.text('Octopus.jpg'))
    browser.element('[class="table-responsive"]').should(have.text('Moscow, Bulkina 65-39'))
    browser.element('[class="table-responsive"]').should(have.text('NCR Delhi'))