import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getinvalidUseremail():
        invalid_email = config.get('common info', 'invalid_email')
        return invalid_email

    @staticmethod
    def getinvalidPassword():
        invalid_password = config.get('common info', 'invalid_password')
        return invalid_password

