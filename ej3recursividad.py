bandera =["R","B","B","R","G","B","B","R","B","R","R","G","R","R","B","G","G"]
print(bandera)
rojo=[]
verde=[]
azul =[]
def bandera_dijkstra(bandera):
  if len(bandera) > 0:
    color=bandera.pop(0)
    if color =="R":
      rojo.append(color)
      bandera_dijkstra(bandera)
    elif color =="G":
      verde.append(color)
      bandera_dijkstra(bandera)
    elif color =="B":
      azul.append(color)
      bandera_dijkstra(bandera)
    else:
      bandera_final=rojo+verde+azul
      print(f"La bandera ordenada es {bandera_final}")
  else:
      bandera_final=rojo+verde+azul
      print(f"La bandera ordenada es {bandera_final}")
bandera_dijkstra(bandera)
    