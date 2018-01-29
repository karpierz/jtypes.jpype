# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# <AK> added
#

from __future__ import absolute_import

from . import common


class GuiTestCase(common.JPypeTestCase):

    def testGuiImports(self):

        from jt.jpype import awt
        self.assertTrue(hasattr(awt, "event"))
        from jt.jpype.awt import event
        self.assertIs(awt.event, event)
        self.assertTrue(hasattr(awt.event, "WindowAdapter"))
        from jt.jpype.awt.event import WindowAdapter
        self.assertIs(awt.event.WindowAdapter, WindowAdapter)

        from jt import jpypex
        self.assertTrue(hasattr(jpypex, "swing"))
        from jt.jpypex import swing
        self.assertIs(jpypex.swing, swing)
        self.assertTrue(hasattr(jpypex.swing, "AbstractAction"))
        from jt.jpypex.swing import AbstractAction
        self.assertIs(jpypex.swing.AbstractAction, AbstractAction)

