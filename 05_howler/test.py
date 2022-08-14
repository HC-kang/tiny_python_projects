#!/usr/bin/env python3
import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput
from typing import final

prg = './howler.py'


# --------------------------------------------------
def random_string():
    """generate a random string"""
    
    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o of --outfile"""
    
    return '-o' if random.randint(0, 1) else '--out_file'


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
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_01():
    """test01"""
    
    rv, out = getstatusoutput(f'{prg} "Ronald Weasley"')
    assert rv == 0
    assert out.rstrip() == 'RONALD WEASLEY'


# --------------------------------------------------
def test_02():
    """test02"""
    
    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)
    
    
    try:
        rv, out = getstatusoutput(f'{prg} "Ronald Weasley" {out_flag()} {out_file}')
        assert rv == 0
        assert out.rstrip() == ''
        assert os.path.isfile(out_file)
        text = open('ron.txt').read().rstrip()
        assert text == 'RONALD WEASLEY'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
        

# --------------------------------------------------
def test_03():
    """test03"""
    
    rv, out = getstatusoutput(f'{prg} ../inputs/fox.txt')
    assert rv == 0
    assert out == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'


# --------------------------------------------------
def test_04():
    """test04"""
    
    rv, out = getstatusoutput(f'{prg} ../inputs/fox.txt {out_flag()} out.txt')
    assert rv == 0
    assert open('out.txt').read().rstrip() == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'


# --------------------------------------------------
def test_file():
    """Test file in/out"""
    
    for expected_file in os.listdir('test-outs'):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)
            
            basename = os.path.basename(expected_file)
            in_file = os.path.join('../inputs', basename)
            out = getoutput(f'{prg} {out_flag()} {out_file} {in_file}')
            assert out.strip() == ''
            produced = open(out_file).read().rstrip()
            expected = open(os.path.join('test-outs', expected_file)).read().strip()
            assert produced == expected
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)


# --------------------------------------------------
def test_06():
    """test06"""

    try:
        out_file = random_string()
        if os.path.isdir('out-files'):
            os.rmdir('out-files')
        
        out = getoutput(f'{prg} {out_flag()} {out_file} "test-outs"')
        assert out.strip() == ''
        assert len(os.listdir('test-outs')) == len(os.listdir('out-files'))
        for test_out in os.listdir('test-outs'):
            expected = open(os.path.join('test-outs', test_out)).read().strip()
            produced = open(os.path.join('out-files', test_out)).read().strip()
            assert produced == expected
    finally:
        if os.path.isdir('out-files'):
            for file in os.listdir('out-files'):
                os.remove(os.path.join('out-files', file))
            os.rmdir('out-files')
