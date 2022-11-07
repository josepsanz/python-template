import logging

logger = logging.getLogger(__name__)


def run():
    logger.info('blablabla')

def main():
    logger.info('Hello world!')
    run()

    
if __name__ == '__main__':
    main()
