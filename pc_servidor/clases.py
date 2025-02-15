class Jugador():
    def __init__(self):
        self.nombre_de_usuario = ' '
        self.nombre = ' '
        self.puntos = 0
        self.estado = True
        self.cartas_obt = []

    def iniciarSesion(self):
        print("\n-----------------------------------------------------\n")
        self.nombre_de_usuario = input("Ingrese su nombre de usuario: ")
        self.nombre = input("Ingrese su nombre: ")
        print("\n-----------------------------------------------------\n")

    def calcularPuntos(self):
        self.puntos = 0
        for n in range(len(self.cartas_obt)):
            self.puntos += self.cartas_obt[n]
        if(self.puntos == 21):
            self.estado = False
        elif(self.puntos > 21):
            for n in range(len(self.cartas_obt)):
                if(self.cartas_obt[n] == 11):
                    self.cartas_obt[n] = 1
                    self.calcularPuntos()
                    return
            self.estado = False
        else:
            pass

    def robarCarta(self, carta, valor, tipo):
        self.cartas_obt.append(valor)
        print(carta, " de ", tipo)
        self.calcularPuntos()

    def seguirJugando(self):
        print("Ingrese 'n' si desea plantarse")
        print("Ingrese 'y' si desea robar otra carta")
        entrada = input()
        if(entrada == 'n' or entrada == 'y'):
            if(entrada == 'n'):
                self.estado = False
        else:
            print("Ingreso una opcion invalida.")
            self.seguirJugando()


class Carta():
    def __init__(self, n, t, i):
        self.numero = n
        if(self.numero >= 10):
            self.valor = 10
        elif(self.numero == 1):
            self.valor = 11
        else:
            self.valor = n
        if(t == 0):
            self.tipo = 'corazon'
        elif(t == 1):
            self.tipo = 'diamante'
        elif(t == 2):
            self.tipo = 'trebol'
        else:
            self.tipo = 'pica'
        self.id = i


class Partida():
    def __init__(self, _cant_j, _estado):
        self.cant_j = _cant_j
        self.estado = _estado
        
    def preguntarOtraPartida(self):
        print("¿Desea volver a jugar? Introducza 'y' o 'n'")
        entrada = input()
        if(entrada == 'n' or entrada == 'y'):
            if(entrada == 'n'):
                self.estado = False
        else:
            print("Ingreso una opcion invalida.")
            self.preguntarOtraPartida()
