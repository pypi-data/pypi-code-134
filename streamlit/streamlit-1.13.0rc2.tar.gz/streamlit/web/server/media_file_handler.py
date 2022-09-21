# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional
from urllib.parse import quote, unquote_plus

import tornado.web

from streamlit.logger import get_logger
from streamlit.runtime.media_file_manager import (
    media_file_manager,
    MediaFileType,
)
from streamlit.string_util import generate_download_filename_from_title
from streamlit.web.server import allow_cross_origin_requests

LOGGER = get_logger(__name__)


class MediaFileHandler(tornado.web.StaticFileHandler):
    def set_default_headers(self) -> None:
        if allow_cross_origin_requests():
            self.set_header("Access-Control-Allow-Origin", "*")

    def set_extra_headers(self, path: str) -> None:
        """Add Content-Disposition header for downloadable files.

        Set header value to "attachment" indicating that file should be saved
        locally instead of displaying inline in browser.

        We also set filename to specify the filename for downloaded files.
        Used for serving downloadable files, like files stored via the
        `st.download_button` widget.
        """
        media_file = media_file_manager.get(path)

        if media_file and media_file.file_type == MediaFileType.DOWNLOADABLE:
            filename = media_file.file_name

            if not filename:
                title = self.get_argument("title", "", True)
                title = unquote_plus(title)
                filename = generate_download_filename_from_title(title)
                filename = f"{filename}{media_file.extension}"

            try:
                file_expr = 'filename="{}"'.format(filename)
            except UnicodeEncodeError:
                file_expr = "filename*=utf-8''{}".format(quote(filename))

            self.set_header("Content-Disposition", f"attachment; {file_expr}")

    # Overriding StaticFileHandler to use the MediaFileManager
    #
    # From the Tornado docs:
    # To replace all interaction with the filesystem (e.g. to serve
    # static content from a database), override `get_content`,
    # `get_content_size`, `get_modified_time`, `get_absolute_path`, and
    # `validate_absolute_path`.
    def validate_absolute_path(self, root: str, absolute_path: str) -> str:
        try:
            media_file_manager.get(absolute_path)
        except KeyError:
            LOGGER.error("MediaFileHandler: Missing file %s", absolute_path)
            raise tornado.web.HTTPError(404, "not found")

        return absolute_path

    def get_content_size(self) -> int:
        abspath = self.absolute_path
        if abspath is None:
            return 0

        media_file = media_file_manager.get(abspath)
        return media_file.content_size

    def get_modified_time(self) -> None:
        # We do not track last modified time, but this can be improved to
        # allow caching among files in the MediaFileManager
        return None

    @classmethod
    def get_absolute_path(cls, root: str, path: str) -> str:
        # All files are stored in memory, so the absolute path is just the
        # path itself. In the MediaFileHandler, it's just the filename
        return path

    @classmethod
    def get_content(
        cls, abspath: str, start: Optional[int] = None, end: Optional[int] = None
    ):
        LOGGER.debug("MediaFileHandler: GET %s", abspath)

        try:
            # abspath is the hash as used `get_absolute_path`
            media_file = media_file_manager.get(abspath)
        except:
            LOGGER.error("MediaFileHandler: Missing file %s", abspath)
            return

        LOGGER.debug(
            "MediaFileHandler: Sending %s file %s", media_file.mimetype, abspath
        )

        # If there is no start and end, just return the full content
        if start is None and end is None:
            return media_file.content

        if start is None:
            start = 0
        if end is None:
            end = len(media_file.content)

        # content is bytes that work just by slicing supplied by start and end
        return media_file.content[start:end]
