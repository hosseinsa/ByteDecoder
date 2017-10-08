#! user/bin/env python
# --coding: ascii--

"""
@file Setup.py
@author Hossein Sarpanah
@version 1.0.0
@brief Generates an .EXE
@details The generated exe IS NOT an installer, is the program itself
@note None
@bug None
@warning None
@date 02-10-2017
"""

from subprocess import check_output

print check_output("pyinstaller Decoder.py --onefile", shell= True)