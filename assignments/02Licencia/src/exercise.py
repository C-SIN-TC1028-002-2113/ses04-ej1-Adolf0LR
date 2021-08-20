def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad>0:
        if edad>=18:
            con = input("¿Tienes identificación oficial? (s/n): ")
            if con == "n":
                print("No cumples requisitos")
            elif con == "s":
                print("Trámite de licencia concedido")
            else:
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")        
    else:
        print("Respuesta incorrecta")
  
  

if __name__ == '__main__':
    main()
