import time
from typing import Callable

from utilities.configuration_manager import ConfigurationManager
import os
import math
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class AssertTimeout:

    @staticmethod
    def are_equal(actual, expected, timeout_in_seconds=ConfigurationManager.get_default_api_timeout_in_seconds()):

        logger.info(f"Waiting for {actual()} to be equal to {expected} within {timeout_in_seconds} seconds")
        result = AssertTimeout.wait_for_condition(lambda: actual() == expected, timeout_in_seconds)

        if not result:
            assert False, f"Condition was not true. Expected: {expected}. Actual: {actual()}"

    @staticmethod
    def is_true(actual, failure_message, timeout_in_seconds=ConfigurationManager.get_default_api_timeout_in_seconds()):

        logger.info(f"Waiting for {actual()} to be true within {timeout_in_seconds} seconds")
        result = AssertTimeout.wait_for_condition(lambda: actual() is True, timeout_in_seconds)

        if not result:
            assert False, f"{failure_message}"

    @staticmethod
    def value_is_within_tolerance(actual: Callable, expected: float, tolerance: float,
                                  timeout_in_seconds=ConfigurationManager.get_default_api_timeout_in_seconds()):

        logger.info(
            f"Waiting for value {actual()} to be equal to {expected} within tolerance in the next {timeout_in_seconds} seconds")
        result = AssertTimeout.wait_for_condition(lambda: math.isclose(actual(), expected, abs_tol=tolerance),
                                                  timeout_in_seconds)

        if not result:
            assert False, f"Value was not within {tolerance} tolerance of {expected}. Actual value is {actual()}"

    @staticmethod
    def is_false(actual: Callable, failure_message: str,
                 timeout_in_seconds=ConfigurationManager.get_default_timeout_in_seconds()):

        logger.info(f"Waiting for {actual()} to be false within {timeout_in_seconds} seconds")
        result = AssertTimeout.wait_for_condition(lambda: actual() == False, timeout_in_seconds)

        if not result:
            assert False, f"{failure_message}"

    @staticmethod
    def wait_for_condition(expected_condition: Callable,
                           timeout_in_seconds=ConfigurationManager.get_default_timeout_in_seconds(),
                           polling_period_in_seconds=0.5):

        timeout = time.time() + float(timeout_in_seconds)

        while time.time() < timeout:

            if expected_condition():
                return True

            time.sleep(polling_period_in_seconds)
        return False

    @staticmethod
    def are_not_equal(actual, expected, timeout_in_seconds=ConfigurationManager.get_default_timeout_in_seconds()):

        logger.info(f"Waiting for {actual()} not to be equal to {expected} within {timeout_in_seconds} seconds")
        result = AssertTimeout.wait_for_condition(lambda: actual() != expected, timeout_in_seconds)

        if not result:
            assert False, f"Condition was not False. Expected: {expected}. Actual: {actual()}"
            