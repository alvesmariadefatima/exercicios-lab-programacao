from click import password_option


login_user = input("Usuário: ")
password = input("Senha: ")

while login_user == password:
    print("Sua senha deve ser diferente do login: ")
    password = input("Senha: ")

print("Você está autenticado(a)!!!")