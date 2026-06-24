import logging
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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

load_dotenv()
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

    def __init__(self, api_key: str):
        self.api_key = api_key

        self.youtube = build(
            "youtube",
            "v3",
            developerKey=self.api_key
        )

    # ---------------------------------------------
    # Obtener información básica del canal
    # ---------------------------------------------
    def get_channel_data(self, channel_id: str) -> dict:

        try:

            request = self.youtube.channels().list(
                part="snippet,statistics",
                id=channel_id
            )

            response = request.execute()

            if not response["items"]:
                raise ValueError(
                    f"No se encontró el canal {channel_id}"
                )

            return response["items"][0]

        except HttpError as e:
            logger.error(f"Error HTTP: {e}")
            raise

        except Exception as e:
            logger.exception(
                f"Error obteniendo datos del canal: {e}"
            )
            raise

    # ---------------------------------------------
    # Obtener IDs de videos
    # ---------------------------------------------
    def get_video_ids(self, channel_id: str) -> list[str]:

        video_ids = []

        try:

            request = self.youtube.search().list(
                part="id",
                channelId=channel_id,
                maxResults=50,
                type="video"
            )

            while request:

                response = request.execute()

                for item in response["items"]:
                    video_ids.append(
                        item["id"]["videoId"]
                    )

                request = self.youtube.search().list_next(
                    request,
                    response
                )

            return video_ids

        except Exception as e:
            logger.exception(
                f"Error obteniendo videos: {e}"
            )
            raise

    # ---------------------------------------------
    # Método principal
    # ---------------------------------------------
    def analyze_channel(
        self,
        channel_id: str
    ) -> ChannelStats:

        try:

            logger.info(
                f"Analizando canal: {channel_id}"
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
                )
            )

        except Exception as e:
            logger.exception(
                f"Error analizando canal: {e}"
            )
            raise


# =====================================================
# PRESENTACIÓN
# =====================================================

def show_results(stats: ChannelStats):

    print("\n" + "=" * 50)

    print(f"Canal: {stats.channel_name}")
    print(f"Suscriptores: {stats.subscribers:,}")
    print(f"Vistas Totales: {stats.total_views:,}")
    print(f"Videos Subidos: {stats.total_videos:,}")

    print("=" * 50)


# =====================================================
# MAIN
# =====================================================

def main():

    API_KEY = os.getenv("YOUTUBE_API_KEY")

    CHANNEL_ID = "UCwtL_041j3xAgo6G42oMr3w"

    try:

        analyzer = YouTubeChannelAnalyzer(
            API_KEY
        )

        stats = analyzer.analyze_channel(
            CHANNEL_ID
        )

        show_results(stats)

    except Exception as e:

        logger.critical(
            f"Fallo fatal: {e}"
        )


if __name__ == "__main__":
    main()