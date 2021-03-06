##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

import os
import gzip
import pickle


class StringAttributeObject(dict):
    def __setattr__(self, k, v):
        self[k] = v

    def __getattr__(self, k):
        return self.get(k, str(k))


def load_pickle(self, filename):
    with gzip.open(os.path.join(
            os.path.dirname(__file__),
            'data',
            self.__class__.__name__,
            '{}.pkl.gz'.format(filename)), 'rb') as f:
        return pickle.load(f)


def load_pickle_file(self, filename):
    with open(os.path.join(os.path.dirname(__file__), 'data', '{}.pickle'.format(filename)), 'r') as f:
        return pickle.load(f)


def test_suite(testnames):
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    for testname in testnames:
        suite.addTest(makeSuite(testname))
    return suite
