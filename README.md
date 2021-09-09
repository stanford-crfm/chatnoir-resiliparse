# ChatNoir Resiliparse

[![Build Wheels](https://github.com/chatnoir-eu/chatnoir-resiliparse/actions/workflows/build-wheels.yml/badge.svg)](https://github.com/chatnoir-eu/chatnoir-resiliparse/actions/workflows/build-wheels.yml)
[![Documentation Status](https://readthedocs.org/projects/chatnoir-resiliparse/badge/?version=latest)](https://resiliparse.chatnoir.eu/en/latest/?badge=latest)

A collection of robust and fast processing tools for parsing and analyzing web archive data.

Resiliparse is part of the [ChatNoir](https://chatnoir.eu/) web analytics toolkit. If you use ChatNoir or any of its tools for a publication, you can make us happy by citing our ECIR demo paper:
```bibtex
@InProceedings{bevendorff:2018,
  address =             {Berlin Heidelberg New York},
  author =              {Janek Bevendorff and Benno Stein and Matthias Hagen and Martin Potthast},
  booktitle =           {Advances in Information Retrieval. 40th European Conference on IR Research (ECIR 2018)},
  editor =              {Leif Azzopardi and Allan Hanbury and Gabriella Pasi and Benjamin Piwowarski},
  ids =                 {potthast:2018c,stein:2018c},
  month =               mar,
  publisher =           {Springer},
  series =              {Lecture Notes in Computer Science},
  site =                {Grenoble, France},
  title =               {{Elastic ChatNoir: Search Engine for the ClueWeb and the Common Crawl}},
  year =                2018
}
```

## Usage Instructions
For detailed information about the build process, dependencies, APIs, or usage instructions, please read the [Resiliparse Documentation](https://resiliparse.chatnoir.eu/en/latest/index.html)

## Resiliparse Module Summary
The Resiliparse collection encompasses the following two modules at the moment:

### 1. Resiliparse
The Resiliparse main module with the following subcomponents:

#### Parsing Utilities
The Resiliparse Parsing Utilities are the largest submodule and provide an extensive (and growing) collection of efficient tools for dealing with encodings and raw protocol payloads, parsing HTML web pages, and preparing them for further processing by extracting structural or semantic information.

For more information, see [Resiliparse Parsing Tools](docs/man/parse.rst)

#### Process Guards
The Resiliparse Process Guard module is a set of decorators and context managers for guarding a processing context to stay within pre-defined limits for execution time and memory usage. Process Guards help to ensure the (partially) successful completion of batch processing jobs in which individual tasks may time out or use abnormal amounts of memory, but in which the success of the whole job is not threatened by (a few) individual failures. A guarded processing context will be interrupted upon exceeding its resource limits so that the task can be skipped or rescheduled.

For more information, see [Resiliparse Process Guards](docs/man/process-guard.rst)

#### Itertools
Resiliparse Itertools are a collection of convenient and robust helper functions for iterating over data from unreliable sources using other tools from the Resiliparse toolkit.

For more information, see [Resiliparse Itertools](docs/man/itertools.rst)

### 2. FastWARC
FastWARC is a high-performance WARC parsing library for Python written in C++/Cython. The API is inspired in large parts by [WARCIO](https://github.com/webrecorder/warcio), but does not aim at being a drop-in replacement.  FastWARC supports compressed and uncompressed WARC/1.0 and WARC/1.1 streams. Supported compression algorithms are GZip and LZ4.

For more information, see the [FastWARC documentation](docs/man/fastwarc.rst)

## Installation
The main Resiliparse package can be installed from PyPi as follows:
```bash
pip install resiliparse
```
FastWARC is being distributed as its own package and can be installed like so:
```bash
pip install fastwarc
```
For optimal performance, however, it is recommended to build FastWARC from sources instead of relying on the pre-built binaries. See below for more information.

## Building From Source
To build Resiliparse or FastWARC from sources, you need to install all required build-time dependencies first. On Ubuntu, this is done as follows:
```bash
# Add Lexbor repository
curl -L https://lexbor.com/keys/lexbor_signing.key | sudo apt-key add -
echo "deb https://packages.lexbor.com/ubuntu/ $(lsb_release -sc) liblexbor" | \
    sudo tee /etc/apt/sources.list.d/lexbor.list

# Install build dependencies
sudo apt update
sudo apt install build-essential python3-dev zlib1g-dev \
    liblz4-dev libuchardet-dev liblexbor-dev
```
Then, to build the actual packages, run:
```bash
# Optional: Create a fresh venv first
python3 -m venv venv && source venv/bin/activate

# Build and install Resiliparse
pip install -e resiliparse

# Build and install FastWARC
pip install -e fastwarc
```
Instead of building the packages from this repository, you can also build them from the PyPi source packages:
```bash
# Build Resiliparse from PyPi
pip install --no-binary resiliparse resiliparse

# Build FastWARC from PyPi
pip install --no-binary fastwarc fastwarc
```
