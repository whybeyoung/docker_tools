from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from artifacts_docker_tool import DockerImageListTool


class IflytekArtifactoryToolkit(BaseToolkit, ABC):
    name: str = "Iflytek Artifactory Toolkit"
    description: str = "Iflytek Artifactory  kit contains all tools related to Iflytek Artifactory"

    def get_tools(self) -> List[BaseTool]:
        return [DockerImageListTool()]

    def get_env_keys(self) -> List[str]:
        return ["ArtifactoryUrl", "DockerUsername", "DockerPassword"]
