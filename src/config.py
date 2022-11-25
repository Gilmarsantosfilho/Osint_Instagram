import configparser
import sys

from src import printcolors as pc

try:
    config = configparser.ConfigParser(interpolation=None)
    config.read("config/credentials.ini")
except FileNotFoundError:
    pc.printout('Error: file "config/credentials.ini" não encontrado!\n', pc.RED)
    sys.exit(0)
except Exception as e:
    pc.printout("Error: {}\n".format(e), pc.RED)
    sys.exit(0)

def getUsername():
    try:

        username = config["Credentials"]["username"]

        if username == '':
            pc.printout('Erro: o campo "username" não pode ficar em branco em "config/credentials.ini"\n', pc.RED)
            sys.exit(0)

        return username
    except KeyError:
        pc.printout('Erro: campo "nome de usuário" ausente em "config/credentials.ini"\n', pc.RED)
        sys.exit(0)

def getPassword():
    try:

        password = config["Credentials"]["password"]

        if password == '':
            pc.printout('Erro: o campo "senha" não pode ficar em branco em "config/credentials.ini"\n', pc.RED)
            sys.exit(0)

        return password
    except KeyError:
        pc.printout('Erro: campo "senha" ausente em "config/credentials.ini"\n', pc.RED)
        sys.exit(0)
