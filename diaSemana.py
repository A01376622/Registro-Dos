#Autor:

def calcularDiaSemana(numeroDia):
    if numeroDia == 0:
        return "Domingo"
    elif numeroDia == 1:
        return "Lunes"
    elif numeroDia == 2:
        return "Martes"
    elif numeroDia == 3:
        return "Miércoles"
    elif numeroDia == 4:
        return "Jueves"
    elif numeroDia == 5:
        return "Viernes"
    elif numeroDia == 6:
        return "Sábado"
    else:
        return "Día inválido"