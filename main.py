import ssl
import flet as ft

# Bypass para el error SSL en Python 3.14
ssl._create_default_https_context = ssl._create_unverified_context


def main(page: ft.Page):
    page.title = "Guía Ñuble"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.is_logged_in = False
    page.view_history = []
    page.comuna_seleccionada = {"nombre": "", "datos": {}}

    comunas_data = {
        "Cobquecura": {
            "imagen": "cobquecura.jpg",
            "descripcion": (
                "Comuna costera con olas imponentes, lobos marinos y sabores"
                " del mar."
            ),
        },
        "Coelemu": {
            "imagen": "coelemu.jpg",
            "descripcion": (
                "Viñas coloniales junto al río, refugio de enoturismo íntimo."
            ),
        },
        "Ninhue": {
            "imagen": "Ninhue.jpg",
            "descripcion": (
                "Pueblo tranquilo cuna de Prat famoso por sus Chupallas en"
                " fibras naturales."
            ),
        },
        "Portezuelo": {
            "imagen": "portezuelo.jpg",
            "descripcion": (
                "Famosa por sus viñas centenarias y río eterno, tierra de vino y"
                " memoria viva."
            ),
        },
        "Quirihue": {
            "imagen": "quirihue.jpg",
            "descripcion": (
                "Historia colonial y arquitectura, bodegas centenarias."
            ),
        },
        "Ránquil": {
            "imagen": "ranquil.jpg",
            "descripcion": (
                "Laderas de viñedos y fiesta del vino en paisaje rural."
            ),
        },
        "Trehuaco": {
            "imagen": "trehuaco.jpg",
            "descripcion": (
                "Naturaleza y tranquilidad rural, cuna ancestral de Lautaro."
            ),
        },
        "Bulnes": {
            "imagen": "bulnes.jpg",
            "descripcion": "Historia ferroviaria y corazón del campo.",
        },
        "Chillán": {
            "imagen": "chillan.jpg",
            "descripcion": "Capital regional, comercio y cultura.",
        },
        "Chillán Viejo": {
            "imagen": "Chillan-Viejo.jpg",
            "descripcion": "Cuna de O'Higgins, historia patria.",
        },
        "El Carmen": {
            "imagen": "el carmen.jpg",
            "descripcion": "Cordillera de los Andes, naturaleza.",
        },
        "Pemuco": {
            "imagen": "pemuco.jpg",
            "descripcion": (
                "Valle profundo e identidad campesina en cada surco."
            ),
        },
        "Pinto": {
            "imagen": "pinto.jpg",
            "descripcion": (
                "Portón a la cordillera con las imponentes Termas y Nevados de"
                " Chillán."
            ),
        },
        "Quillón": {
            "imagen": "QUILLON.jpg",
            "descripcion": (
                "El 'Valle del Sol' con laguna Avendaño y saltos cristalinos."
            ),
        },
        "San Ignacio": {
            "imagen": "san ignacio.jpg",
            "descripcion": (
                "Campos y fe se entrelazan en sus tradiciones rurales."
            ),
        },
        "Yungay": {
            "imagen": "YUNGAY.jpeg",
            "descripcion": (
                "Puerta de entrada a la cordillera, hermosos trigales bajo"
                " cielos serranos."
            ),
        },
        "Coihueco": {
            "imagen": "coihueco.jpeg",
            "descripcion": (
                "Parques y embalses rodeados de bosque para escapadas"
                " naturales."
            ),
        },
        "Ñiquén": {
            "imagen": "ñiquen.jpg",
            "descripcion": (
                "Parques naturales y reserva de biodiversidad en ribera del"
                " Ñuble."
            ),
        },
        "San Carlos": {
            "imagen": "san carlos.jpg",
            "descripcion": (
                "Música folclórica y tradiciones, cuna de Violeta Parra."
            ),
        },
        "San Fabián de Alico": {
            "imagen": "san fabian.jpg",
            "descripcion": "Naturaleza y turismo aventura, tradición arriera.",
        },
        "San Nicolás": {
            "imagen": "san nicolas.jpg",
            "descripcion": "Agricultura y tradiciones patrimoniales del campo.",
        },
    }

    def go_to(route, from_route=None):
      if from_route:
         page.view_history.append(from_route)
      page.route = route
      route_change(None)

    def login_action(e):
        page.is_logged_in = True
        page.view_history.clear()
        go_to("/", from_route="/login")

    def logout_action(e):
        page.is_logged_in = False
        page.view_history.clear()
        go_to("/welcome", from_route="/")

    def seleccionar_comuna(comuna_nombre):
        page.comuna_seleccionada["nombre"] = comuna_nombre
        page.comuna_seleccionada["datos"] = comunas_data[comuna_nombre]
        go_to("/comuna", from_route="/")

    def welcome_view():
        return ft.View(
            route="/welcome",
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(
                                src="images/mapa.jpg",
                                width=600,
                                height=600,
                                fit="contain",
                            ),
                            ft.Text(
                                "¡Descubre Ñuble App!",
                                size=35,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color="green900",
                            ),
                            ft.Text(
                                (
                                    "Tu guía Virtual que te acompaña a descubrir"
                                    " el corazón cultural y natural de nuestra"
                                    " Región."
                                ),
                                text_align=ft.TextAlign.CENTER,
                                color="teal600",
                                italic=True,
                                size=18,
                            ),
                            ft.Button(
                                "Ingresar",
                                on_click=login_action,
                                style=ft.ButtonStyle(
                                    bgcolor="teal900",
                                    color="teal100",
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    shadow_color="grey600",
                                    elevation=5,
                                    text_style=ft.TextStyle(
                                        size=12, weight=ft.FontWeight.BOLD
                                    ),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=10,
                    border_radius=10,
                    bgcolor="teal100",
                    border=ft.Border.all(3, "teal100"),
                    width=600,
                    height=850,
                    alignment=ft.Alignment(0, 0),
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor="teal900",
        )

    def inicio_view():
        comuna_cards = []
        for nombre, datos in comunas_data.items():
            card = ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src=f"images/{datos['imagen']}",
                            width=300,
                            height=125,
                            fit="cover",
                        ),
                        ft.Text(
                            nombre,
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color="white",
                        ),
                        ft.Text(
                            datos["descripcion"],
                            size=10,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=3,
                            color="white",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=10,
                border_radius=8,
                bgcolor="black",
                border=ft.Border.all(1, "black"),
                on_click=lambda e, comuna=nombre: seleccionar_comuna(comuna),
                animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            )
            comuna_cards.append(card)

        grilla = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=200,
            child_aspect_ratio=0.8,
            spacing=10,
            run_spacing=10,
            controls=comuna_cards,
        )

        return ft.View(
            route="/",
            controls=[
                ft.AppBar(
                    leading=ft.IconButton(
                        icon=ft.Icons.MENU, tooltip="Menú (simulado)"
                    ),
                    title=ft.Text(
                        "Bienvenido a la Región de Ñuble",
                        size=25,
                        italic=True,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color="teal100",
                    ),
                    center_title=True,
                    bgcolor="teal900",
                    color="teal100",
                    actions=[
                        ft.Row([
                            ft.Text("Login", size=14, color="white"),
                            ft.IconButton(
                                icon=ft.Icons.PERSON,
                                tooltip="Perfil / Login",
                                on_click=lambda _: go_to("/login"),
                            ),
                        ]),
                    ],
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Explora las 21 comunas con sus paisajes, cultura y"
                            " tradición",
                            size=18,
                            italic=True,
                            text_align=ft.TextAlign.CENTER,
                            color="cyan100",
                            weight=ft.FontWeight.W_500,
                        ),
                        ft.Text(
                            "Elige una comuna para comenzar tu aventura.",
                            size=12,
                            italic=True,
                            text_align=ft.TextAlign.CENTER,
                            color="cyan100",
                        ),
                        ft.Divider(height=20),
                        grilla,
                    ]),
                    padding=10,
                    expand=True,
                    bgcolor="grey900",
                ),
                ft.BottomAppBar(
                    content=ft.Row(
                        [
                            ft.IconButton(
                                ft.Icons.HOME,
                                icon_color="cyan100",
                                tooltip="Inicio",
                                on_click=lambda _: go_to("/"),
                            ),
                            ft.IconButton(
                                ft.Icons.AUDIOTRACK,
                                icon_color="cyan100",
                                tooltip="Tus Audios",
                                on_click=lambda _: go_to("/audios"),
                            ),
                            ft.IconButton(
                                ft.Icons.FAVORITE,
                                icon_color="cyan100",
                                tooltip="Tus Favoritos",
                                on_click=lambda _: go_to("/favoritos"),
                            ),
                            ft.IconButton(
                                ft.Icons.DIRECTIONS_WALK, icon_color="cyan100"
                            ),
                            ft.IconButton(
                                ft.Icons.SETTINGS,
                                icon_color="cyan100",
                                tooltip="Configuración",
                                on_click=lambda _: go_to("/config"),
                            ),
                            ft.IconButton(
                                ft.Icons.EXIT_TO_APP,
                                icon_color="cyan100",
                                tooltip="Cerrar sesión",
                                on_click=logout_action,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    bgcolor="teal900",
                ),
            ],
            padding=0,
        )

    def vista_comuna_view():
        nombre = page.comuna_seleccionada["nombre"]
        datos = page.comuna_seleccionada["datos"]

        app_bar = ft.AppBar(
            title=ft.Text(
                "¡Descubre Ñuble App!",
                size=30,
                weight=ft.FontWeight.BOLD,
                color="teal50",
                text_align=ft.TextAlign.CENTER,
            ),
            center_title=True,
            bgcolor="teal900",
        )
        if nombre == "Cobquecura":
            content = ft.Column(
                [
                    ft.Text(
                        "Cobquecura",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="teal100",
                    ),
                    ft.Image(src="images/bote.jpg", width=400),
                    ft.Container(
                        content=ft.Column(
                            spacing=12,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Button(
                                    "🗺 Mapa",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/mapa_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "📸 Galería",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to("/lugar"),
                                ),
                                ft.Button(
                                    "🔉 Audios",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/audios_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "📖 Historia",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/historia_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "🛏 Hospedaje",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/hospedaje_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "🍽 Gastronomía",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/gastronomia_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "📍 Rutas exclusivas",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/rutas_exclusivas"
                                    ),
                                ),
                                ft.Button(
                                    "💬 Comentarios",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to(
                                        "/comentarios_cobquecura"
                                    ),
                                ),
                                ft.Button(
                                    "🎮 Juego",
                                    width=500,
                                    height=40,
                                    on_click=lambda _: go_to("/juego"),
                                ),
                            ],
                        ),
                        bgcolor="teal800",
                        padding=20,
                        border_radius=15,
                        margin=ft.Margin(0, 20, 0, 20),
                    ),
                ],
                alignment=ft.Alignment(0, 0),
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            content = ft.Column(
                [
                    ft.Image(src="images/mapa.jpg", width=100),
                    ft.Text(nombre, italic=True, size=30, color="teal50"),
                    ft.Text(
                        datos.get("descripcion", "Sin descripción"),
                        italic=True,
                        size=20,
                        color="teal100",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Image(
                        src=f"images/{datos.get('imagen', '')}", width=500
                    ),
                    ft.Text(
                        "...Otras funcionalidades próximamente disponibles...",
                        italic=True,
                        size=20,
                        color="teal100",
                    ),
                    ft.Image(src="images/app.jpg", width=180),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

        bottom_bar = ft.Container(
            bgcolor="teal900",
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        ft.Icons.HOME,
                        icon_color="cyan100",
                        on_click=lambda _: go_to("/"),
                    ),
                    ft.IconButton(
                        ft.Icons.AUDIOTRACK,
                        icon_color="cyan100",
                        tooltip="Tus Audios",
                        on_click=lambda _: go_to("/audios"),
                    ),
                    ft.IconButton(
                        ft.Icons.FAVORITE,
                        icon_color="cyan100",
                        on_click=lambda _: go_to("/favoritos"),
                    ),
                    ft.IconButton(
                        ft.Icons.VOLUME_UP,
                        icon_color="cyan100",
                        on_click=lambda _: go_to("/audios"),
                    ),
                    ft.IconButton(
                        ft.Icons.DIRECTIONS_WALK, icon_color="cyan100"
                    ),
                    ft.IconButton(
                        ft.Icons.SETTINGS,
                        icon_color="cyan100",
                        on_click=lambda _: go_to("/config"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            height=60,
            padding=10,
        )
        return ft.View(
            route="/comuna",
            bgcolor="teal900",
            controls=[
                app_bar,
                ft.Container(
                    content=content,
                    bgcolor="black",
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    padding=20,
                ),
                bottom_bar,
            ],
        )

    def detalle_lugar_view():
        fotos_cobquecura = [
            "images/cobquecura1.jpg",
            "images/cobquecura2.jpg",
            "images/cobquecura3.jpg",
            "images/cobquecura4.jpg",
            "images/cobquecura5.jpg",
            "images/cobquecura6.jpg",
        ]
        grid = ft.GridView(
            expand=True,
            max_extent=150,
            child_aspect_ratio=1,
            spacing=10,
            run_spacing=10,
            controls=[
                ft.Container(
                    content=ft.Image(src=img, fit="contain"),
                    bgcolor="teal900",
                    border_radius=10,
                    padding=5,
                )
                for img in fotos_cobquecura
            ],
        )
        return ft.View(
            route="/lugar",
            controls=[
                ft.AppBar(
                    title=ft.Text(
                        "Galerías de tus fotos de Cobquecura",
                        italic=True,
                        size=30,
                        color="teal100",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    leading=ft.IconButton(
                        ft.Icons.ARROW_BACK, on_click=lambda _: go_to("/comuna")
                    ),
                    bgcolor="teal900",
                ),
                ft.Container(
                    content=grid,
                    padding=20,
                    expand=True,
                    bgcolor="black",
                ),
            ],
        )

    def login_view():
        usuario_simulado = "TURISTA_1"
        correo_simulado = "turista1@nubleapp.cl"

        return ft.View(
            route="/login",
            bgcolor="teal900",
            controls=[
                ft.AppBar(
                    title=ft.Text("Inicio de sesión"),
                    center_title=True,
                    bgcolor="teal900",
                    color="teal100",
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(
                                ft.Icons.PERSON, size=150, color="teal50"
                            ),
                            ft.Text(
                                "LOGIN",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color="teal900",
                            ),
                            ft.TextField(
                                label="Usuario",
                                value=usuario_simulado,
                                disabled=True,
                                bgcolor="teal700",
                                border_color="cyan100",
                                color="white",
                            ),
                            ft.TextField(
                                label="Correo electrónico",
                                value=correo_simulado,
                                disabled=True,
                                bgcolor="teal700",
                                border_color="cyan100",
                                color="white",
                            ),
                            ft.TextButton(
                                "¿No tienes cuenta? Regístrate",
                                icon=ft.Icons.PERSON_ADD,
                                tooltip="Formulario simulado",
                                on_click=lambda e: print("Registro simulado"),
                            ),
                            ft.Text(
                                "Sesión iniciada correctamente",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="green200",
                            ),
                            ft.Text(
                                f"¡Bienvenido {usuario_simulado} a nuestra"
                                " App!",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color="teal900",
                            ),
                            ft.Text(
                                "👋 ¡A descubrir Ñuble!",
                                size=22,
                                text_align=ft.TextAlign.CENTER,
                                color="teal900",
                            ),
                            ft.Button(
                                "Iniciar sesión", on_click=lambda e: go_to("/")
                            ),
                            ft.Divider(height=30),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=30,
                    alignment=ft.Alignment(0, 0),
                    bgcolor="teal400",
                    border_radius=12,
                    border=ft.Border.all(2, "cyan400"),
                    shadow=ft.BoxShadow(
                        color="black54",
                        blur_radius=15,
                        offset=ft.Offset(0, 4),
                        spread_radius=3,
                    ),
                ),
            ],
        )

    def vista_estatica_view(titulo, imagen, ruta_volver="/comuna"):
        return ft.View(
            route=f"/{titulo.lower()}",
            bgcolor="teal900",
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.AppBar(
                    title=ft.Text(
                        titulo, weight=ft.FontWeight.BOLD, color="teal50"
                    ),
                    center_title=True,
                    bgcolor="teal900",
                    leading=ft.IconButton(
                        ft.Icons.ARROW_BACK,
                        on_click=lambda _: go_to(ruta_volver),
                    ),
                ),
                ft.Container(
                    expand=True,
                    bgcolor="black",
                    padding=0,
                    margin=0,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src=imagen, width=500, height=700, fit="cover"
                            ),
                            ft.Text(
                                f"{titulo} - sección en desarrollo",
                                size=15,
                                color="teal50",
                                weight=ft.FontWeight.W_500,
                            ),
                            ft.Image(src="images/app.jpg", width=160),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ),
                ft.Container(
                    bgcolor="teal900",
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.IconButton(
                                ft.Icons.HOME,
                                icon_color="teal100",
                                on_click=lambda _: go_to("/"),
                            ),
                            ft.IconButton(
                                ft.Icons.AUDIOTRACK,
                                icon_color="cyan100",
                                tooltip="Tus Audios",
                                on_click=lambda _: go_to("/audios"),
                            ),
                            ft.IconButton(
                                ft.Icons.FAVORITE,
                                icon_color="teal100",
                                on_click=lambda _: go_to("/favoritos"),
                            ),
                            ft.IconButton(
                                ft.Icons.VOLUME_UP,
                                icon_color="teal100",
                                on_click=lambda _: go_to("/audios"),
                            ),
                            ft.IconButton(
                                ft.Icons.DIRECTIONS_WALK,
                                icon_color="teal100",
                                on_click=lambda _: go_to("/rutas"),
                            ),
                            ft.IconButton(
                                ft.Icons.SETTINGS,
                                icon_color="teal100",
                                on_click=lambda _: go_to("/config"),
                            ),
                        ],
                    ),
                ),
            ],
        )

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            if page.is_logged_in:
                page.views.append(inicio_view())
            else:
                page.views.append(welcome_view())
        elif page.route == "/welcome":
            page.views.append(welcome_view())
        elif page.route == "/login":
            page.views.append(login_view())
        elif page.route == "/comuna":
            page.views.append(vista_comuna_view())
        elif page.route == "/lugar":
            page.views.append(detalle_lugar_view())
        elif page.route == "/favoritos":
            page.views.append(
                vista_estatica_view(
                    "Favoritos", "images/favoritos.jpeg", "/comuna"
                )
            )
        elif page.route == "/config":
            page.views.append(
                vista_estatica_view(
                    "Configuración", "images/configuracion.jpg", "/comuna"
                )
            )
        elif page.route == "/rutas":
            page.views.append(
                vista_estatica_view(
                    "Rutas Sugeridas", "images/RUTAS.jpeg", "/comuna"
                )
            )
        elif page.route == "/audios":
            page.views.append(
                vista_estatica_view(
                    "Lista de audios", "images/leyendas.jpeg", "/comuna"
                )
            )
        elif page.route == "/juego":
            page.views.append(
                vista_estatica_view(
                    "Juego Interactivo", "images/app.jpg", "/comuna"
                )
            )
        elif page.route == "/mapa_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Mapa de Cobquecura", "images/MapaCobque.png", "/comuna"
                )
            )
        elif page.route == "/audios_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Audios de Cobquecura",
                    "images/audios_cobquecura.jpg",
                    "/comuna",
                )
            )
        elif page.route == "/historia_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Historia de Cobquecura",
                    "images/historia_cobquecura.jpg",
                    "/comuna",
                )
            )
        elif page.route == "/hospedaje_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Hospedaje en Cobquecura",
                    "images/hospedaje_cobquecura.jpg",
                    "/comuna",
                )
            )
        elif page.route == "/gastronomia_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Gastronomía de Cobquecura",
                    "images/gastronomia_cobquecura.jpg",
                    "/comuna",
                )
            )
        elif page.route == "/rutas_exclusivas":
            page.views.append(
                vista_estatica_view(
                    "Rutas exclusivas", "images/rutas_exclusivas.jpg", "/comuna"
                )
            )
        elif page.route == "/comentarios_cobquecura":
            page.views.append(
                vista_estatica_view(
                    "Comentarios de usuarios",
                    "images/comentarios.jpg",
                    "/comuna",
                )
            )
        else:
            page.views.append(welcome_view())
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = (
        lambda e: page.view_history.pop() if page.view_history else "/"
    )

    # Inicialización limpia sin corrutina
    page.route = "/welcome"
    route_change(None)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")