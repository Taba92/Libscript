import json

# Classe manager delle configurazioni. Per ora supporta solo file json
class ConfigurationManager():
    config = {}

    def __init__(self, config_file_name, file_type = "json"):
        with open(config_file_name, 'r') as f:
            if(file_type == "json"):
                self.config = json.load(f)
            else:
                raise Exception(f"Estensione file config {file_type} non supportata")

    # Ritorna il dizionario delle configurazioni    
    def GetConfigs(self):
        return self.config
    
    # Ritorna una configurazione dato una chiave di configurazione
    def GetConfigValue(self, nomeVoceConfigurazione):
        if(nomeVoceConfigurazione in self.config.keys()):
            return self.config[nomeVoceConfigurazione]
        else:
            raise Exception(f"Chiave configurazione {nomeVoceConfigurazione} non presente")