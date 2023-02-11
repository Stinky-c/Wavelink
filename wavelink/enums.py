"""MIT License

Copyright (c) 2019-2021 PythonistaGuild

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from enum import Enum
else:
    from disnake import Enum

__all__ = ("ErrorSeverity", "LoadType", "Event")


class ErrorSeverity(Enum):
    common = "COMMON"
    suspicious = "SUSPICIOUS"
    fault = "FAULT"


class LoadType(Enum):
    track_loaded = "TRACK_LOADED"
    playlist_loaded = "PLAYLIST_LOADED"
    search_result = "SEARCH_RESULT"
    no_matches = "NO_MATCHES"
    load_failed = "LOAD_FAILED"


class Event(Enum):
    """
    Represents all the events of the library.
    Must pass as string, listeners do not account for different enums

    These offer to register listeners/events in a more pythonic way; additionally autocompletion and documentation are both supported.

    Inspired by disnake 2.8.0

    """

    node_ready = "wavelink_node_ready"
    """Called when the Node you are connecting to has initialised and successfully connected to Lavalink."""

    websocket_closed = "wavelink_websocket_closed"
    """Called when the Node websocket has been closed by Lavalink."""

    track_start = "wavelink_track_start"
    """Called when a track starts playing."""

    track_end = "wavelink_track_end"
    """Called when the current track has finished playing."""

    track_exception = "wavelink_track_exception"
    """Called when a TrackException occurs in Lavalink."""

    track_stuck = "wavelink_track_stuck"
    """Called when a TrackStuck occurs in Lavalink."""
