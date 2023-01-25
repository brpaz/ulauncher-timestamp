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

        eventValue = event.get_argument()
        description = "From seconds"
        if len(eventValue) > 11:
            eventValue = eventValue[0:10]
            description = "From submultiple of a second"

        utcDt = datetime.datetime.utcfromtimestamp(int(eventValue))
        localDt = datetime.datetime.fromtimestamp(int(eventValue))

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
