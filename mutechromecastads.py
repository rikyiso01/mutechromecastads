from time import sleep
from pychromecast import Chromecast
from pychromecast.controllers.media import MediaStatusListener, MediaStatus
from os import environ
from socket import gethostbyname
from sys import exit
from logging import INFO, basicConfig, getLogger
from signal import signal, SIGTERM

LOGGER = getLogger(__name__)
HOST_VARIABLE_NAME='CHROMECAST_HOST'

class Listener(MediaStatusListener):
    def __init__(self, chromecast: Chromecast):
        self.chromecast: Chromecast = chromecast
        self.muted: bool = False

    def new_media_status(self, status: MediaStatus) -> None:
        LOGGER.info(f"Currently playing {status.title}")
        ad = status.title == "Advertisement"
        if ad and not self.muted:
            self.chromecast.set_volume_muted(True)
            self.muted = True
        elif not ad and self.muted:
            self.muted = False
            self.chromecast.set_volume_muted(False)


def exit_handler(*_: object):
    raise KeyboardInterrupt()


def main():
    signal(SIGTERM, exit_handler)
    basicConfig(level=INFO)
    hostname = environ.get(HOST_VARIABLE_NAME)
    if hostname is None:
        LOGGER.error(f"Missing {HOST_VARIABLE_NAME} environment variable, exiting...")
        exit(1)
    ip = None
    while ip is None:
        LOGGER.info(f"Resolving {hostname}")
        try:
            ip = gethostbyname(hostname)
        except OSError as e:
            LOGGER.error("Error resolving hostname", exc_info=e)
            sleep(1)
    chromecast = Chromecast(ip)

    LOGGER.info("Starting service")
    chromecast.start()
    chromecast.wait()

    chromecast.media_controller.register_status_listener(Listener(chromecast))
    LOGGER.info("Service started, waiting for events")
    chromecast.join()
    LOGGER.error("pychromecast crashed, exiting...")
    exit(1)


if __name__ == "__main__":
    main()
