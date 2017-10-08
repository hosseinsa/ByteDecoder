#! user/bin/env python
# --coding: ascii--

"""
@file DecodingData.py
@authors Hossein Sarpanah, Stefano G.
@version 1.0.0
@brief This module creates a bunch of functions to test all written functions
@details
@note None
@bug None
@warning None
@date ---
"""

import unittest
import os


from DECODER.decoder import ExtractData, FrameFromText, DecodeFrame, DecodeList, PrepareData, WriteValue

RFI_valid_path = 'Z:\Software_tests\ByteDecoder\RFI_Valid'
RFI_error_path = 'Z:\Software_tests\ByteDecoder\RFI_With_Error'
RFI_wrong_path = 'Z:\Software_tests\ByteDecoder\RFI_Wrong'

RFIpath = RFI_valid_path + '\RFI.txt'
RFIempty = 'Z:\Software_tests\ByteDecoder\Empty_txt.txt'
NEWpath = os.getcwd() + '\RFI_result.txt'

RFI_valid = [RFI_valid_path + '\\' + RFITestName for RFITestName in os.listdir(RFI_valid_path)]
RFI_error = [RFI_error_path + '\\' + RFITestName for RFITestName in os.listdir(RFI_error_path)]
RFI_wrong = [RFI_wrong_path + '\\' + RFITestName for RFITestName in os.listdir(RFI_wrong_path)]

ByteFrame = [[0xFF, 0x04, 0x08, 0xA0, 0x0E, 0x7C, 0x44, 0x98, 0x6C, 0xAF, 0x43, 0xDE, 0xD1],
             [0xFF, 0x04, 0x08, 0xB8, 0x10, 0x7C, 0x44, 0x5C, 0x68, 0xAF, 0x43, 0x5C, 0x8B],
             [0xFF, 0x04, 0x08, 0x5A, 0x0F, 0x7C, 0x44, 0xD6, 0x52, 0xAF, 0x43, 0x37, 0xCE],
             [0xFF, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF],
             ]

ListOfListOfTuple = [[([0xA0, 0x0E, 0x7C, 0x44], 1008.23), ([0x98, 0x6C, 0xAF, 0x43], 350.848)],
                     [([0xB8, 0x10, 0x7C, 0x44], 1008.26), ([0x5C, 0x68, 0xAF, 0x43], 350.815)],
                     [([0x5A, 0x0F, 0x7C, 0x44], 1008.24), ([0xD6, 0x52, 0xAF, 0x43], 350.647)],
                     [([0x00, 0x00, 0x00, 0x00], 0), ([0x00, 0x00, 0x00, 0x00], 0)],
                     ]

