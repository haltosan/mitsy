# Mitsy

A language built off the idea that Mov Is Turing Complete (mitc, mitsy phonetically)

[![Run on Repl.it](https://repl.it/badge/github/haltosan/mitsy-compiler#)](https://repl.it/github/haltosan/mitsy-compiler#)

## About

This is an odd project of mine. You might want to see a [project](https://github.com/haltosan/comp-sci-final) using this for a better understanding. Basically, this compiles a *higher* level language to something akin to mov instructions (like the [movfuscator](https://github.com/xoreaxeaxeax/movfuscator)). If looking at just the "mov" instructions, it is very hard to understand what is going on. Unlike popular languages, this is yet to have a decompiler so this system is pretty good at obfuscation (making everything impossible to understand).

## Use

The compiler is pretty simple. Write in the 'in.mitc' file, the output will be in out.bc. Use **option 1** to compile. It will compile to a list of mitc commands for debugging, but **option 3** will clean it up to allow you to run it in the mvm (mitsy virtual machine). Use **option 2** to allocate more memory for specific purposes. Similar to Java, this compiles to bytecode and then is run inside a virtual machine ([mvm](https://github.com/haltosan/mvm)). This virtual machine can be created in any language to obfuscate any section of a program.

### Syntax

For syntax, see the 'documentation.md' file. Most of the documentation is up to date, just check the source if you think a command doesn't exist. The translation gives the compiler rounds, what instructions compile to, and what instructions aren't finished.
