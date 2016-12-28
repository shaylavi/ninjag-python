# Ninjag
A python package for generating `ninja` build configuration files based on user input YAML files

## Install
This is a python command line app.  
After the input you will have `ninjag` command
on your path.
```
pip install ninjag
```

## Dependency
* [PyYAML](https://github.com/yaml/pyyaml)

## Background knowledge
* [YAML format](https://learn.getgrav.org/advanced/yaml)
* [ninja manual](https://ninja-build.org/manual.html#_introduction)

## Usage
The first argument is the output file name,  
The rest of the arguments are input files.
```
ninjag <output file> <input file 1> <input file 2> ...
```

In the input `yaml` file, there are three required sections:  
* const: a dictionary of `ninja` constant definitions
* rules: a dictionary of `ninja` rules definitions
* tasks: a list of dictionaries of `ninja` build tasks.  
  - rule: which `ninja` rule to apply for this task
  - in: a `list` of input file names
  - out: a `list` of output file names
  - const: a dictionary  of local constant definitions,  
    which have higher priority than the global constants
Note that `in` and `out` are `ninja` built-in keywords,  
and must be written as the way they are.


## Examples
input1.yaml
```
const:
  cflags: -Wall -Wconversion -Wextra

rules:
  cc: gcc $cflags $in -o $out

tasks:
- rule: cc
  in: [hello.c]
  out: [hello.exe]
  const:
    cflags: -Wall

```

Then type command:
```
ninjag build.ninja input1.yaml
```
The output is (`build.ninja`):
```
cflags = -Wall -Wconversion -Wextra

rule cc
  command = gcc $cflags $in -o $out

build hello.exe: cc hello.c
  cflags = -Wall

```

## License
MIT/X11 Steven(Yuhang) Wang (c) 2016
