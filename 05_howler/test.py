#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './howler.py'


def random_string():
    """generate a random string"""
    
    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def out_flag():
    """Either -o or --outfile"""
    
    return '-o' if random.randint(0, 1) else '--outfile'


def test_exist():
    """exists"""
    
    assert os.path.isfile(prg)


def test_usage():
    """usage"""
    
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == 'FOO BAR BAZ'


def test_text_outfile():
    """Test STDIN/outfile"""

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        out = getoutput(f'{prg} {out_flag()} {out_file} "foo bar baz"')
        assert out.strip() == ''
        assert os.path.isfile(out_file)
        text = open(out_file).read().rstrip()
        assert text == 'FOO BAR BAZ'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


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
            expected = open(os.path.join('test-outs',
                                         expected_file)).read().strip()
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)


def test_lower_text():
    """Test lower case"""

    for flag in ['-e', '--ee']:
        out = getoutput(f'{prg} {flag} "foO BaR BAZ"')
    assert out.strip() == 'foo bar baz'


def test_directory():
    """Test Directory"""
    
    out = getoutput('python howler.py -d ./test-outs -e')
    # out = getoutput(f'{prg} "-d ./test-outs"')
    lists = [file for file in os.listdir('test-outs') if os.path.isfile(file)]

    for target_files in lists:
        try:
            out_file = target_files
            if os.path.isfile(out_file):
                os.remove(out_file)
        
            assert out.strip() == ''
            produced = open(os.path.join('./test-outs/new', (out_file))).read().rstrip()
            expected = open(os.path.join('lower',
                                         target_files)).read().strip()
            assert produced == expected
        finally:
            if os.path.isdir(out_file):
                os.remove(out_file)