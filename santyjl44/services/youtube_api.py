import logging
import os
from dataclasses import dataclass

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UCwtL_041j3xAgo6G42oMr3w"


# =====================================================
# LOGGER
# =====================================================

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("YouTubeStats")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


logger = setup_logger()


# =====================================================
# MODELO
# =====================================================

@dataclass
class ChannelStats:
    channel_name: str
    subscribers: int
    total_views: int
    total_videos: int


# =====================================================
# CLIENTE YOUTUBE
# =====================================================

class YouTubeChannelAnalyzer:

    BASE_URL = (
        "https://www.googleapis.com/youtube/v3/channels"
    )

    def __init__(self, api_key: str):

        if not api_key:
            raise ValueError(
                "YOUTUBE_API_KEY no encontrada"
            )

        self.api_key = api_key

    def get_channel_data(
        self,
        channel_id: str
    ) -> dict:

        try:

            response = requests.get(
                self.BASE_URL,
                params={
                    "part": "snippet,statistics",
                    "id": channel_id,
                    "key": self.api_key,
                },
                timeout=10,
            )

            response.raise_for_status()

            data = response.json()

            if not data.get("items"):
                raise ValueError(
                    f"No se encontró el canal {channel_id}"
                )

            return data["items"][0]

        except requests.exceptions.Timeout:

            logger.exception(
                "Tiempo de espera agotado"
            )
            raise

        except requests.exceptions.ConnectionError:

            logger.exception(
                "Error de conexión"
            )
            raise

        except requests.exceptions.HTTPError as e:

            logger.exception(
                f"Error HTTP: {e}"
            )
            raise

        except Exception as e:

            logger.exception(
                f"Error obteniendo datos: {e}"
            )
            raise

    def analyze_channel(
        self,
        channel_id: str
    ) -> ChannelStats:

        try:

            logger.info(
                f"Analizando canal {channel_id}"
            )

            channel_data = self.get_channel_data(
                channel_id
            )

            stats = channel_data["statistics"]

            return ChannelStats(
                channel_name=channel_data["snippet"]["title"],
                subscribers=int(
                    stats.get("subscriberCount", 0)
                ),
                total_views=int(
                    stats.get("viewCount", 0)
                ),
                total_videos=int(
                    stats.get("videoCount", 0)
                ),
            )

        except Exception as e:

            logger.exception(
                f"Error analizando canal: {e}"
            )
            raise


# =====================================================
# INSTANCIA GLOBAL
# =====================================================

youtube_client = YouTubeChannelAnalyzer(
    API_KEY
)


# =====================================================
# MAIN TEST
# =====================================================

if __name__ == "__main__":

    stats = youtube_client.analyze_channel(
        CHANNEL_ID
    )

    print("\n" + "=" * 50)
    print(f"Canal: {stats.channel_name}")
    print(f"Subs: {stats.subscribers:,}")
    print(f"Views: {stats.total_views:,}")
    print(f"Videos: {stats.total_videos:,}")
    print("=" * 50)