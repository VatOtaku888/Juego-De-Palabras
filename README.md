# Juego de palabras!!

#### ERRORES COMUNES

Te recomiendo no poner str en las preguntas Numericas

Puede causar algun error al programa

---
#### DATOS


> por accidente puse que el programa es una calculadora enrealidad es un juego de palabras
este programa lo hice por diversion
Y es un codigo simple No es una app solo es un codigo hecho por diversion y lo queria compartir con ustedes!!
---

 #### INSTALACIÓN: 
```python
C:\Users\vatma>cd Escritorio

C:\Users\vatma\Escritorio>cd Juego_De_Palabras
#Ejecucion
C:\Users\vatma\Escritorio\Juego_De_Palabras>python Code.py
#Si no te deja poner cd Escritorio puedes hacer esto 
C:\Users\vatma>cd One Drive

C:\Users\vatma\OneDrive>cd Escritorio

C:\Users\vatma\OneDrive\Escritorio>cd Juego_De_Palabras

C:\Users\vatma\OneDrive\Escritorio\Juego_De_Palabras>python Code.py
```
**Un Ejemplo De el resultado** 
[](https://cdn.discordapp.com/attachments/698548898129510500/849768107002167306/Gameplay.png)
Para empezar la instalacion debes darle click [Aqui](https://www.mediafire.com/folder/cyzm66e2hw0xi/Juego_De_Palabras)

**Sigue los siguientes pasos de las imagenes para ejecutarlo**

 ![](https://cdn.discordapp.com/attachments/698548898129510500/849768107002167306/Gameplay.png)

  #### CODIGO 
**Code.py**
```python
#..........MODULOS.......#
import colorama #Modulo de colores
from colorama import Fore, Back, Style #Estilos de colores
colorama.init (autoreset = True) # Colores

#......Presentation.....#
print(Fore.BLUE + '''
      .....       .....                .....       .....
     .......     .......              .......     .......
    .........   .........            .........   .........
   ........... ........... COMIENZA ........... ...........
   ........... ...........          ........... ...........
    .........   .........            .........   .........
     .......     .......              .......     .......
      .....       .....                .....       .....
      ''')

#........Variables......#
print(Fore.GREEN + ''' 
    Juego de palabras
    Escribe start para jugar y cancel para no jugar!!
    si no pones ninguna de las dos te va a salir un error
    Asi que preparate!!
      
      ''')
Value = str(input(Fore.YELLOW + "\nOption:")) #input para elegir si quieres empezar el juego o no




#........Code..........#
if Value == "Start" or Value == "start" or Value == "START": #Opcion para comenzar el juego
    print(Fore.GREEN + '''
     MUY BIEN EMPIEZA EL JUEGO!!!

    ........PRIMERA PREGUNTA......
    ¿Cuanto es 4 + 4?

          ''')
    Respuesta = int(input(Fore.YELLOW + "\nQuestion:")) #Input para responder la respuesta
#....PRIMERA PREGUNTA...#
    if Respuesta == 8: #Condicional de la primera pregunta
        print(Fore.GREEN + f'''
    CORRECTO!! 4 + 4 es {Respuesta}

    .......SEGUNDA PREGUNTA.........
    ¿Cuanto es 6 x 6?
              ''')
        Respuesta2 = int(input(Fore.YELLOW + "\nQuestion2:")) # input Para responder la pregunta2
#.....SEGUNDA PREGUNTA..#
        if Respuesta2 == 36: # Condicional De la pregunta2
            print(Fore.GREEN + f'''
    Wow wow correcto es {Respuesta2}

    ........TERCERA PREGUNTA.......
    ¿a cuantos años puedes para entrar a discord?
                  ''')
            Respuesta3 = int(input(Fore.YELLOW + "\nQuestion3:")) #Input de la pregunta
#......TERCERA PREGUNTA.#
            if Respuesta3 == 13: # condicional de la pregunta
                print(Fore.GREEN + f'''
    Correcto necesitas o {Respuesta3}!!!

    ........Ultima Pregunta........
    ¿Quien es el creador de facebook?
                     ''')
                Respuesta4 = str(input(Fore.YELLOW + "\nQuestion4:"))
#.....ULTIMA PREGUNTA..#
                if Respuesta4 == "Mark Zuckerberg" or Respuesta4 == "mark zuckerberg" or Respuesta4 == "zuckerberg" or Respuesta4 == "Mark" or Respuesta4 == "MARK ZUCKERBERG" or Respuesta4 == "mark" or Respuesta4 == "MARK": #lista de respuestas validas
                    print(Fore.GREEN + f'''
    CORRECTO!! LA RESPUESTA ES {Respuesta4}
    ESO ES TODO POR HOY!!! 
    Creditos: Twitter:@VatOtaku,Youtube: vat otaku
    Bonus.... End Or Bonus?
                          ''')
#......BONUS............#
                    Bonus_1 = str(input(Fore.YELLOW + "\nBonus:")) #input del bonus
                    if Bonus_1 == "Bonus" or Bonus_1 == "bonus" or Bonus_1 == "BONUS": #Bonus Condicional
                    
                        print(Fore.GREEN + '''
    ........BONUS QUESTION....
    ¿Eri gei? Sis Non
                        ''')
                        SisONon = str(input(Fore.YELLOW + "\nSisNon:")) # Opciones
                        if SisONon == "Sis" or SisONon == "sis" or SisONon == "SIS": #Condicional Opciones
                              print(Fore.RED + '''
    JAJAJAJA ERI GEI WEON
                              ''')
                        elif SisONon == "Non" or SisONon == "non" or SisONon == "NON": # Opcion 2 Condicional
                              print(Fore.GREEN + '''
    Non Erigei???? altocrak
                            ''')
                        else: #Opcion no valida
                            print(Fore.RED + ''' 
    Eres Mas Gei Non Dijiste Sis o Non :rage:
                            ''')
                    elif Bonus_1 == "End" or "end" or "END": # opcion End Cancelar Bonus
                        print(Fore.RED + '''
    Termina el juego Adios!!
                        ''')
                    else: #Opcion invalida
                        print(Fore.GREEN + '''
    No elegiste una opcion Valida
                        ''')        
#..PREGUNTA INCORRECTA.#
                else: # Respuesta incorrecta o mal escrita
                    print(Fore.RED + f'''
    Revisa si escribiste bien el nombre o si es el verdadero propietario
                          ''')

#.RESPUESTA INCORRECTA.#
            else: #Edad No valida o no exacta
                print(Fore.RED + f'''
    Incorrecto No es {Respuesta3} debe ser la edad exacta no menor o mayor de la edad que se debe poner
                       ''')
            
#...RESPUESTA INCORRECTA#
        else: #Operacion incorrecta
            print(Fore.RED + f'''
    Incorrectoo!! es {Respuesta2}
                  ''')
    else: #Operacion incorrecta
        print(Fore.RED + f'''
    INCORRECTO 4 + 4 NO ES {Respuesta}!!!
              ''')

#.......CANCEL.........#

elif Value == "cancel" or Value == "Cancel" or Value == "CANCEL": # Cancelar juego
    print(Fore.RED + '''
    Si no querias jugar por que no lo dijiste antes!!!??
    Bueno Adios mi estimado
          ''')

#......NONE_OPTION.....#

else: # Opcion invalida
    print(Fore.RED + '''
    ELIGE UNA OPCION VALIDA!!
    Usa start para jugar usa cancel 
    para no jugar
          ''')
```

