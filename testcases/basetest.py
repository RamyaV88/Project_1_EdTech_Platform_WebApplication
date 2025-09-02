import pytest

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    url = ReadConfig.get_application_url()
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    invalid_email = ReadConfig.get_invalid_user_email()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogGen.loggen()
