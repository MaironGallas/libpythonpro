from libpythonpro.spam.enviador_de_email import Enviador


def test_criador_de_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('mairongallas@gmail.com',
                    'luciano@python.pro.br',
                    'Curso Python Pro',
                    'Primeira Turma Guido Von Rossum Aberta')

    assert 'mairongallas@gmail.com' in resultado
