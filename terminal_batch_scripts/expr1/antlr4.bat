::java org.antlr.v4.Tool %*
java -jar C:\Javalib\antlr-4.5.3-complete.jar *.g4
javac -cp C:\Javalib\antlr-4.5.3-complete.jar *.java

set /P id=Enter Grammar Name: 
java -cp .;C:\Javalib\antlr-4.5.3-complete.jar org.antlr.v4.gui.TestRig %id% prog in.txt -tree -gui
set /P id2=Press any key ... 