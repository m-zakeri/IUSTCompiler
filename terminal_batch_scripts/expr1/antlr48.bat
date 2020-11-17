::java org.antlr.v4.Tool %*
java -jar "D:\Program Files\Java\jdk-10.0.2\bin\antlr-4.8-complete.jar" *.g4
javac -cp "D:\Program Files\Java\jdk-10.0.2\bin\antlr-4.8-complete.jar" *.java

set /P id=Enter Grammar Name: 
java -cp .;"D:\Program Files\Java\jdk-10.0.2\bin\antlr-4.8-complete.jar" org.antlr.v4.gui.TestRig %id% prog in.txt -tree -gui
set /P id2=Press any key ... 