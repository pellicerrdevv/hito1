def procesar_usuario(datos):

    return{
        "login": datos["login"],
        "repos": datos["public_repos"],
        "followers": datos["followers"],
        "location": datos["location"]
    }
    