# ToDo: logging refactor 📝
import logging

logger = logging.getLogger('PokemonGameinfo')
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger.setLevel(logging.DEBUG)
