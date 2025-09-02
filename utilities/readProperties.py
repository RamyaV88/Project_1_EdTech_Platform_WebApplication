import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_invalid_user_email():
        invalid_email = config.get('common info', 'invalid_email')
        return invalid_email

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('common info', 'invalid_password')
        return invalid_password
