import time
import random
from playwright.sync_api import sync_playwright

def simulate_traffic():
    with sync_playwright() as p:
        for i in range(30):  # Ejecutar 30 veces
            print(f"Ejecutando simulación {i + 1}/30...")

            browser = p.firefox.launch(headless=True)  
            context = browser.new_context()
            page = context.new_page()
            
            # Navegar al sitio
            page.goto("https://teseodata.com/aphrodite/media/index.html")
            print("Página cargada.")

            # Permanencia en la página (15-30 segundos)
            stay_time = random.randint(15, 30)
            print(f"Permaneciendo en la página por {stay_time} segundos...")
            time.sleep(stay_time)

            # Simular interacción si hay enlaces
            links = page.locator("a").all()
            if links:
                print("Haciendo clic en el primer enlace encontrado...")
                links[0].click()
                
                # Permanencia en la página después del clic (10-20 segundos)
                post_click_time = random.randint(10, 20)
                print(f"Permaneciendo en la página después del clic por {post_click_time} segundos...")
                time.sleep(post_click_time)
            else:
                print("No se encontraron enlaces.")

            # Cerrar navegador
            browser.close()
            print("Simulación completada.\n")

            # Espera aleatoria entre ejecuciones (5-10 segundos)
            delay_between_executions = random.randint(5, 10)
            print(f"Esperando {delay_between_executions} segundos antes de la siguiente ejecución...\n")
            time.sleep(delay_between_executions)

simulate_traffic()
