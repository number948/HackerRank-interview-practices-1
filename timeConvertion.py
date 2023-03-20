def timeConvertion(s):
    
    borde = "12"
    letra = s[-2:]
    hora = s[0:2]
    am = "AM"
    pm = "PM"
    
    if s[0:2] == borde and letra == pm: 
        s_nuevo = s.replace("PM", "  ")
        return s_nuevo
    
    elif s[0:2] == borde and letra == am: 
        s_nuevo = s.replace("12", "00")
        s_nuevo_sin_am = s_nuevo.replace("AM", " ")

        return s_nuevo_sin_am
   
    elif s[0:2] <= "11" and letra == am:
        s_nuevo_am = s.replace("AM", "  ")
        return s_nuevo_am
    
    elif s[0:2] <= "11" and letra == pm:
        int_hora = int(hora)
        hora_actual = int_hora + 12
        parseo= str(hora_actual)
        s_nuevo_pm = s.replace(hora, parseo)
        s_nuevo_pm_sin_pm = s_nuevo_pm.replace("PM", " ")

        return s_nuevo_pm_sin_pm

    
print(timeConvertion("04:05:45PM"))