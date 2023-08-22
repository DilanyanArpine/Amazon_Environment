import time
import unittest
import random_name_generator as rng
from selenium import webdriver
from selenium.webdriver.common.by import By
from sources.basePage_ import BasePage
from sources.login__.loginPage_ import LoginPage
from sources.manageProfilesPage_ import ManageProfilesPage
from sources.accountPage_ import AccountPage
from sources.navigationBar__.accountModalLists_ import AccountModalLists
from sources.navigationBar__.navigationBar_ import NavigationBar
from common import data_
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ProfileNameEdit(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(data_.urlSignIn)
        self.loginPageObj = LoginPage(self.driver)
        self.accountPageObj=AccountPage(self.driver)
        self.manageProfilesPageObj=ManageProfilesPage(self.driver)
        self.accountModalListsObj=AccountModalLists(self.driver)
        self.basePageObj = BasePage(self.driver)
        self.navigationBarObj = NavigationBar(self.driver)


    def test_edit_profile_name(self):
        # Log in using valid credentials
        self.loginPageObj.fill_login_filed(data_.loginDataValidArpine["username"])
        self.loginPageObj.press_continue_button()
        self.loginPageObj.fill_password_field(data_.loginDataValidArpine["password"])
        self.loginPageObj.press_signin_button()

        # Navigate to the profile settings page
        self.navigationBarObj.click_to_account_modal_lists()
        self.accountPageObj.click_your_profiles_button()
        self.manageProfilesPageObj.select_profile()
        self.manageProfilesPageObj.click_edit_profile_name_button()

        """Generate a random name and edit the profile name"""
        randName = rng.generate_one()
        time.sleep(3)
        self.manageProfilesPageObj.edit_name_filed(randName)
        time.sleep(3)
        self.manageProfilesPageObj.press_save_changes_button()

        """ Verify that the profile name has been updated"""
        profileNameLocator = (By.ID, "profile-name")
        profileName = self.basePageObj._get_element_text_by_locator(profileNameLocator)
        assert profileName == randName, "Assertion Error: The profile name was not updated"

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()