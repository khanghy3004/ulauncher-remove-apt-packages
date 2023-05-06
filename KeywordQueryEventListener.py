from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
import RM
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):

        args = event.get_argument()
        length_list = extension.preferences["length-list"]
        packageNames = RM.list(args, length_list)
        items = []

        if args is not None:
            try:
                args = int(args)
            except ValueError:
                pass

            if isinstance(args, int) and args is not None:

                packageAfter = packageNames[args - 1 :]
                for package in packageAfter:

                    items.append(
                        ExtensionResultItem(
                            icon="images/remove.png",
                            name=package,
                            on_enter=ExtensionCustomAction(
                                {"action": "remove", "package": package},
                                keep_app_open=True,
                            ),
                        )
                    )

                return RenderResultListAction(items)

            else:
                for package in packageNames:
                    if (
                        package.lower().startswith(args.lower())
                        or args.lower() in package.lower()
                    ):
                        items.append(
                            ExtensionResultItem(
                                icon="images/remove.png",
                                name=package,
                                on_enter=ExtensionCustomAction(
                                    {"action": "remove", "package": package},
                                    keep_app_open=True,
                                ),
                            )
                        )

                return RenderResultListAction(items)

        return extension.render_main_page(None)
