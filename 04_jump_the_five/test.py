#!/usr/bin/env python3
import os
from subprocess import getstatusoutput

prg = './jump.py'

# --------------------------------------------------
def test_exist():
    """comment"""
    
    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""
    
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test01"""
    
    rv, out = getstatusoutput(f'{prg} 123-456-7890')
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_02():
    """test02"""
    
    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.strip() == 'That number to call is 512-340-6789.'
