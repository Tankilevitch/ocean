from typing import Any

from gitlab.v4.objects import Project

from gitlab_integration.events.hooks.base import HookHandler
from gitlab_integration.utils import ObjectKind
from port_ocean.context.ocean import ocean


class Pipelines(HookHandler):
    events = ["Pipeline Hook"]
    system_events = ["pipeline"]

    async def _on_hook(self, body: dict[str, Any], gitlab_project: Project) -> None:
        pipeline = gitlab_project.pipelines.get(body["object_attributes"]["id"])
        await ocean.register_raw(ObjectKind.PIPELINE, [pipeline.asdict()])
