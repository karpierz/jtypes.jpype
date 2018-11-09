# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# FIXME this class is entirely replaced with calls to .class_ and
# should likely be deprecated.


def getModifiers(jclass):

    """Returns the Java language modifiers for this class or interface,
    encoded in an integer."""

    return jclass.class_.getModifiers()


def getConstructors(jclass):

    """Returns an array containing Constructor objects reflecting all the public
    constructors of the class represented by this Class object."""

    return jclass.class_.getConstructors()[:]


def getDeclaredConstructors(jclass):

    """Returns an array of Constructor objects reflecting all the constructors
    declared by the class represented by this Class object."""

    return jclass.class_.getDeclaredConstructors()[:]


def getMethods(jclass):

    """Returns an array containing Method objects reflecting all the public
    member methods of the class or interface represented by this Class object,
    including those declared by the class or interface and those inherited
    from superclasses and superinterfaces."""

    return jclass.class_.getMethods()[:]


def getDeclaredMethods(jclass):

    """Returns an array of Method objects reflecting all the methods declared
    by the class or interface represented by this Class object."""

    return jclass.class_.getDeclaredMethods()[:]


def getFields(jclass):

    """Returns an array containing Field objects reflecting all the accessible
    public fields of the class or interface represented by this Class object."""

    return jclass.class_.getFields()[:]


def getDeclaredFields(jclass):

    """Returns an array of Field objects reflecting all the fields declared
    by the class or interface represented by this Class object."""

    return jclass.class_.getDeclaredFields()[:]
