import keyboard
from selene import browser, have, be
from faker import Faker
fake = Faker()
import random

def test_complete_todo():
    browser.element('[placeholder="First Name"]').type(fake.first_name_male())
    browser.element('[placeholder="Last Name"]').type(fake.last_name_male())
    browser.element('[id="userEmail"]').type(fake.email())
    browser.element('[for="gender-radio-1"]').click() #Male
    browser.element('[placeholder="Mobile Number"]').type(random.randint(1000000000, 9000000000)).press_tab()
    browser.element('[id="dateOfBirthInput"]').type(fake.date_of_birth(None, 1, 90)).press_enter()


    browser.element('[id="subjectsInput"]').type('M')
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsInput"]').type('Co')
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsContainer"]').should(have.text('Maths'))
    browser.element('[id="subjectsContainer"]').should(have.text('Computer Science'))

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('[for="uploadPicture"]').click()
    keyboard.write('https://github.com/andrejevdenis/Hw4_AndreevDk/blob/master/tests/Octopus.jpg')
    keyboard.send('ENTER')

    browser.element('[placeholder="Current Address"]').type(fake.address())

    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('[id="state"]').should(have.text('NCR'))

    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    browser.element('[id="city"]').should(have.text('Delhi'))

    browser.element('[id="submit"]').click()
    browser.element('[class="modal-header"]').should(have.text('Thanks for submitting the form'))