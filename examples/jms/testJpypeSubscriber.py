#
# porting for PY3, reformated (PEP8) and adopted for jt.jpype by Adam Karpierz
#

from __future__ import absolute_import, division, print_function

from jt.jpype import *
import time


def pySubscriber(proxy,
                 javaNamingFactory="weblogic.jndi.WLInitialContextFactory",
                 javaNamingProvider="t3://158.188.40.21:7001",
                 connectionFactory="weblogic.jms.ConnectionFactory",
                 topicName="defaultTopic"):
    return messaging.JpypeSubscriber(proxy,
                                     javaNamingFactory, javaNamingProvider,
                                     connectionFactory, topicName)


## Startup Jpype and import the messaging java package
startJVM(None,
         "-Djava.class.path=D:/jIRAD/JpypeJMS/src;D:/jIRAD/JpypeJMS/classes;"
         "C:/bea/weblogic81/server/lib/weblogic.jar")
messaging = JPackage('messaging')


# Setup the JProxy for the messaging.JpypeSubscriberCallback interface
class pyCallback:

    startTime = 0
    count = 0

    def onMessage(self, text):
        print(text)
        if text == 'Start':
            pyCallback.startTime = time.time()
            pyCallback.count = 0
        elif text == 'Stop':
            print("Message Rate =",
                  float(pyCallback.count) / (time.time()-pyCallback.startTime))
        else:
            pyCallback.count += 1


c = pyCallback()
proxy = JProxy(messaging.JpypeSubscriberCallback, inst=c)

# Get a subscriber
sub = pySubscriber(proxy)
print("Listening...")

# Prevent this thread from exiting
time.sleep(1000)

# exit
shutdownJVM()
