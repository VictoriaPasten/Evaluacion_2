from django.shortcuts import render

def index(request):
    videojuegos = [
        {'name': 'The Legend of Zelda', 'genero': 'Acción-Aventura', 'plataforma': 'Varias', 'año': '1986','desarrollador':'Nintendo' ,'image': 'zelda.jpg'},
        {'name': 'Super Mario Bros', 'genero': 'Plataformas', 'plataforma': 'Varias', 'año': '1985','desarrollador':'Nintendo', 'image': 'mario.jpg'},
        {'name': 'Minecraft', 'genero': 'Sandbox', 'plataforma': 'Varias', 'año': '2011', 'desarrollador':'Mojang','image': 'minecraft.jpg'},
    ]

    selected_game = request.GET.get('game', 'The Legend of Zelda')

    context = {
        'videojuegos': videojuegos,
        'selected_game': next(filter(lambda x: x['name'] == selected_game, videojuegos), None)
    }

    return render(request, 'GaleriaApp/index.html', context)
