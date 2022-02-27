class Polindroma():
  miCadenaDeTexto = ""
  def es_polindroma(miCadenaDeTexto):
    def quita_acentos(s):
      replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
      for a, b in replacements:
        s = s.replace(a, b)
        return s
        #s cadena sin tildes
    
    

#aqui quito los espacios si los hay y lo pongo en minisculas
  
    if quita_acentos(miCadenaDeTexto).lower().replace(" ", "")== quita_acentos(miCadenaDeTexto).lower().replace(" ", "")[::-1]:
      print(quita_acentos(miCadenaDeTexto).lower().replace(" ",""))
      print("Es polindroma")
      
    else:
      print(quita_acentos(miCadenaDeTexto).lower().replace(" ",""))
      print("No es polindroma")
      
#funcion que quita los acentos
  
  es_polindroma("Salás")