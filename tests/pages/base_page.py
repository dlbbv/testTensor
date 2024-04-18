class BasePage():
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def findAll(self, args):
        return self.browser.find_elements(*args)

    def execute(self, args):
        return self.browser.execute_script(*args)

    def currentUrl(self):
        return self.browser.current_url

    def title(self):
        return self.browser.title
