import flet as ft
from flet import Text
import math


def main(page:ft.Page):
    # page.add(ft.Text(f'Ruta inicial: {page.route}'))
    page.window_width = 460
    page.window_height = 900
    page.window_resizable = False
    page.padding = 10
    page.title = 'App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # Componente Page1
    textoPage1 = [
        ft.Text('App', size=30, color='black', weight=ft.FontWeight.W_600, width=460, text_align='center'),
        ft.Text('Dimensionamientos de tuberias', size=20, color='black', weight=ft.FontWeight.W_200, width=460, text_align='center'),
        ft.Text('Creadores', size=15, color='black', weight=ft.FontWeight.W_800, width=460, text_align='center'),
        ft.Text('Dario Acosta', size=15, color='black', weight=ft.FontWeight.W_400, width=460, text_align='center'),
        ft.Text('Nallely tómala', size=15, color='black', weight=ft.FontWeight.W_400, width=460, text_align='center'),
        ft.Text('Alex loor', size=15, color='black', weight=ft.FontWeight.W_400, width=460, text_align='center'),
        ft.Text('Aldair Mendoza', size=15, color='black', weight=ft.FontWeight.W_400, width=460, text_align='center'),
        

    ]

    imagePage1 = [
        ft.Image(
            src='./img/upse-logo.png',
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=150,
            )
    ]

    com2Page1 =ft.Container(content=ft.Column(imagePage1),width=460, height=150, margin=ft.margin.only(top=20), border_radius=10, alignment=ft.alignment.center)
    comPage1 = ft.Container(content=ft.Column(textoPage1),width=460, height=300, margin=ft.margin.only(top=20), border_radius=10, alignment=ft.alignment.center)
    
    
    colPage1 = ft.Column(spacing=0, controls=[com2Page1, comPage1], alignment=ft.alignment.center)
   

    


    # Componentes Page2

    textoPage2 = [
        ft.Text('Calculadora', size=25, color='black', weight=ft.FontWeight.W_600, width=460, text_align='center'),
        ft.Text('Factor de fricción f por el método de iteración de un punto', size=15, color='black', weight=ft.FontWeight.W_100, width=460, text_align='center'),
        ft.Text(value='Manual de uso:', size=15, color='black', weight=ft.FontWeight.W_600, width=440, text_align='center'),
        ft.Text(value='Este apartado calcula el factor de fricción (f) para el flujo de fluidos en una tubería. Crucial en la determinación de las pérdidas de carga debidas a la fricción', size=15, color='black', weight=ft.FontWeight.W_100, width=400, text_align='center'),

        ft.Text(value='Variables de entrada', size=15, color='black', weight=ft.FontWeight.W_800, width=400, text_align='left'),
        ft.Text(value='E_D(texto): Representa la relación de rugosidad y diámetro de la tubería. **  Se debe escribir e/d incluyendo /   **', size=15, color='black', weight=ft.FontWeight.W_300, width=400, text_align='left'),
        ft.Text(value='Ejemplo: 20000/10000 indica que e = 20000 y d = 10000', size=15, color='black', weight=ft.FontWeight.W_600, width=400, text_align='left'),

        ft.Text(value='N_r (Numero):  Número de Reynolds (Nr) un parámetro adimensional que caracteriza el tipo de flujo en la tubería.', size=15, color='black', weight=ft.FontWeight.W_300, width=400, text_align='left'),
        ft.Text(value='Ejemplo: 4000', size=15, color='black', weight=ft.FontWeight.W_600, width=400, text_align='left'),
  

    ]


    # Calculos y muestreo Page2
    def factorFriccion(E_D, N_R):
        e_d = E_D.split('/')
        e = float(e_d[0])
        d = float(e_d[1])
        N_r = int(N_R)
        print(N_r)
        if N_r <= 2000:
            f = 64 / N_r
            print(f'La tubería con el valor {f} es lisa o rugosa')
            lisa_o_rugosa.value = f'El valor de N_r es menor a 2000, la tuberia es rugosa o lisa {f}'
        elif N_r < 4000:
            print(f'El número de Reynolds no es correcto, tu valor fue {N_r}')
            nr_no_permitido.value = f'Nr no permitido {N_r}'
        else:
            # Tuberia lisa (Método de Moody)
            f_moody = 0.25 / abs(math.log(1 / (3.7 * (d / e))) + 5.74 / N_r**0.9)**2

            # Tuberia rugosa (Ecuación de Colebrook-White)
            f_i = 64 / N_r
            i = 1
            while True:
                f_colebrook = 1 / (2 * math.log10((2 * e / d) + (18.7 / (N_r * math.sqrt(f_i)))))**2
                if abs(f_colebrook - f_i) < 1e-6:
                    break
                f_i = f_colebrook
                i += 1
                
            tp2.value =  f'El factor de friccion es: {f_i}'
            
            return f_i
    

    def mostrarFriccion(e):
        data = factorFriccion(E__D.value, N__R.value)
        page.update()

    tp2 = ft.Text(color='black')
    lisa_o_rugosa = ft.Text(color='black')
    nr_no_permitido = ft.Text(color='black')
    E__D = ft.TextField(label='Rugosidad-absoluta/Diamentro tuberia', color='black')
    N__R = ft.TextField(label='Numero de Reynolds', color='black')
    bpag1 = ft.ElevatedButton(text='Calcular', 
    on_click=mostrarFriccion)

    lista = [
        E__D, N__R, bpag1, tp2,lisa_o_rugosa,nr_no_permitido,
    ]
  
    
    comPage2 =ft.Container(content=ft.Column(textoPage2),width=400, height=380, margin=ft.margin.only(top=20), border_radius=10, alignment=ft.alignment.center)

    com2Page2 =ft.Container(content=ft.Column(lista),width=400, height=300, margin=ft.margin.only(top=20), border_radius=10, alignment=ft.alignment.center)

    colPage2 = ft.Column(spacing=0, controls=[comPage2, com2Page2], alignment=ft.alignment.center)

  
    

    # Componentes Page3
    textoPage3 = [
        ft.Text('Comprobación', size=25, color='black', weight=ft.FontWeight.W_600, width=460, text_align='center'),
        ft.Text('Diseño de tuberías simples.', size=15, color='black', weight=ft.FontWeight.W_100, width=460, text_align='center'),
    ]


    # Calculo y muestre Page3

    
    def tuberiaSimple(D, e, H, E, v, p, n, z_2, L):
        # Variables
        g = 9.81
        D = float(D)
        e = float(e)
        H = float(H)
        E = float(E)
        v = float(v)
        p = float(p)
        n = float(n)
        z_2 = float(z_2)
        L = float(L)
        A = math.pi * D**2 / 4

        # Comprobación de que la rugosidad relativa sea mayor que cero
        if n / D <= 0:
            print("La rugosidad relativa debe ser mayor que cero.")
            return

        # Suposición inicial
        h_L = H - z_2

        # Iteración
        i = 1
        while True:
            # Calcular v_i en la ecuación 3
            v_i = ((-2 * ((2*g*h_L)**0.5)) / (L**0.5)) * math.log(max(1e-6, (n / (3.7 * D)) + ((2.51 * v * (L**0.5)) / (D * ((2 * g * h_L)**0.5)))))

            # Comprobación de que la velocidad sea mayor que cero
            if v_i <= 0:
                print("La velocidad debe ser mayor que cero.")
                return

            # Calcular h_L(i+1) en la ecuación 9
            h_L_nuevo = H - z_2 - p * ((v_i**2) / (2 * g))

            # Imprimir Q
            Q = v_i * A
            print(f"Iteración {i}: Q = {Q}")
            caudal.value = f'El valor del caudal es {Q}'


            # Verificar condición de convergencia
            if abs(h_L_nuevo - h_L) <= E or i > 100:
                break

            # Actualizar h_L para la siguiente iteración
            h_L = h_L_nuevo
            i += 1

        print("Fin del programa.")



    def mostrarTuberia(e):
        data = tuberiaSimple(v_D.value, v_e.value, v_H.value, v_E.value, v_v.value, v_p.value, v_n.value, v_z2.value, v_L.value)
        page.update()

    caudal = ft.Text(color='black')
    v_D = ft.TextField(label='Diametro tuberia', color='black')
    v_e = ft.TextField(label='Rugosidad tuberia', color='black')
    v_H = ft.TextField(label='Energia', color='black')
    v_E = ft.TextField(label='Tolerancia', color='black')
    v_v = ft.TextField(label='Velocidad inicial', color='black')
    v_p = ft.TextField(label='Perdida de carga localizada', color='black')
    v_n = ft.TextField(label='Rugosidad relativa de la tubería', color='black')
    v_z2 = ft.TextField(label='Energía en la salida de la tubería', color='black')
    v_L = ft.TextField(label='Longitud de la tubería.', color='black')
    bpag3 = ft.ElevatedButton(text='Calcular', 
    on_click=mostrarTuberia)


    lista_page3 = [
        v_D, v_e, v_H, v_E, v_v, v_p,v_n, v_z2, v_L, bpag3, caudal,
    ]
   




    comPage3 =ft.Container(content=ft.Column(textoPage3),width=400, height=80, margin=ft.margin.only(top=5), border_radius=10, alignment=ft.alignment.center)

    com2Page3 =ft.Container(content=ft.Column(lista_page3),width=400, height=800, margin=ft.margin.only(top=0), border_radius=10, alignment=ft.alignment.center)

    colPage3 = ft.Column(spacing=0, controls=[comPage3, com2Page3], alignment=ft.alignment.center)

    # Funcion Cambiar Paginas
    def cambiarPagina(e):
        indice = e.control.selected_index
        page1.visible = True if indice == 0 else False
        page2.visible = True if indice == 1 else False
        page3.visible = True if indice == 2 else False
        page.update()

    # Paginas
    page1 = ft.Container(
        colPage1,
        width=460,
        height=800,
        bgcolor='#F2ECFF',
        alignment=ft.alignment.center
        
    )
    page2 = ft.Container(
        colPage2,
        width=460,
        height=800,
        bgcolor='#F2ECFF',
        alignment=ft.alignment.center
        
    )
    page3 = ft.Container(
        colPage3,
        width=460,
        height=800,
        bgcolor='#F2ECFF',
        alignment=ft.alignment.center
        
    )   
    

    # Componente Navegacion
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=cambiarPagina,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationDestination(icon=ft.icons.CONFIRMATION_NUMBER, label="Fricción"),
            ft.NavigationDestination(icon=ft.icons.LOCAL_DRINK, label="Tuberia"),
        ], 
        
    )
    
    page.add(ft.Container(content=ft.Column([page1,
                                             page2, 
                                             page3])))
    

ft.app(target=main)
