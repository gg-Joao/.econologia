import re

class ValidacaoUtil:
    """Utilitário para validações de formato e limites de caracteres"""
  
    PADROES = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'telefone_br': r'^\d{10,11}$',
        'cnpj': r'^\d{14}$',
        'nome': r'^[a-zA-ZÀ-ÿ\s]+$',
        'razao_social': r'^[a-zA-Z0-9À-ÿ\s\.,&-]+$',
        'endereco': r'^[a-zA-Z0-9À-ÿ\s\.,#-]+$',
        'senha': r'^[a-zA-Z0-9!@#$%^&*()_+=\-\[\]{};:\'",.<>?/`~|\\]+$'
    }
    

    LIMITES = {
        'nome': {'min': 3, 'max': 50},
        'email': {'min': 5, 'max': 100},
        'telefone': {'min': 10, 'max': 11},
        'senha': {'min': 6, 'max': 20},
        'cnpj': {'min': 14, 'max': 14},
        'razao_social': {'min': 3, 'max': 100},
        'endereco': {'min': 5, 'max': 200},
        'fone_cooperativa': {'min': 10, 'max': 11}
    }
    
    @staticmethod
    def validar_nome(nome):
        """
        Valida nome (apenas letras e espaços)
        Retorna: (válido: bool, mensagem: str)
        """
        nome = nome.strip()
        limites = ValidacaoUtil.LIMITES['nome']
        
        if not nome:
            return False, "Nome não pode estar vazio"
        
        if len(nome) < limites['min']:
            return False, f"Nome deve ter no mínimo {limites['min']} caracteres"
        
        if len(nome) > limites['max']:
            return False, f"Nome não pode exceder {limites['max']} caracteres (atual: {len(nome)})"
        
        if not re.match(ValidacaoUtil.PADROES['nome'], nome):
            return False, "Nome deve conter apenas letras e espaços"
        
        return True, "OK"
    
    @staticmethod
    def validar_email(email):
        """
        Valida formato de email
        Retorna: (válido: bool, mensagem: str)
        """
        email = email.strip()
        limites = ValidacaoUtil.LIMITES['email']
        
        if not email:
            return False, "Email não pode estar vazio"
        
        if len(email) > limites['max']:
            return False, f"Email não pode exceder {limites['max']} caracteres (atual: {len(email)})"
        
        if not re.match(ValidacaoUtil.PADROES['email'], email):
            return False, "Email inválido (formato: usuario@dominio.com)"
        
        return True, "OK"
    
    @staticmethod
    def validar_telefone(telefone):
        """
        Valida telefone brasileiro (10 ou 11 dígitos)
        Retorna: (válido: bool, mensagem: str)
        """
        telefone_limpo = re.sub(r'[^\d]', '', telefone)
        limites = ValidacaoUtil.LIMITES['telefone']
        
        if not telefone_limpo:
            return False, "Telefone não pode estar vazio"
        
        if len(telefone_limpo) < limites['min']:
            return False, f"Telefone deve ter no mínimo {limites['min']} dígitos (atual: {len(telefone_limpo)})"
        
        if len(telefone_limpo) > limites['max']:
            return False, f"Telefone não pode exceder {limites['max']} dígitos (atual: {len(telefone_limpo)})"
        
        if not re.match(ValidacaoUtil.PADROES['telefone_br'], telefone_limpo):
            return False, "Telefone deve conter apenas números (10 ou 11 dígitos)"
        
        return True, "OK"
    
    @staticmethod
    def validar_cnpj(cnpj):
        """
        Valida CNPJ (14 dígitos)
        Retorna: (válido: bool, mensagem: str)
        """
        cnpj_limpo = re.sub(r'[^\d]', '', cnpj)
        limites = ValidacaoUtil.LIMITES['cnpj']
        
        if not cnpj_limpo:
            return False, "CNPJ não pode estar vazio"
        
        if len(cnpj_limpo) != limites['max']:
            return False, f"CNPJ deve ter exatamente {limites['max']} dígitos (atual: {len(cnpj_limpo)})"
        
        if not re.match(ValidacaoUtil.PADROES['cnpj'], cnpj_limpo):
            return False, "CNPJ deve conter apenas números"
        
        return True, "OK"
    
    @staticmethod
    def validar_senha(senha):
        """
        Valida senha (comprimento mínimo e máximo)
        Retorna: (válido: bool, mensagem: str)
        """
        limites = ValidacaoUtil.LIMITES['senha']
        
        if not senha:
            return False, "Senha não pode estar vazia"
        
        if len(senha) < limites['min']:
            return False, f"Senha deve ter no mínimo {limites['min']} caracteres"
        
        if len(senha) > limites['max']:
            return False, f"Senha não pode exceder {limites['max']} caracteres (atual: {len(senha)})"
        
        return True, "OK"
    
    @staticmethod
    def validar_razao_social(razao):
        """
        Valida razão social (letras, números e espaços)
        Retorna: (válido: bool, mensagem: str)
        """
        razao = razao.strip()
        limites = ValidacaoUtil.LIMITES['razao_social']
        
        if not razao:
            return False, "Razão Social não pode estar vazia"
        
        if len(razao) < limites['min']:
            return False, f"Razão Social deve ter no mínimo {limites['min']} caracteres"
        
        if len(razao) > limites['max']:
            return False, f"Razão Social não pode exceder {limites['max']} caracteres (atual: {len(razao)})"
        
        if not re.match(ValidacaoUtil.PADROES['razao_social'], razao):
            return False, "Razão Social contém caracteres inválidos"
        
        return True, "OK"
    
    @staticmethod
    def validar_endereco(endereco):
        """
        Valida endereço
        Retorna: (válido: bool, mensagem: str)
        """
        endereco = endereco.strip()
        limites = ValidacaoUtil.LIMITES['endereco']
        
        if not endereco:
            return False, "Endereço não pode estar vazio"
        
        if len(endereco) < limites['min']:
            return False, f"Endereço deve ter no mínimo {limites['min']} caracteres"
        
        if len(endereco) > limites['max']:
            return False, f"Endereço não pode exceder {limites['max']} caracteres (atual: {len(endereco)})"
        
        if not re.match(ValidacaoUtil.PADROES['endereco'], endereco):
            return False, "Endereço contém caracteres inválidos"
        
        return True, "OK"
    
    @staticmethod
    def formatar_telefone(telefone):
        """Formata telefone brasileiro para exibição"""
        telefone_limpo = re.sub(r'[^\d]', '', telefone)
        
        if len(telefone_limpo) == 11:
            return f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"
        elif len(telefone_limpo) == 10:
            return f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
        
        return telefone
    
    @staticmethod
    def formatar_cnpj(cnpj):
        """Formata CNPJ para exibição"""
        cnpj_limpo = re.sub(r'[^\d]', '', cnpj)
        
        if len(cnpj_limpo) == 14:
            return f"{cnpj_limpo[:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:]}"
        
        return cnpj
