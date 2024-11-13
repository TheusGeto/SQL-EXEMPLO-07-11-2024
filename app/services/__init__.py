from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository: 
    def init (self, session: Session): 
        self.session = session
    def salvar_usuario(self, usuario: Usuario): self.session.add(usuario) self.session.commit()