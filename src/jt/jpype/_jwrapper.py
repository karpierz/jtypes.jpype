# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from ..jtypes      import _jwrapper
from ..jtypes._jvm import JVM


class JBoolean(_jwrapper.jboolean):

    jvm = JVM._jvm_ref()


class JChar(_jwrapper.jchar):

    jvm = JVM._jvm_ref()


class JByte(_jwrapper.jbyte):

    jvm = JVM._jvm_ref()


class JShort(_jwrapper.jshort):

    jvm = JVM._jvm_ref()


class JInt(_jwrapper.jint):

    jvm = JVM._jvm_ref()


class JLong(_jwrapper.jlong):

    jvm = JVM._jvm_ref()


class JFloat(_jwrapper.jfloat):

    jvm = JVM._jvm_ref()


class JDouble(_jwrapper.jdouble):

    jvm = JVM._jvm_ref()


class JString(_jwrapper.jstring):

    jvm = JVM._jvm_ref()


class JObject(_jwrapper.jobject):

    jvm = JVM._jvm_ref()


del _jwrapper
del JVM
