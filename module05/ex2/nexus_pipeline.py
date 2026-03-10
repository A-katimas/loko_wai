from abc import ABC, abstractmethod
from typing import Protocol


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages = []

    @abstractmethod
    def add_stage(self, stage: "ProcessingStage") -> None:
        self.stages.append(stage)
        pass

    @abstractmethod
    def process(self, data: any) -> any:
        pass


class JSONAdpter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipline_id = pipeline_id

    def process(self, data: any) -> any:
        return data


class CVSAdpter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipline_id = pipeline_id

    def process(self, data: any) -> any:
        return data


class StreamAdpter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipline_id = pipeline_id

    def process(self, data: any) -> any:
        return data


class ProcessingStage(Protocol):
    def process(self, data: any) -> any:
        return data


class inputstage:
    def process(self, data: any) -> dict:
        chien = {data}
        return chien


class TrasformStage:
    def process(self, data: any) -> dict:
        chien = {data}
        return chien


class OutputStage:
    def process(self, data: any) -> dict:
        chien = str(data)
        return chien


def main():
    pass


if __name__ == "__main__":
    main()
