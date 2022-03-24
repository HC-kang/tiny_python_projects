#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


def test_exist():
    """exist"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""
    
    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


def test_one():
    """one item"""
    
    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'


def test_two():
    """two item"""
    
    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


def test_more_than_two():
    """more than two items"""
    
    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


def test_more_than_two_sorted():
    """more than two items"""
    
    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected


def test_no_comma_before_and():
    """no comma before and"""
    
    arg = '"potato chips" cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg} --option')
    expected = ('You are bringing potato chips, '
                'cupcakes and French silk pie.')
    assert out.strip() == expected


def test_delimeter():
    """delimeter test"""
    
    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg} --delimiter -')
    expected = ('You are bringing potato chips- coleslaw- '
                'cupcakes- and French silk pie.')
    assert out.strip() == expected