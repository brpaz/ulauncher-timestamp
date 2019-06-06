import logging
import datetime
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class TimestampExtension(Extension):

    def __init__(self):
        logger.info('init Timestamp Extension')
        super(TimestampExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        timestampSec = int(event.get_argument())
        try:
            utcDt = datetime.datetime.utcfromtimestamp(timestampSec)
            localDt = datetime.datetime.fromtimestamp(timestampSec)

            formattedLocalDt = localDt.strftime('%Y-%m-%d %H:%M:%S')
            formattedUtcDt = utcDt.strftime('%Y-%m-%d %H:%M:%S')
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name="Local Time (ts in secs): " + formattedLocalDt,
                highlightable=False,
                on_enter=CopyToClipboardAction(formattedLocalDt)
            ))

            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name="UTC Time (ts in secs): " + formattedUtcDt,
                highlightable=False,
                on_enter=CopyToClipboardAction(formattedUtcDt)
            ))
        except ValueError:
            print("Value error: probably ts out of range because ts in milliseconds")

        # Add additional output in case timestamp is given in milliseconds
        timestampMillisec = int(event.get_argument())
        timestampSec = timestampMillisec / 1000
        utcDt = datetime.datetime.utcfromtimestamp(timestampSec)
        localDt = datetime.datetime.fromtimestamp(timestampSec)

        formattedLocalDt = localDt.strftime('%Y-%m-%d %H:%M:%S')
        formattedUtcDt = utcDt.strftime('%Y-%m-%d %H:%M:%S')
        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name="Local Time (ts in msecs): " + formattedLocalDt,
            highlightable=False,
            on_enter=CopyToClipboardAction(formattedLocalDt)
        ))

        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name="UTC Time (ts in msecs): " + formattedUtcDt,
            highlightable=False,
            on_enter=CopyToClipboardAction(formattedUtcDt)
        ))

        return RenderResultListAction(items)


if __name__ == '__main__':
   TimestampExtension().run()
