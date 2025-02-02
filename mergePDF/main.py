import PyPDF2
 
def mergePDF(numPDF, output):
    merge = PyPDF2.PdfMerger()
    for p in range(1, numPDF +1, 1):
        pdf = str(p) + ".pdf"
        merge.append(pdf)
    with open(output, 'wb') as file:
        merge.write(file)
    print(f'PDFs fusionados exitosamente en { file }')
 
if __name__ == "__main__":
    numPDF = int(input("Ingrese el numero de archivos a fusionar: "))
    output = str(input("Ingrese el nombre del archivo de salida: "))
    mergePDF(numPDF, output)
