import calendar

# Crear un archivo HTML
with open("calendar.html", "w", encoding="utf-8") as file:
    file.write("<!DOCTYPE html>\n")
    file.write("<html lang='es'>\n")
    file.write("<head>\n")
    file.write("<meta charset='UTF-8'>\n")
    file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    file.write("<title>Calendario 2025</title>\n")
    file.write("<link rel='stylesheet' href='./style.css'>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<h1>Calendario 2025</h1>\n")

    for mes in range(1, 13):
        file.write(f"<div class='month'><h2>{calendar.month_name[mes]}</h2>\n")
        file.write("<table>\n")
        file.write("<tr><th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th></tr>\n")
        
        cal = calendar.monthcalendar(2025, mes)
        for semana in cal:
            file.write("<tr>\n")
            for dia in semana:
                file.write(f"<td>{dia if dia != 0 else ''}</td>\n")
            file.write("</tr>\n")
        
        file.write("</table></div>\n")

    file.write("</body>\n")
    file.write("</html>\n")
    file.close()

print("El calendario para 2025 ha sido generado y guardado como 'calendar.html'.")
