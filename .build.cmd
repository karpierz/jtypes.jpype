@echo off
setlocal
set JAVA8_HOME=C:\Program Files\Java\jdk1.8.0_181
if not defined JAVA_HOME (set JAVA_HOME=%JAVA8_HOME%)
set javac="%JAVA_HOME%"\bin\javac -encoding UTF-8 -g:none -deprecation -Xlint:unchecked ^
    -source 1.8 -target 1.8 -bootclasspath "%JAVA8_HOME%\jre\lib\rt.jar"
pushd "%~dp0"\tests
rmdir /Q/S classes 2> nul & mkdir classes
dir /S/B/O:N ^
    harness\*.java ^
    2> nul > build.fil
%javac% -d classes -classpath harness/lib/* @build.fil
del /F/Q build.fil
popd
endlocal