# Table used in MbCrc16 function to calculate CRC according to Modbus protocol specifications
_TabellaCrcH = (
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x00,	0xC1,	0x81,	0x40,	0x01,	0xC0,	0x80,	0x41,
    0x01,	0xC0,	0x80,	0x41,	0x00,	0xC1,	0x81,	0x40,
)
# Table used in MbCrc16 function to calculate CRC according to Modbus protocol specifications
_TabellaCrcL = (
    0x00,	0xC0,	0xC1,	0x01,	0xC3,	0x03,	0x02,	0xC2,
    0xC6,	0x06,	0x07,	0xC7,	0x05,	0xC5,	0xC4,	0x04,
    0xCC,	0x0C,	0x0D,	0xCD,	0x0F,	0xCF,	0xCE,	0x0E,
    0x0A,	0xCA,	0xCB,	0x0B,	0xC9,	0x09,	0x08,	0xC8,
    0xD8,	0x18,	0x19,	0xD9,	0x1B,	0xDB,	0xDA,	0x1A,
    0x1E,	0xDE,	0xDF,	0x1F,	0xDD,	0x1D,	0x1C,	0xDC,
    0x14,	0xD4,	0xD5,	0x15,	0xD7,	0x17,	0x16,	0xD6,
    0xD2,	0x12,	0x13,	0xD3,	0x11,	0xD1,	0xD0,	0x10,
    0xF0,	0x30,	0x31,	0xF1,	0x33,	0xF3,	0xF2,	0x32,
    0x36,	0xF6,	0xF7,	0x37,	0xF5,	0x35,	0x34,	0xF4,
    0x3C,	0xFC,	0xFD,	0x3D,	0xFF,	0x3F,	0x3E,	0xFE,
    0xFA,	0x3A,	0x3B,	0xFB,	0x39,	0xF9,	0xF8,	0x38,
    0x28,	0xE8,	0xE9,	0x29,	0xEB,	0x2B,	0x2A,	0xEA,
    0xEE,	0x2E,	0x2F,	0xEF,	0x2D,	0xED,	0xEC,	0x2C,
    0xE4,	0x24,	0x25,	0xE5,	0x27,	0xE7,	0xE6,	0x26,
    0x22,	0xE2,	0xE3,	0x23,	0xE1,	0x21,	0x20,	0xE0,
    0xA0,	0x60,	0x61,	0xA1,	0x63,	0xA3,	0xA2,	0x62,
    0x66,	0xA6,	0xA7,	0x67,	0xA5,	0x65,	0x64,	0xA4,
    0x6C,	0xAC,	0xAD,	0x6D,	0xAF,	0x6F,	0x6E,	0xAE,
    0xAA,	0x6A,	0x6B,	0xAB,	0x69,	0xA9,	0xA8,	0x68,
    0x78,	0xB8,	0xB9,	0x79,	0xBB,	0x7B,	0x7A,	0xBA,
    0xBE,	0x7E,	0x7F,	0xBF,	0x7D,	0xBD,	0xBC,	0x7C,
    0xB4,	0x74,	0x75,	0xB5,	0x77,	0xB7,	0xB6,	0x76,
    0x72,	0xB2,	0xB3,	0x73,	0xB1,	0x71,	0x70,	0xB0,
    0x50,	0x90,	0x91,	0x51,	0x93,	0x53,	0x52,	0x92,
    0x96,	0x56,	0x57,	0x97,	0x55,	0x95,	0x94,	0x54,
    0x9C,	0x5C,	0x5D,	0x9D,	0x5F,	0x9F,	0x9E,	0x5E,
    0x5A,	0x9A,	0x9B,	0x5B,	0x99,	0x59,	0x58,	0x98,
    0x88,	0x48,	0x49,	0x89,	0x4B,	0x8B,	0x8A,	0x4A,
    0x4E,	0x8E,	0x8F,	0x4F,	0x8D,	0x4D,	0x4C,	0x8C,
    0x44,	0x84,	0x85,	0x45,	0x87,	0x47,	0x46,	0x86,
    0x82,	0x42,	0x43,	0x83,	0x41,	0x81,	0x80,	0x40,
)


def mb_crc16(frame):
    """
    Calculate CRC according to Modbus protocol specifications for frame of data specified.

    @param frame: Data frame for which CRC must be calculated
    @return:
    """
    crc_h = 0xFF
    crc_l = 0xFF

    for c in frame:
        i = crc_l ^ c
        crc_l = crc_h ^ _TabellaCrcH[i]
        crc_h = _TabellaCrcL[i]

    return crc_h, crc_l


