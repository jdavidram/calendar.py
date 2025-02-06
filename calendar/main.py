from datetime import datetime
import calendar

festivosFijos   = [[1, 1],
                   [1, 5],
                   [20, 7],
                   [7, 8],
                   [8, 12],
                   [25, 12]]    #[DD, MM]

festivosVariables   = [[6, 1],
                       [24, 3],
                       [17, 4],
                       [18, 4],
                       [2, 6],
                       [23, 6],
                       [30, 6],
                       [18, 7],
                       [13, 10],
                       [3, 11],
                       [17, 11]]      #[DD, MM] 2025


festivos_2025   = festivosFijos +  festivosVariables

def calendario():
    year = str(datetime.now().year)
    with open("calendar.html", "w", encoding="utf-8") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html lang='es'>\n")
        file.write("<head>\n")
        file.write("<meta charset='UTF-8'>\n")
        file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        file.write("<title>Calendario " + year + "</title>\n")
        file.write("<link rel='stylesheet' href='./styles/style.css'>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<span><h1>Calendario " + year + "</h1></span>\n")
        for m in range(1, 13, 1):
            file.write("<div class='month'><h2>" + calendar.month_name[m] + "</h2>\n")
            file.write("<table>\n")
            file.write("<thead><tr><th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th></tr></thead><tbody>\n")
            cal = calendar.monthcalendar(2025, m)
            if len(cal) < 6:
                cal.append([0]*7)
            for w in cal:
                file.write("<tr>\n")
                for d in w:
                    file.write(f"<td>{d if d != 0 else ''}</td>\n")
                file.write("</tr>\n")
            file.write("</tbody></table></div>\n")
        file.write("</body>\n")
        file.write("</html>\n")
        file.close()
    print("El calendario para " + year + " ha sido generado y guardado como 'calendar.html'.")

if __name__ == "__main__":
    calendario()
