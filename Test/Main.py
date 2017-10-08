#! user/bin/env python
# --coding: ascii--

"""
@file Main.py
@author Hossein Sarpanah
@version 1.0.0
@brief This module executes the tests and provides an outcome to the user.
@details It demonstrates results in a textual interface .
@note None
@bug None
@warning None
@date 04-10-2017
"""
import unittest



from DecodingData import ExtractDataCase, FrameFromTextCase, DecodeFrameCase, DecodeListCase, PrepareDataCase, WriteValueCase

ExtractData = unittest.TestLoader().loadTestsFromTestCase(ExtractDataCase)
FrameFromText = unittest.TestLoader().loadTestsFromTestCase(FrameFromTextCase)
DecodeFrame = unittest.TestLoader().loadTestsFromTestCase(DecodeFrameCase)
DecodeList = unittest.TestLoader().loadTestsFromTestCase(DecodeListCase)
PrepareData = unittest.TestLoader().loadTestsFromTestCase(PrepareDataCase)
WriteValue = unittest.TestLoader().loadTestsFromTestCase(WriteValueCase)
Suite_Decoding = unittest.TestSuite([ExtractData,
                                     FrameFromText,
                                     DecodeFrame,
                                     DecodeList,
                                     PrepareData,
                                     WriteValue,
                                     ])

results = unittest.TextTestRunner(verbosity=2).run(Suite_Decoding)


