from pydantic import BaseModel
from src.models import UserDTO, RegisterDTO

class AuthService(BaseModel):
    @staticmethod
    def login(userDTO: UserDTO) -> str:
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
    
    @staticmethod
    def register(registerDTO: RegisterDTO) -> str:
        if len(registerDTO.username) != 0:
            output_str = "Nazwa Użytkownika: " + registerDTO.username + "\n"
            print ("nazwa Użytkownika: " + registerDTO.username + "\n")
        else:
            output_str = "Brak nazwy użytkownika\n"

        return output_str