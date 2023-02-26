import logging
from logging.handlers import RotatingFileHandler
import json

# Classe manager dei logger
class LogManager():
    logger = None

    # Se al costruttore gli viene passato un solo argomento assume che sia il nome di un file e usa il logger di default
    # altrimenti assume che sia un nome di file di configurazione logger con la relativa estensione
    # Per ora è supportata solo l'estensione json
    def __init__(self, *args):
        #1) Se ha un solo argomento allora uso il logger di default sul nome del file
        if(len(args) == 1):
            log_handler = RotatingFileHandler(
                            filename = args[0],
                            mode = 'a',
                            maxBytes = 104858,
                            backupCount = 1,
                            delay = 0
                    )
            logging.basicConfig(
                            level=logging.DEBUG, 
                            format='Log %(asctime)s: %(levelname)s %(message)s\n',
                            datefmt = '%d/%m/%Y %I:%M', 
                            handlers = [log_handler]
                            )
        #2) Assume che gli sia stato passato un nome di file di configurazione con la relativa estensione
        elif (len(args) == 2):
            config_file_path = args[0]
            estensione_file_config = args[1]
            logger_config = None
            #2.1) Processo il file di configurazione per il logger
            with open(config_file_path, 'r') as f:
                if (estensione_file_config == "json"):
                    logger_config = json.load(f)
                else:
                    raise Exception(f"Estensione file configurazione logger {estensione_file_config} non supportata")
            logging.config.dictConfig(logger_config)
        #3) In qualsiasi altro caso vado in errore
        else:
            raise Exception(f"Parametri costruttore non validi: {args}")
        self.logger = logging.getLogger()

    # Ritorna il logger gestito dal manager
    def GetLogger(self):
        return self.logger