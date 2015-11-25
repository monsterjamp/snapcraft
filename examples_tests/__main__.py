# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import logging
import sys
import unittest

from examples_tests import tests


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--skip-install',
        help=('skip the tests that install the example snaps into a snappy '
              'virtual machine'),
        action='store_true')
    args = parser.parse_args()
    if args.skip_install:
        tests.config['skip-install'] = True

    # Strip all the command line arguments, so unittest does not handle them
    # again.
    argv = [sys.argv[0]]
    unittest.main('examples_tests.tests', verbosity=2, argv=argv)


if __name__ == '__main__':
    main()
