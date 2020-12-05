from configparser import ConfigParser
from os.path import dirname, abspath, join
def get_config_information(browser):
    config = ConfigParser()    
    my_file = join(dirname(dirname(abspath(__file__))),"config.ini")
    config.read(my_file)
    if browser == "chrome":
        return config.get('selenium','chromedriver')
    elif browser == 'firefox':
        return config.get('selenium','geckodriver')

if(__name__ == '__main__'):
    print(get_config_information("chrome"))