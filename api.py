from twilio.rest import Client

account_sid = 'AC27aeb99a862caa2ee504d65a039b4e15'
auth_token = '2628e3b2b09991c904b9af0060bd9352'

client = Client(account_sid, auth_token)


def enviar_mensagem(conteudo):

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=conteudo,
        to='whatsapp:+557991790119'
    )
    return message

