#-------------------------------------------------------------------------------
# LLVM emulator of x86
#
# This emulates an x86 processor in LLVM.
#-------------------------------------------------------------------------------

# For compatibility with Python 3
from __future__ import print_function

# Imports
from llvm import *
from llvm.core import *


#-------------------------------------------------------------------------------
# Decorators
#-------------------------------------------------------------------------------

def Instruction(f):
	
	def new_f(self, instruction):
		print(instruction.mnemonic+" found.") 
		return f(self, instruction)
		
	return new_f


#-------------------------------------------------------------------------------
# Emulation
#-------------------------------------------------------------------------------

# Emulation of x86 in LLVM
class Emulator(object):

	def __init__(self, name, symbol_table):
		self.module = Module.new(name)
		self.symbol_table = symbol_table

	@Instruction
	def PUSH(self, instruction):
		pass

	@Instruction
	def XOR(self, instruction):
		pass

	@Instruction
	def DEC(self, instruction):
		pass

	@Instruction
	def SUB(self, instruction):
		pass

	@Instruction
	def MOV(self, instruction):
		pass

	@Instruction
	def LEAVE(self, instruction):
		pass

	@Instruction
	def CALL(self, instruction):
		pass

	@Instruction
	def RET(self, instruction):
		pass

