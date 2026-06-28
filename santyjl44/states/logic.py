import reflex as rx
import asyncio
from ..services.youtube_api import (
    youtube_client,
    ChannelStats,
    CHANNEL_ID,
)

class HeroState(rx.State):

    words = [
        "PROGRAMO",
        "PROGRESO",
        "PROACTIVO",
        "PROSPERO",
    ]

    current_word_index: int = 0
    current_text: str = ""

    deleting: bool = False

    @rx.event(background=True)
    async def start_typewriter(self):

        while True:

            word = self.words[self.current_word_index]

            # ESCRIBIR
            while len(self.current_text) < len(word):

                async with self:
                    self.current_text = word[: len(self.current_text) + 1]

                await asyncio.sleep(0.30)

            # ESPERAR
            await asyncio.sleep(1.4)

            # BORRAR
            while len(self.current_text) > 0:

                async with self:
                    self.current_text = self.current_text[:-1]

                await asyncio.sleep(0.14)

            # SIGUIENTE PALABRA
            async with self:
                self.current_word_index = (
                    self.current_word_index + 1
                ) % len(self.words)

            await asyncio.sleep(0.2)

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