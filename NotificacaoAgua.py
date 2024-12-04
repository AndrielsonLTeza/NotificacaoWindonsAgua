import time
from plyer import notification

def notificar():
    try:
        notification.notify(
            title="Notificação: Hora de Beber Água!",
            message="Beba um copo de água para se manter hidratado.",
            app_icon="C:\\Windows\\System32\\CopodeAgua.ico",  # Certifique-se de usar o caminho correto
            timeout=5  # segundos
        )
        print("Notificação enviada com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar notificação: {e}")

# Intervalo de tempo entre notificações (em segundos)
intervalo = 60 * 60  # 1 hora

print("Programa de notificação iniciado. Notificações aparecerão a cada 1 hora.")

while True:
    try:
        notificar()
        time.sleep(intervalo)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break

# Manter a janela do prompt de comando aberta
input("Pressione Enter para fechar o programa.")
