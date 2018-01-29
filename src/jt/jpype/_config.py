# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

class ConversionConfigClass(object):

    string = property(lambda self:       getattr(self, "_flag", True),
                      lambda self, flag: setattr(self, "_flag", bool(flag)))

ConversionConfig = ConversionConfigClass()
