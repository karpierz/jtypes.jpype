#
# porting for PY3, reformated (PEP8) and adopted for jt.jpype by Adam Karpierz
#

from __future__ import absolute_import, division, print_function

from jt.jpype import *
import time

NUMMSGS = 10

def pyPublisher(javaNamingFactory="weblogic.jndi.WLInitialContextFactory",
                javaNamingProvider="t3://158.188.40.21:7001",
                connectionFactory="weblogic.jms.ConnectionFactory",
                topicName="defaultTopic"):
    return messaging.JpypePublisher(javaNamingFactory, javaNamingProvider,
                                    connectionFactory, topicName)

## Startup Jpype and import the messaging java package
startJVM(None,
         "-Djava.class.path=D:/jIRAD/JpypeJMS/src;D:/jIRAD/JpypeJMS/classes;"
         "C:/bea/weblogic81/server/lib/weblogic.jar")
messaging = JPackage('messaging')

# Get a publisher
publisher = pyPublisher()

## Timing test
# The "Start" message signals the subscriber to start timing message receipts
publisher.publish("Start")

t0 = time.time()
for i in range(NUMMSGS):
    publisher.publish("Hello World! %s" % i)
print("MessageRate =", float(NUMMSGS) / (time.time() - t0))

# The "Stop" message signals the subscriber to stop timing message receipts
publisher.publish("Stop")

# Close and quit
publisher.close()
shutdownJVM()
