import pywhatkit as kit
import time

# Lista de números de telefone e a mensagem
numeros_telefone = [
    "+5516994182750",
    "+5516992624128",
    "+5516991499760",
    "+5516992890025",
    "+5516991493543"
]
mensagem = "Teste 9 de automação do whatsapp!"

for i, numero in enumerate(numeros_telefone):
    try:
        # Envia a mensagem instantaneamente
        kit.sendwhatmsg_instantly(numero, mensagem)
        print(f"Mensagem enviada para {numero}")

        # Espera 60 segundos antes de enviar para o próximo número
        if i < len(numeros_telefone) - 1:
            print("Esperando 60 segundos antes de enviar a próxima mensagem...")
            time.sleep(60)
    except Exception as e:
        print(f"Falha ao enviar mensagem para {numero}. Erro: {e}")
