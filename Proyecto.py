def pruebas():
    print("=== INICIO DE PRUEBAS ===")

    # Listas para manejar datos
    clientes = []
    servicios = []
    reservas = []

    # =========================
    # 1-3 CLIENTES (válidos e inválidos)
    # =========================
    try:
        clientes.append(Cliente("Ana", "123", "ana@gmail.com"))  # válido
        print("Cliente válido creado")

        clientes.append(Cliente("Luis", "456", "luisgmail.com"))  # inválido
    except Exception as e:
        guardar_log("Error cliente: " + str(e))
        print("Error controlado en cliente:", e)

    try:
        clientes.append(Cliente("", "789", "correo@gmail.com"))  # inválido
    except Exception as e:
        guardar_log("Error cliente: " + str(e))
        print("Error controlado en cliente:", e)

    # =========================
    # 4-6 SERVICIOS (correctos)
    # =========================
    try:
        servicios.append(ReservaSala("Sala", 50))
        servicios.append(AlquilerEquipo("Equipo", 30))
        servicios.append(Asesoria("Asesoría", 40))
        print("Servicios creados correctamente")
    except Exception as e:
        guardar_log("Error servicio: " + str(e))

    # =========================
    # 7-10 RESERVAS (válidas e inválidas)
    # =========================
    try:
        r1 = Reserva(clientes[0], servicios[0], 2)  # válida
        r1.confirmar()
        reservas.append(r1)
        print(r1.mostrar())
    except Exception as e:
        guardar_log("Error reserva: " + str(e))

    try:
        r2 = Reserva(clientes[0], servicios[1], 3)  # válida
        r2.confirmar()
        reservas.append(r2)
        print(r2.mostrar())
    except Exception as e:
        guardar_log("Error reserva: " + str(e))

    try:
        r3 = Reserva(clientes[0], servicios[2], -1)  # inválida
        reservas.append(r3)
    except Exception as e:
        guardar_log("Error reserva: " + str(e))
        print("Error controlado en reserva:", e)

    try:
        r4 = Reserva("cliente falso", servicios[0], 2)  # inválida
        reservas.append(r4)
    except Exception as e:
        guardar_log("Error reserva: " + str(e))
        print("Error controlado en reserva:", e)

    print("=== FIN DE PRUEBAS ===")
