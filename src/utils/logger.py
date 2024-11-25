# src/utils/logger.py
import logging

logging.basicConfig(level=logging.DEBUG, filename='game.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('BippyGame')