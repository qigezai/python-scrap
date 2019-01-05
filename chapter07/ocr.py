#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/5 下午11:15

import csv
import string
from PIL import Image
import pytesseract
from form import register

REGISTER_URl = 'http://example.webscraping.com/user/register'

def main():
    print register('Test Account', 'Test Account', 'example@webscarping.com', 'example', ocr)

def ocr(img):
    # threshold the image to ignore background and keep text
    gray  =img.convert('L')
    # gray.save('captcha_greyscale.png')
    bw = gray.point(lambda x:0 if x<1 else 255, '1')
    # bw.save('captcha_threshold.png')
    word = pytesseract.image_to_string(bw)
    ascii_word = ''.join(c for c in word if c in string.letters).lower()
    return ascii_word

def test_sample():
    """
    Test accuracy of OCR on sample images
    :return:
    """
    corrent = total = 0
    for filename, text in csv.reader(open('samples/samples.csv')):
        img = Image.open('samples/'+filename)
        if ocr(img) == text:
            corrent += 1
        total += 1
    print 'Accuracy: %d/%d' % (corrent, total)

if __name__ == '__main__':
    main()