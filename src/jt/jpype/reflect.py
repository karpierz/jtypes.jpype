# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


def getModifiers(jclass):

    """Returns the Java language modifiers for this class or interface,
    encoded in an integer."""

    return int(jclass.__javaclass__.getRawModifiers())


def getConstructors(jclass):

    """Returns an array containing Constructor objects reflecting all the public
    constructors of the class represented by this Class object."""

    ctors = jclass.__javaclass__.getConstructors()
    if not ctors: return ()
    ctor_class = ctors[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(ctor_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(ctor))
                 for ctor in ctors)


def getDeclaredConstructors(jclass):

    """Returns an array of Constructor objects reflecting all the constructors
    declared by the class represented by this Class object."""

    ctors = jclass.__javaclass__.getDeclaredConstructors()
    if not ctors: return ()
    ctor_class = ctors[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(ctor_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(ctor))
                 for ctor in ctors)


def getMethods(jclass):

    """Returns an array containing Method objects reflecting all the public
    member methods of the class or interface represented by this Class object,
    including those declared by the class or interface and those inherited
    from superclasses and superinterfaces."""

    methods = jclass.__javaclass__.getMethods()
    if not methods: return ()
    method_class = methods[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(method_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(meth))
                 for meth in methods)


def getDeclaredMethods(jclass):

    """Returns an array of Method objects reflecting all the methods declared
    by the class or interface represented by this Class object."""

    methods = jclass.__javaclass__.getDeclaredMethods()
    if not methods: return ()
    method_class = methods[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(method_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(meth))
                 for meth in methods)


def getFields(jclass):

    """Returns an array containing Field objects reflecting all the accessible
    public fields of the class or interface represented by this Class object."""

    fields = jclass.__javaclass__.getFields()
    if not fields: return ()
    field_class = fields[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(field_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(fld))
                 for fld in fields)


def getDeclaredFields(jclass):

    """Returns an array of Field objects reflecting all the fields declared
    by the class or interface represented by this Class object."""

    fields = jclass.__javaclass__.getDeclaredFields()
    if not fields: return ()
    field_class = fields[0].getClass()
    thandler = jclass.__jvmstate__.type_handler.get_handler(field_class)
    jt_jvm   = jclass.__jvmstate__.jt_jvm
    return tuple(thandler.toPython(jt_jvm.JObject.fromObject(fld))
                 for fld in fields)
