from pydantic import BaseModel
from src.models import UserDTO

class AuthService(BaseModel):
    @staticmethod
    def login(userDTO: UserDTO):
        if len(userDTO.username) != 0:
            output_str = "Nazwa Użytkownika: " + userDTO.username + "\n"
            print("Nazwa Użytkownika: " + userDTO.username + "\n")
        else:
            output_str = "Brak nazwy użytkownika\n"
            print("Brak nazwy użytkownika\n")

        if len(userDTO.password) != 0:
            output_str += "Hasło Użytkownika: " + userDTO.password
            print("Hasło Użytkownika: " + userDTO.password)
        else:
            output_str += "Brak hasła użytkownika"
            print("Brak hasła użytkownika")

        return output_str