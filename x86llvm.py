#-------------------------------------------------------------------------------
# x86toLLVM
#
# This code converts an ELF/PE file to LLVM bitcode.
#-------------------------------------------------------------------------------

# For compatibility with Python 3
from __future__ import print_function

# Imports
import sys
import distorm3
from elftools.elf.elffile import ELFFile

from emulator import Emulator


def process_file(filename):
	print('Processing file: ', filename)
	with open(filename, 'rb') as file:

		# Note, we can't close file until we have finished reading data
		elf_file = ELFFile(file)

		# Code is normally in the data section
		text_section = elf_file.get_section_by_name(".text")
		base_address = text_section.header['sh_addr']
		disassembly = distorm3.Decompose(base_address, text_section.data())

		# Get the symbol table as table of addresses mapped to names
		symbol_table_section = elf_file.get_section_by_name(".symtab")
		symbol_table = {} # TODO: Fill in the symbol table...

		# Create an LLVM emulator
		emulator = Emulator("module", symbol_table)
		for instruction in disassembly:
			if hasattr(emulator, instruction.mnemonic):
				method = getattr(emulator, instruction.mnemonic)
				method(instruction)
			else:
				print(instruction.mnemonic+" not implemented yet. Please implement it!")

	return disassembly


if __name__ == '__main__':
	for filename in sys.argv[1:]:
		process_file(filename)