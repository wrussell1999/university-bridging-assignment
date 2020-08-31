from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)
        self.browser.get('http://localhost:8000/accounts/login')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('admin')
        password.send_keys('admin')
        save = self.browser.find_element_by_id('save')
        save.click()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Will Russell', self.browser.title)

    def test_cv_page(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Will Russell | CV', self.browser.title)

    def test_cv_sections(self):
        self.browser.get('http://localhost:8000/cv')
        section_titles = self.browser.find_elements_by_class_name('section-title')

        self.assertTrue(any(section_title.text == 'Education' for section_title in section_titles))
        self.assertTrue(any(section_title.text == 'Experience' for section_title in section_titles))
        self.assertTrue(any(section_title.text == 'Skills' for section_title in section_titles))
        self.assertTrue(any(section_title.text == 'Projects' for section_title in section_titles))
        
    def test_cv_education(self):
        self.browser.get('http://localhost:8000/cv/new/education')
        institute = self.browser.find_element_by_id('id_institute')
        education_type = self.browser.find_element_by_id('id_education_type')
        start_date = self.browser.find_element_by_id('id_start_date')
        finish_date = self.browser.find_element_by_id('id_finish_date')
        course = self.browser.find_element_by_id('id_course')

        institute.send_keys('University of Life')
        education_type.send_keys('University')
        start_date.send_keys('03/08/2020')
        finish_date.send_keys('04/08/2020')
        course.send_keys('PhD Life')

        save = self.browser.find_element_by_class_name('save')
        save.click()

    def test_cv_experience(self):
        self.browser.get('http://localhost:8000/cv/new/experience')
        company = self.browser.find_element_by_id('id_company')
        job_title = self.browser.find_element_by_id('id_job_title')
        start_date = self.browser.find_element_by_id('id_start_date')
        finish_date = self.browser.find_element_by_id('id_finish_date')

        company.send_keys('Awesome Corp')
        job_title.send_keys('CEO')
        start_date.send_keys('01/08/2020')
        finish_date.send_keys('02/08/2020')

        save = self.browser.find_element_by_class_name('save')
        save.click()

    def test_cv_skills(self):
        self.browser.get('http://localhost:8000/cv/new/skill')
        content = self.browser.find_element_by_id('id_content')
        years_experience = self.browser.find_element_by_id('id_years_experience')
        
        content.send_keys('Flutter')
        years_experience.send_keys(1)
        
        save = self.browser.find_element_by_class_name('save')
        save.click()

    def test_cv_projects(self):
        self.browser.get('http://localhost:8000/cv/new/project')
        title = self.browser.find_element_by_id('id_title')
        content = self.browser.find_element_by_id('id_content')

        title.send_keys('How I made my first website')
        content.send_keys('It all started long ago...')

        save = self.browser.find_element_by_class_name('save')
        save.click()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
