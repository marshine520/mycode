#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest


class Testlogin:
    def test_login1(self):
        print("已登录1")
        assert 1

    def test_login2(self):
        print("已登录2")
        assert 1

    def test_login3(self):
        print("已登录3")
        assert 1

    def test_login4(self):
        print("已登录4")
        assert 0
        # if __name__ == '__main__':
        #     pytest.main(["-s", "login1.py"])
