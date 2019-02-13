# -*- coding:utf-8 -*-
__author__ = 'shichao'
import glob
import os
from pypinyin import pinyin, lazy_pinyin, Style


""":
unicode is Chinese characters, numbers, alphabet or other types

"""

def is_Chinese(uchar):
    """unicode char to be Chinese character"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """unicode char to be numbers"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    """unicode char to be English alphabet"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_other(uchar):
    """unicode char to be other types"""
    if not (is_Chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False

def B2Q(uchar):
    """半角转全角"""
    inside_code=ord(uchar)
    if inside_code<0x0020 or inside_code>0x7e:
    #不是半角字符就返回原来的字符
        return uchar
    if inside_code==0x0020:
    #除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code=0x3000
    else:
        inside_code+=0xfee0
        return unichr(inside_code)

def Q2B(uchar):
    """全角转半角"""
    inside_code=ord(uchar)
    if inside_code==0x3000:
        inside_code=0x0020
    else:
        inside_code-=0xfee0
    if inside_code<0x0020 or inside_code>0x7e:
    #转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)

def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])

def uniform(ustring):
    """格式化字符串，完成全角转半角，大写转小写的工作"""
    return stringQ2B(ustring).lower()

def string2List(ustring):
    """将ustring按照中文，字母，数字分开"""
    retList=[]
    utmp=[]
    for uchar in ustring:
        if is_other(uchar):
            if len(utmp)==0:
                continue
            else:
                retList.append("".join(utmp))
                utmp=[]
        else:
            utmp.append(uchar)
        if len(utmp)!=0:
            retList.append("".join(utmp))
        return retList


    #test Q2B and B2Q
    for i in range(0x0020,0x007F):
        print(Q2B(B2Q(unichr(i))),B2Q(unichr(i)))

    #test uniform
    ustring=u'中国 人名ａ高频Ａ'
    ustring=uniform(ustring)
    ret=string2List(ustring)
    print(ret)

def Chinese_filename_to_pinyin(root_in):
    path = '/Users/shichao/OneDrive/Documents/'
    files = '*.pdf'
    filepath = os.path.join(path, files)
    pdfs = glob.glob(filepath)
    for pdf in pdfs:
        new_name = ''
        pdf = os.path.basename(pdf)
        pdf = pdf.decode('utf-8')
        print(pdf)
        name_list = pinyin(pdf, style=Style.TONE2, heteronym=False)
        for name in name_list:
            new_name += name[0]
        if len(new_name) > 20:
            new_name = ''
            name_list = pinyin(pdf, style=Style.INITIALS, strict=False)
            for name in name_list:
                new_name += name[0]
        os.rename(os.path.join(path, pdf), os.path.join(path, new_name))

def main():
    # filepath = '/Users/shichao/OneDrive/Documents/*.pdf'
    path = '/Users/shichao/OneDrive/Documents/'
    files = '*.pdf'
    filepath = os.path.join(path,files)
    pdfs = glob.glob(filepath)
    for pdf in pdfs:
        new_name = list()
        for char in pdf:
            new_name.append(pinyin(char, style=Style.TONE2, heteronym=True)) if is_Chinese(char) else new_name.append(char)
            print(char)
            print(True) if is_Chinese(char) else False




if __name__ == '__main__':
    main()