import Utilities.FrameworkUtilities

def setup_function(self):
    print("Launching Browser")
    self.driver = Utilities.FrameworkUtilities.launchBrowser("Chrome")


def tearDown(self):
    self.driver.close()

def launchWebsite(self):
    self.driver.get("https://www.makemytrip.com/")