import configparser
import logging.config
from dataclasses import dataclass

from utilities.EnumBase import EnumBase

logger = logging.Logger("configuration_manager")


class EnvironmentType(EnumBase):
    REAL = 1
    ALPHA = 2
    BETA = 3

class ConfigurationManager:
    """
        Responsible to load configuration settings
    """
    config_data = None

    @classmethod
    def init(cls, config_name):
        """
            To load configuration data
            """
        config = configparser.ConfigParser()
        path_to_config = "config/config.ini"
        if not config.read(path_to_config):
            raise ValueError(f"Failed to read config from [{path_to_config}]")
        cls.config_data = config[config_name]

    @classmethod
    def get_active_browser(cls):
        """
            To get configured browser name, returns default value of "Chrome" if
                  related config key is missing in the configuration file.
        """
        active_browser = cls.get_config_value("active_browser", "Headless")
        return active_browser

    @classmethod
    def get_environment(cls):
        """
            To get configured environment, returns default value of "QA" environment if
                     related config key is missing in the configuration file.
        """
        environment = cls.get_config_value("environment", "SIMULATION")
        return environment

    @classmethod
    def get_base_url(cls):
        """
            To get configured base url, returns default value of "http://localhost:4200" if
                      related config key is missing in the configuration file.
        """
        base_url = cls.get_config_value("base_url", "http://localhost:4200")
        return base_url

    @classmethod
    def get_page_url(cls, page_name):
        """
            To get configured page url, returns default value of "page" if
                      related config key is missing in the configuration file.
        """
        page_url = cls.get_config_value(page_name)
        return page_url


    @classmethod
    def get_log_folder(cls):
        """
            To get configured path for pytest log results.
        """
        log_folder = cls.get_config_value("pytest_result_dir")
        return log_folder


    @classmethod
    def get_config_value(cls, config_name, default_value=None):
        """
            To return the configured value for a given key.  Accepts optional
              default value which would be returned if given configured key
              is not in the configuration file
        """
        if not cls.config_data:
            raise ValueError("Config manager data was not initialized, run 'init' class method before using")
        if config_name in cls.config_data:
            return cls.config_data[config_name]
        else:
            logger.debug("returning default value for ", config_name)
            return default_value
        
    @classmethod
    def get_default_timeout_in_seconds(cls):
        """
            To get configured environment, returns the default timeout for api calls
        """
        environment = cls.get_config_value("default_timeout_in_seconds", 60)
        return environment


