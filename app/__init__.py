#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect
from flask_babel import Babel
#criando o aplicativo
app = Flask(__name__)
#puxando o arquivo config.py
app.config.from_object('config')
#criando um objeto db da classe SQLAlchemy
db = SQLAlchemy(app)
#criar uma variável migrate e passar a instância da aplicação e do db
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
csrf.init_app(app)

babel = Babel(app)

#determinar o que vai ter no projeto
#FIXME:model


#NOTE: Alpha InfoSystems
#FIXME:model
from .models.alpha import nivel_model
from .models.alpha import tecnico_model
from .models.alpha import cliente_model
from .models.alpha import peca_model
from .models.alpha import sevico_model
from .models.alpha import marca_model
from .models.alpha import equipamento_model
from .models.alpha import orcamento_model
from .models.alpha import itempeca_tem



#FIXME:view
from .views import nivel_view
from .views import tecnico_view
from .views import equipamento_view














