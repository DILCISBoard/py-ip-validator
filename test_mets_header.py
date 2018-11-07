import unittest
from metsvalidator.mets_validator_impl import load_xml, validate

# In this class we test first the correct mets header element and then different error samples. 
# If validation error was detected - validation result should be False.
class MetsHeaderTestCase(unittest.TestCase):
    """ Tests for METS header element """

    @classmethod
    def setUpClass(self):
        self.rules = load_xml("metsvalidator/mets_header_validator.xml")

    def test_load_rules(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_element_ok.xml")
        self.assertTrue(validationResult==True)

    def test_csip7_check_header_element(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_element_not_exists.xml")
        self.assertTrue(validationResult==True)

    def test_csip9_check_package_creation_date(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_package_creation_date_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip10_check_package_last_modification_date(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_package_last_modification_date_not_exists.xml")
        self.assertTrue(validationResult==False)

    def test_csip11_check_oais_package_type(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_oais_package_type_not_exists.xml")
        self.assertTrue(validationResult==False)
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_oais_package_type_value_error.xml")
        self.assertTrue(validationResult==False)

    def test_csip12_check_header_agent_element(self):
        validationResult, report = validate(self.rules, "metsvalidator/mets_header_agent_element_not_exists.xml")
        self.assertTrue(validationResult==True)

if __name__ == '__main__':
    unittest.main()
