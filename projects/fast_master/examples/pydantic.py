# Conversões automáticas
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

u = User(name="Felipe", age="30", email="f@pycode.com")
print(u.age)   # 30 (foi convertido de str para int)



# Validação automática
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

User(email="email_invalido") # Levanta ValidationError



# Defaults e opcionais
class Produto(BaseModel):
    nome: str
    preco: float = 0.0
    descricao: str | None = None
