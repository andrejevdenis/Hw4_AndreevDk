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
    browser.element('[id="subjectsContainer"]').click()
    keyboard.write('Eng')
    keyboard.press('Enter')

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('[for="uploadPicture"]').click()
    keyboard.write('D:\Octopus.jpg')
    keyboard.press('ENTER')

    browser.element('[placeholder="Current Address"]').type(fake.address())

    browser.element('[id="state"]').click()
    keyboard.write('ncr')
    keyboard.press('ENTER')

    browser.element('[id="city"]').click()
    keyboard.write('Delhi')
    keyboard.press('ENTER')

    browser.element('[id="submit"]').click()