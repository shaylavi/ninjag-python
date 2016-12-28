# Ninjag
A python package for generating `ninja` build configuration files based on user input YAML files

## Install
This is a python command line app.  
After the input you will have `ninjag` command
available to you.
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

The input configuration can span multiple `yaml` files,  
but the combined content must have three required sections:  
* const: a dictionary of `ninja` constant definitions
* rules: a dictionary of `ninja` rules definitions
* tasks: a list of dictionaries of `ninja` build tasks.  
  - rule: which `ninja` rule to apply for this task
  - in: a `list` of input file names
  - out: a `list` of output file names
  - const: a dictionary  of local constant definitions,  
    which have higher priority than the global constants
Notes:
* `in` and `out` are `ninja` built-in keywords.  
  they must be written as the way they are.
* `in` and `out` can be either a string or a list of strings
* the `rules` and `tasks` sections from multiple inputs  
  will be concatenated, but `const` definitions will be  
  overridden (files specified later have higher priority)


## Examples
input1.yaml
```
const:
  cflags: -Wall -Wconversion -Wextra

rules:
  cc: gcc $cflags $in -o $out

tasks:
- rule: cc
  in:
  - hello.c
  out:
  - hello.exe
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


The `const` definition can have list as value:
```
const:
  W:
  - -Wall
  - -Werror
  - -Wconversion
  I:
  - -I/home/include1
  - -I/home/include2
```
The above will be translated to:
```
W = -Wall -Werror -Wconversion
I = -I/home/include1 -I/home/include2
```

## License
MIT/X11 Steven(Yuhang) Wang (c) 2016
