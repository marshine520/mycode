#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import random
#i = 0
class Testlogin:
    @pytest.mark.run(order=1)
    def test_login1(self):
        print("1")
        assert 1

    @pytest.mark.run(order=3)
    def test_login2(self):
        print("2")
        assert 1

    @pytest.mark.run(order=4)
    def test_login3(self):
        print("3")
        assert 1

    @pytest.mark.run(order=2)
    def test_login4(self):
        print("4")
        num = random.randint(1,3)
        if num == 1:
            assert 1
        else:
            assert 0
