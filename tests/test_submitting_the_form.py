from selene import browser, be, have
from time import sleep

# def test_Search_does_not_return_results():
#     browser.open("https://google.com")
#     browser.element('[name="q"]').should(be.blank).type('hjhjkhbjkhh').press_enter()
#     browser.element('.card-section').should(have.text('ничего не найдено'))
#     sleep(5)


# def test_search_does_not_return_results(windows_size):
#     browser.open("https://ya.ru")
#     browser.element('[name="text"]').should(be.blank).type('hjhjkhbjkhh').press_enter()
#     browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
#     sleep(3)

def test_submitting_the_form():
