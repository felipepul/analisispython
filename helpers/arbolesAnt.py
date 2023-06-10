def crearTabla(dataFrame,nombreTabla):
    archivoHTML=dataFrame.to_html()
    archivo=open(f"./tables/{nombreTabla}.html","w")
    archivo.write(archivoHTML)
    archivo.close()