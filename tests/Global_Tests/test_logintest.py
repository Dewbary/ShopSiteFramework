from utilities.BaseClass import BaseClass
from selenium import webdriver
import time


class TestOne(BaseClass):

    def test_logintest(self):
        log = self.getLogger()
        log.info("TEST HAS BEEN COMPLETED")