#-------------------------------------------------------------------------------
# x86toLLVM
#
# This code converts an ELF file to LLVM bitcode.
#-------------------------------------------------------------------------------

# For compatibility with Python 3
from __future__ import print_function

# Imorts
import sys
import distorm3
from elftools.elf.elffile import ELFFile


def process_file(filename):
	print('Processing file: ', filename)
	with open(filename, 'rb') as file:

		# Note, we can't close file until we have finished reading data
		elf_file = ELFFile(file)

		# Code is normally in the data section
		text_section = elf_file.get_section_by_name(".text")
		base_address = text_section.header['sh_addr']
		disassembly = distorm3.Decompose(base_address, text_section.data())
		

	return disassembly


if __name__ == '__main__':
	for filename in sys.argv[1:]:
		process_file(filename)