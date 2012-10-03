x86 to LLVM
===========

This project aims to convert x86 files (such as ELF or PE files) to LLVM bitcode. At the moment this project is a very early planning stage.

This project will rely on several external libraries for python. These are

- [distorm3](http://code.google.com/p/distorm/) for disassembly of the PE files
- [llvm-py](http://www.mdevan.org/llvm-py/) for constructing the LLVM code
- [pyelftools](https://bitbucket.org/eliben/pyelftools/overview) for reading ELF files

Using *pyelftools* (or a PE file eqivalent) the object file will be read, disassembly will proceed using *distorm3*. The disassembled instructions will then be translated from x86 to their LLVM emulation equivalent, instruction by instruction. This part will use the *llvm-py* library which emits the bitcode.

There are many possible uses of the library once working. These might include:

- Cross compiling from one architecture to another
- Optimization of existing binaries
- Static analysis of binaries

Feel free to contribute or get in touch.
