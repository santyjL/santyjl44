import reflex as rx

from ..services.youtube_api import (
    youtube_client,
    ChannelStats,
    CHANNEL_ID,
)


class StateYoutube(rx.State):

    stats: ChannelStats | None = None

    error: str = ""

    loading: bool = False

    async def load_canal_youtube(self):

        self.loading = True
        self.error = ""

        try:

            self.stats = (
                youtube_client.analyze_channel(
                    CHANNEL_ID
                )
            )

        except Exception as e:

            self.error = str(e)

        finally:

            self.loading = False

    @rx.var
    def nombre_canal(self) -> str:

        if not self.stats:
            return ""

        return self.stats.channel_name

    @rx.var
    def subscribers(self) -> str:

        if not self.stats:
            return "0"

        return f"{self.stats.subscribers:,}"

    @rx.var
    def total_views(self) -> str:

        if not self.stats:
            return "0"

        return f"{self.stats.total_views:,}"

    @rx.var
    def total_videos(self) -> str:

        if not self.stats:
            return "0"

        return f"{self.stats.total_videos:,}"