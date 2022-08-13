#!/usr/bin/env python3
import os
from subprocess import getstatusoutput

prg = './howler.py'

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
    
    rv, out = getstatusoutput(f'{prg} "Ronald Weasley"')
    assert rv == 0
    assert out == 'RONALD WEASLEY'


# --------------------------------------------------
def test_02():
    """test02"""
    
    for flag in ['-o', '--out']:
        rv, out = getstatusoutput(f'{prg} "Ronald Weasley" {flag} ron.txt')
        assert rv == 0
        assert open('ron.txt').read().strip() == 'RONALD WEASLEY'

# --------------------------------------------------
def test_03():
    """test03"""
    
    rv, out = getstatusoutput(f'{prg} ../inputs/fox.txt')
    assert rv == 0
    assert out == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'


# --------------------------------------------------
def test_04():
    """test04"""
    
    for flag in ['-o', '--out']:
        rv, out = getstatusoutput(f'{prg} ../inputs/fox.txt {flag} out.txt')
        assert rv == 0
        assert open('out.txt').read().strip() == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
