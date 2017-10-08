#! /usr/bin/env python
# -*- coding: ascii -*-

# FILE HEADER
##
# @file decoder.py
# @author Hossein Sarpanah
# @version 1.0.0
# @brief A bunch of functions for decoding a file
# @details Manage operations for reading a file, taking the values, decode those values, write them on a new txt file.
# @note None
# @bug None
# @warning None
# @date 02-10-2017

import os
import copy
import struct
path_to_file = 'C:\Users/hossein/Desktop/ByteDecoder_exe/DECODER/RFI.txt'
FF = 0xFF


def ExtractData(path_to_file):
    """
    #brief This function opens txt file with a standard format and returns its contents as sting
    @param path_to_file:
    @return text: returns string
    """
    try:
        in_file = open(path_to_file, "r")
        text = in_file.read()
        in_file.close()
        if text == '':
            return False
    except Exception:
        raise
    return text


def FrameFromText(string):
    """"
    @brief This function reads all string lines and returns a list of list of received frames.
    """
    temp= []
    allValues = []

    temp.extend(x.split(' ') for x in string.split('\n'))
    for y in temp:
        y.pop()

    TxFrame = ['FF', '04', '00', '00', '00', '04', 'FF', 'FF']
    for element in temp:
        if element == TxFrame:
            pass
        else:
            allValues.append(element)
    ReceivedFrame = []
    for ciao in allValues:
        try:
            Tempb = copy.deepcopy([int(x, 16) for x in ciao])
            if len(Tempb) != 13:
                raise TypeError
        except:
            return [[]] # will be interpretated as false
        ReceivedFrame.append(Tempb)
    return ReceivedFrame

def decode(bytes4):
    """
    input: 4 bytes
    output: little endian float
    @return 4 bytes and unpack the string
    """
    return bytes4, struct.unpack('<f', ''.join(chr(x) for x in bytes4))[0]
    # print""

def DecodeFrame(Frame):
    """
    @brief Decode a line of received frame
    @param Frame:
    @return A list of active and reference frames
    """
    return [decode(Frame[3:7]), decode(Frame[7:11])]


def DecodeList(ListOfFrame):
    """
    @brief Decode the whole received frame line by line
    @param Frame:
    @return A list of active and reference tuples
    """

    result = []
    for Frame in ListOfFrame:
        result.append(DecodeFrame(Frame))
    return result

def BytesToString(bts):
    """
    @brief Convert byte to string
    @param bts:
    @return byte string
    """
    return ' '.join(['0x' + format(b, '02X') for b in bts])


def FloatToString(flt, decimal):
    """
    @brief Convert float to string
    @param flt:
    @param decimal:
    @return Float as a string
    """
    return str(round(flt, decimal))


def PairStrings(string1, string2):
    """
      @brief pairing two strings
      @param flt:
      @param decimal:
      @return string
      """
    return string1 + '\t' + string2


def TupleSolver(my_tuple, decimal = 2):
    string1 = BytesToString(my_tuple[0])
    string2 = FloatToString(my_tuple[1], decimal)
    return PairStrings(string1, string2)


def FrameSolver(my_frame):
    return TupleSolver(my_frame[0]) + '\t' + TupleSolver(my_frame[1], 3)

def FrameLabel():
    """
      @brief Add label at the header
      @param flt:
      @param decimal:
      @return
      """
    return (''+'\t'+'Active'+'\t'+''+'\t'+'Reference')

def PrepareData(DecodedFrameList):
    """
      @brief This function create a list of string consist of a active values, reference values and their float values
      @param flt:
      @param decimal:
      @return a list of string
      """
    LstOfString = []
    LstOfString.append(FrameLabel())
    for Frame in DecodedFrameList:
        LstOfString.append(FrameSolver(Frame))
    return LstOfString

def WriteValue(path, text):
    """
    @brief This function creates a Data Analysis as subdirection of operatore folder
    @param path:
    @param text:
    @return:
    """
    #

    if not os.path.isfile(path):
        f = open(path, "w")
        for Line in text:
            f.write(Line + '\n')
        f.close()
    else:
        return False

    return True

def NewTxt(TxtFile):
    """"
    @brief This function creates a new path by using the original path which we're gonna decode its contents.
    @param TxtFile: Is referring to the file which should be decoded.
    @return NewPath: a new path
    """
    formatE = str(TxtFile)[-4:]
    Name = str(TxtFile)[:-4]
    New_File = Name + "_decoded" + formatE
    NewPath = os.getcwd() + '\\' + New_File
    return NewPath


directory = os.getcwd()
paths = os.listdir(directory)
File = '.txt'
for TxtFile in paths:
    if TxtFile.endswith(File):
        if not TxtFile.endswith('_decoded.txt'):
            Text = ExtractData(TxtFile)
            listofframe = FrameFromText(Text)
            if listofframe == [[]]:
                print 'File %s has an unexpected format and will be ignored.' % TxtFile
                continue
            result = DecodeList(listofframe)
            PrepareString = PrepareData(result)
            NewPath = NewTxt(str(TxtFile))
            WriteValue(NewPath, PrepareString)
        else:
            print 'File %s has not been decoded correctly!' % (TxtFile )
raw_input('Press any button to close')