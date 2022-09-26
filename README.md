# ProgSIs

-*-*-*-*-*-*-*-*-*-ENSAMBLADOR-*-*-*-*-*-*-*-*-*-

Con la instalación de "nasm" y "minGW" y con la ayuda de los videos de

la maestra agregamos las variables de entornos para poder hacer posibles

los comandos desde CMD o Windows PowerShell.

Con ayuda de nuestro bloc de notas podemos creamos nuestro codigo en lenguaje

esamblador con la extensión .asm, despues con ciertos comados en Windows

Powershell o en CMD creamos nuestros archivos .obj (nasm -fwin32 .\hola.asm) y 

finalmente el .exe (gcc .\hola.obj -o holakk.exe), finalmente arrastramos

el .exe al PowerShell o al CMD para correr nuestro programa.

-*-*-*-*-*-*-*-*-*-BIBLIOTECAS-*-*-*-*-*-*-*-*-*-

Creamos tres archivos dos con formato .cpp y otro de formato .h

para hacer nuestra biblioteca estatica compilamos con (> g++ -c foo.cpp) en cmd

posteriormente con (> ar rcs libfoo.a foo.o), luego con (> g++ -c main.cpp) y 

finalmente con (> g++ -o main.exe main.o -L. -lfoo)

para hacer una biblioteca solo tenemos que hacer los siguientes comandos con 

los mismos archivos:

          1.-(> g++ -fPIC --shared -o foo.dll foo.cpp)

          2.-(> nm foo.dll)

          3.-(> g++ -L. -lfoo -o main main.cpp)
          
TODOS LOS ARCHIVOS .EXE LOS EJECUTAMOS ARRASTRANDOLOS AL CMD O AL POWERSHELL