class ExtractDataCase(unittest.TestCase):
    """
    @brief ExtractData reads text from a .txt in the given path and return the text as a string
    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_ExtractData_IsString(self):
        """
        @brief Valid input should return a string
        """

        RFI_to_test = RFI_valid + RFI_error + RFI_wrong
        for path in RFI_to_test:
            self.assertEqual(type(ExtractData(path)), str)

    def test_ExtractData_CorrectText(self):
        """
        @brief Valid input extraction
        """

        RFI_to_test = RFI_valid + RFI_error + RFI_wrong
        for path in RFI_to_test:
            in_file = open(path, "r")
            text = in_file.read()
            in_file.close()
            self.assertEqual(ExtractData(path), text)

    def test_ExtractData_NonExistingPath(self):
        """
        @brief NonExistingPath will raise WindowsError
        """
        with self.assertRaises(IOError):
            ExtractData('C:/NonExistingPath')

    def test_ExtractData_WrongPath(self):
        """
        @brief Wrong path should raise TypeError
        """
        with self.assertRaises(TypeError):
            ExtractData(15)

    def test_ExtractData_EmptyDoc(self):
        """
        @brief Empty doc should return false
        """
        self.assertEqual(ExtractData(RFIempty), False)


class FrameFromTextCase(unittest.TestCase):
    """
    @brief FrameFromText extract valid frames from text

    @details a frame is defined valid if
    Is on a newline
    Is bracketed in square parenthesis
    Nothing follows or precede the square parenthesis
    Contains only 13 bytes in the form '00', separated by a space
    Immediately follows the request frame: [FF 04 00 00 00 04 FF FF] # will not be tested

    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_FrameFromText_types(self):
        """
        @brief valid text should output formatted frame
        """

        RFI_to_test = RFI_valid + RFI_error
        for path in RFI_to_test:
            temp_file = open(path, "r")
            rfi_text = temp_file.read()
            temp_file.close()
            self.assertEqual(type(FrameFromText(rfi_text)), list)
            for frame in FrameFromText(rfi_text):
                self.assertEqual(type(frame), list)
                for N in frame:
                    self.assertEqual(type(N), int)

    def test_FrameFromText_removal(self):
        """
        @brief valid text should remove question frames from output (redundant!)
        """

        RFI_to_test = RFI_valid + RFI_error
        for path in RFI_to_test:
            temp_file = open(path, "r")
            rfi_text = temp_file.read()
            temp_file.close()
            for frame in FrameFromText(rfi_text):
                self.assertNotEqual(frame, [0xFF, 0x04, 0x00, 0x00, 0x00, 0x04, 0xFF, 0xFF])

    def test_FrameFromText_length(self):
        """
        @brief valid text should output frames with correct length
        """

        RFI_to_test = RFI_valid + RFI_error
        for path in RFI_to_test:
            temp_file = open(path, "r")
            rfi_text = temp_file.read()
            temp_file.close()
            for frame in FrameFromText(rfi_text):
                self.assertEqual(len(frame), 13)

    def test_FrameFromText_bytes(self):
        """
        @brief valid text should output frame with correct starting and ending bytes
        """

        RFI_to_test = RFI_valid + RFI_error
        for path in RFI_to_test:
            temp_file = open(path, "r")
            rfi_text = temp_file.read()
            temp_file.close()
            for frame in FrameFromText(rfi_text):
                crc_h, crc_l = mb_crc16(frame[:11])
                self.assertEqual(frame[0], 0xFF)
                self.assertEqual(frame[1], 0x04)
                self.assertEqual(frame[2], 0x08)
                self.assertEqual(frame[11], crc_l)
                self.assertEqual(frame[12], crc_h)


