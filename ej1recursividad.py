lista_palabras=["Alien","Eduardo","Cabeza","Rubén","Javier","Atlas","Río", "Servir", "Abrir","Camión", "Ordenador", "Mandaloriano", "Conflicto", "Móvil", "Estambul","Wifi", "Nft", "Real Madrid","Dicotomía","Gafas", "Pesado", "Bicicleta","Reloj", "Abrigo", "Criptoestafa", "Emblemático","Inanición","Comunicación","Ifema","Spa","Auditorio","Campo", "Bernabéu", "Iluminati", "Copiar", "Libre", "Como", "El", "Mar"]
print(lista_palabras)
cota_sup=len(lista_palabras)
mitad=((cota_sup)//2)
print("¿Que palabra quieres buscar?")
palabra_introducida=str(input())

def dicotomia(mitad):
  numero_tabla=lista_palabras.index(palabra_introducida)
  if numero_tabla==mitad:
     print(f"La palabra {palabra_introducida} se encuentra en el índice {numero_tabla}")
  elif numero_tabla< mitad:
   dicotomia(mitad-1)
  elif  numero_tabla > mitad:
   dicotomia(mitad+1)

dicotomia(mitad)