#!/usr/bin/python3

# This file is part of bundlereducer, a tool to extract topology
# subsets from deployer bundle yaml files.
#
# Author, maintainer:  Ryan Beisner <ryan.beisner@canonical.com>
#
# Copyright 2016 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from bundle_reducer import reducer_cli


if __name__ == '__main__':
    sys.exit(reducer_cli.main())