class DecodeFrameCase(unittest.TestCase):
    """
    @brief DecodeFrame takes a frame and returns bytes and bytes' value
    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_DecodeFrame_type(self):
        for Frame in ByteFrame:
            self.assertEqual(type(DecodeFrame(Frame)), list)
            for element in DecodeFrame(Frame):
                self.assertEqual(type(element), tuple)
                self.assertEqual(type(element[0]), list)
                self.assertEqual(type(element[1]), float)
                self.assertEqual(len(element), 2)

    def test_DecodeFrame_result0(self):
        """
        @brief checking known results
        """
        act, res = DecodeFrame(ByteFrame[0])
        self.assertEqual(act[0], [0xA0, 0x0E, 0x7C, 0x44])
        self.assertAlmostEqual(act[1], 1008.23, delta=0.01)
        self.assertEqual(res[0], [0x98, 0x6C, 0xAF, 0x43])
        self.assertAlmostEqual(res[1], 350.848, delta=0.001)

    def test_DecodeFrame_result1(self):
        """
        @brief checking known results
        """
        act, res = DecodeFrame(ByteFrame[1])
        self.assertEqual(act[0], [0xB8, 0x10, 0x7C, 0x44])
        self.assertAlmostEqual(act[1], 1008.26, delta=0.01)
        self.assertEqual(res[0], [0x5C, 0x68, 0xAF, 0x43])
        self.assertAlmostEqual(res[1], 350.815, delta=0.001)

    def test_DecodeFrame_result2(self):
        """
        @brief checking known results
        """
        act, res = DecodeFrame(ByteFrame[2])
        self.assertEqual(act[0], [0x5A, 0x0F, 0x7C, 0x44])
        self.assertAlmostEqual(act[1], 1008.24, delta=0.01)
        self.assertEqual(res[0], [0xD6, 0x52, 0xAF, 0x43])
        self.assertAlmostEqual(res[1], 350.647, delta=0.001)

    def test_DecodeFrame_result3(self):
        """
        @brief checking known results
        """
        act, res = DecodeFrame(ByteFrame[3])
        self.assertEqual(act[0], [0x00, 0x00, 0x00, 0x00])
        self.assertEqual(act[1], 0)
        self.assertEqual(res[0], [0x00, 0x00, 0x00, 0x00])
        self.assertEqual(res[1], 0)


class DecodeListCase(unittest.TestCase):
    """
    @brief DecodeList produce a list of DecodeFrame's results
    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_DecodeList_type(self):
        """
        @brief check type
        """
        self.assertEqual(type(DecodeList(ByteFrame)), list)


class PrepareDataCase(unittest.TestCase):
    """
    @brief from an expected input, produce a formatted string to be printed
    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_PrepareData_type(self):
        """
        @brief valid input produce formatted output (list of string)
        """
        self.assertEqual(type(PrepareData(ListOfListOfTuple)), list)
        for line in PrepareData(ListOfListOfTuple):
            self.assertEqual(type(line), str)

    def test_PrepareData_separators(self):
        """
        @brief 4 elements are expected, separated by '\t'
        """
        for line in PrepareData(ListOfListOfTuple):
            self.assertEqual(line.count('\t'), 3)

    def test_PrepareData_testcase(self):
        """
        @brief known result
        """
        self.assertEqual(PrepareData([ListOfListOfTuple[0]]),
                         ["0xA0 0x0E 0x7C 0x44\t1008.23\t0x98 0x6C 0xAF 0x43\t350.848"])


class WriteValueCase(unittest.TestCase):
    """
    @brief write a string into a file in a provided path
    """

    def setUp(self):
        self.file = open("Test", "r")

    def tearDown(self):
        self.file.close()

    def test_WriteValue_FilePresent(self):
        """
        @brief Check if file is created and contains the correct text
        """
        text = 'Example Text!'
        path = os.getcwd() + '/test.txt'
        if os.path.isfile(path):
            os.remove(path)
        self.assertEqual(WriteValue(path, [text]), True)
        self.assertEqual(os.path.isfile(path), True)
        in_file = open(path, "r")
        in_file_text = in_file.read()
        in_file_text = in_file_text.strip()
        in_file.close()
        self.assertEqual(text, in_file_text)
        if os.path.isfile(path):
            os.remove(path)

    def test_WriteValue_FileAlready(self):
        """
        @brief should return False if file is present.
        """
        text = 'Another Example Test!'
        original_text = "This line should be present in the file"
        path = os.getcwd() + '/test.txt'

        if os.path.isfile(path):
            os.remove(path)
        out_file = open(path, "w")
        out_file.write(original_text)
        out_file.close()

        self.assertEqual(WriteValue(path, [text]), False)

        in_file = open(path, "r")
        in_file_text = in_file.read()
        in_file_text = in_file_text.strip()
        in_file.close()
        self.assertEqual(original_text, in_file_text)
        os.remove(path)
