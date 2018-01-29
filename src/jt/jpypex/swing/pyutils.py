# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


def buildMenuBar(menuDef):

    from ...jpype import javax, JObject

    jmb = javax.swing.JMenuBar()

    for item in menuDef:
        jm = buildMenu(item[0], item[1])
        jmb.add(JObject(jm, javax.swing.JMenu))

    return jmb


def buildMenu(name, menuDef):

    from ...jpype import javax

    jm = javax.swing.JMenu(name)

    for item in menuDef:
        if item is None:
            jm.addSeparator()
        elif isinstance(item, (list, tuple)):
            jm2 = buildMenu(item[0], item[1])
            jm.add(jm2)
        else:
            jm.add(item.proxy)

    return jm
