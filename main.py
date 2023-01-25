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

        if event.get_argument() is None:
            dt = datetime.datetime.now()
            ts = str(int(dt.timestamp()))
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name="Timestamp: " + ts,
                description=dt.strftime('%Y-%m-%d %H:%M:%S'),
                highlightable=False,
                on_enter=CopyToClipboardAction(ts)
            ))
            return RenderResultListAction(items)

        timestamp = int(event.get_argument())
        description = "From seconds"
        if timestamp > 99999999999:
            timestamp = timestamp/1000
            description = "From milliseconds"

        utcDt = datetime.datetime.utcfromtimestamp(timestamp)
        localDt = datetime.datetime.fromtimestamp(timestamp)

        formattedLocalDt = localDt.strftime('%Y-%m-%d %H:%M:%S')
        formattedUtcDt = utcDt.strftime('%Y-%m-%d %H:%M:%S')
        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name="Local Time: " + formattedLocalDt,
            description=description,
            highlightable=False,
            on_enter=CopyToClipboardAction(formattedLocalDt)
        ))

        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name="UTC Time: " + formattedUtcDt,
            description=description,
            highlightable=False,
            on_enter=CopyToClipboardAction(formattedUtcDt)
        ))

        return RenderResultListAction(items)

if __name__ == '__main__':
   TimestampExtension().run()
