from datetime import datetime

class DataUtil:
    """Utilitário para formatação de datas"""
    
    @staticmethod
    def formatar_data(data_str):
        """Formata data para o padrão DD/MM/YYYY"""
        if not data_str:
            return ""
        
        try:
            if isinstance(data_str, str):
                # Tenta diferentes formatos
                for fmt in ['%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d']:
                    try:
                        data_obj = datetime.strptime(data_str[:19], fmt[:19])
                        return data_obj.strftime('%d/%m/%Y')
                    except:
                        continue
                return data_str
            elif isinstance(data_str, datetime):
                return data_str.strftime('%d/%m/%Y')
            else:
                return str(data_str)
        except:
            return str(data_str)
    
    @staticmethod
    def formatar_data_hora(data_str):
        """Formata data e hora para o padrão DD/MM/YYYY HH:MM"""
        if not data_str:
            return ""
        
        try:
            if isinstance(data_str, str):
                # Remove milissegundos se existirem
                data_sem_ms = data_str.split('.')[0] if '.' in data_str else data_str
                data_obj = datetime.strptime(data_sem_ms, '%Y-%m-%d %H:%M:%S')
                return data_obj.strftime('%d/%m/%Y %H:%M')
            elif isinstance(data_str, datetime):
                return data_str.strftime('%d/%m/%Y %H:%M')
            else:
                return str(data_str)
        except:
            return str(data_str)
