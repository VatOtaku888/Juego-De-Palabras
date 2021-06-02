#..........MODULOS.......#
import colorama
from colorama import Fore, Back, Style
colorama.init (autoreset = True)

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
print('''
      Juego de palabras
      Escribe start para jugar y cancel para no jugar!!
      si no pones ninguna de las dos te va a salir un error
      Asi que preparate!!
      
      ''')
Value = str(input(Fore.YELLOW + "\nOption:"))




#........Code..........#
if Value == "Start" or Value == "start" or Value == "START":
    print(Fore.GREEN + '''
       MUY BIEN EMPIEZA EL JUEGO!!!
      ........PRIMERA PREGUNTA......
      ¿Cuanto es 4 + 4?
          ''')
    Respuesta = int(input(Fore.YELLOW + "\nQuestion:"))
#....PRIMERA PREGUNTA...#
    if Respuesta == 8:
        print(Fore.GREEN + f'''
      CORRECTO!! 4 + 4 es {Respuesta}
      .......SEGUNDA PREGUNTA.........
      ¿Cuanto es 6 x 6?
              ''')
        Respuesta2 = int(input(Fore.YELLOW + "\nQuestion2:"))
#.....SEGUNDA PREGUNTA..#
        if Respuesta2 == 36:
            print(Fore.GREEN + f'''
      Wow wow correcto es {Respuesta2}
       ........TERCERA PREGUNTA.......
      ¿a cuantos años puedes para entrar a discord?
                  ''')
            Respuesta3 = int(input(Fore.YELLOW + "\nQuestion3:"))
#......TERCERA PREGUNTA.#
            if Respuesta3 == 13:
                print(Fore.GREEN + f'''

       Correcto necesitas o {Respuesta3}!!!
       ........Ultima Pregunta........
      ¿Quien es el creador de facebook?

                     ''')
                Respuesta4 = str(input(Fore.YELLOW + "\nQuestion4:"))
#.....ULTIMA PREGUNTA..#

                if Respuesta4 == "Mark Zuckerberg" or Respuesta4 == "mark zuckerberg" or Respuesta4 == "zuckerberg" or Respuesta4 == "Mark" or Respuesta4 == "MARK ZUCKERBERG" or Respuesta4 == "mark" or Respuesta4 == "Mark zuckerberg":
                  print(Fore.GREEN + f'''
                                              
      CORRECTO!! LA RESPUESTA ES {Respuesta4}
      ESO ES TODO POR HOY!!! 
      Creditos: Twitter:@VatOtaku,Youtube: vat otaku
      Bonus.. or end? para cancelar
                          ''')
            
                  Bonus_1 = str(input(Fore.YELLOW + "\nBonus:"))
                  if Bonus_1 == "Bonus" or Bonus_1 == "bonus" or Bonus_1 == "BONUS":

                        print(Fore.GREEN + '''

      ........BONUS QUESTION....

      ¿Eri gei? Sis Non
                        ''')
                        SisONon = str(input(Fore.YELLOW + "\nSisNon:"))
                        if SisONon == "Sis" or SisONon == "sis" or SisONon == "SIS":
                              print(Fore.RED + '''
      JAJAJAJA ERI GEI WEON
                              ''')
                        elif SisONon == "Non" or SisONon == "non" or SisONon == "NON":
                              print(Fore.GREEN + '''
      Non Erigei???? altocrak
                              ''')
                        else: 
                              print(Fore.RED + '''
      ERI SUPER GAY NON DIJISTE SIS O NON
                                    ''')
                  elif Bonus_1 == "End" or Bonus_1 == "end" or Bonus_1 == "END":
                              print(Fore.RED + '''
      Adios Mi estimado espero que 
      hayas disfrutado de este programa
      Bye bye!!!
                        ''')
                  else:
                              print(Fore.RED + '''
      No eligiste Ninguna opcion Que mencione o lo escribiste mal
                                    ''')
#..PREGUNTA INCORRECTA.#
            else:
                    print(Fore.RED + f'''
      Revisa si escribiste bien el nombre o si es el verdadero propietario
                          ''')

#.RESPUESTA INCORRECTA.#
            else:
                print(Fore.RED + f'''
      Incorrecto No es {Respuesta3} debe ser la edad exacta no menor o mayor de la edad que se debe poner
                       ''')
            
#...RESPUESTA INCORRECTA#
        else:
            print(Fore.RED + f'''
      ncorrectoo!! es {Respuesta2}
                  ''')
    else:
        print(Fore.RED + f'''
      INCORRECTO 4 + 4 NO ES {Respuesta}!!!
              ''')

#.......CANCEL.........#

elif Value == "cancel" or Value == "Cancel" or Value == "CANCEL":
    print(Fore.RED + '''
      Si no querias jugar por que no lo dijiste antes!!!??
      Bueno Adios mi estimado
          ''')

#......NONE_OPTION.....#

else:
    print(Fore.RED + '''
      ELIGE UNA OPCION VALIDA!!
      Usa start para jugar usa cancel 
      para no jugar
          ''')