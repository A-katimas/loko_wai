from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Union
import json
import csv


# ======================
# Protocol (duck typing)
# ======================

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# ======================
# Pipeline abstrait
# ======================

class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, file_path: str) -> Union[str, Any]:
        pass


# ======================
# Stages
# ======================

class InputStage:
    def process(self, data: Any) -> Any:
        print("InputStage: validation")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("TransformStage: transformation")

        if isinstance(data, list):
            return [x for x in data]

        if isinstance(data, dict):
            data["processed"] = True

        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("OutputStage: formatting")
        return data


# ======================
# Adapters
# ======================

class JSONAdapter(ProcessingPipeline):

    def process(self, file_path: str) -> Union[str, Any]:

        print(f"\nProcessing JSON file: {file_path}")

        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            result = self.run_stages(data)

            return f"JSON processed: {result}"

        except Exception as e:
            return f"JSON error: {e}"


class CSVAdapter(ProcessingPipeline):

    def process(self, file_path: str) -> Union[str, Any]:

        print(f"\nProcessing CSV file: {file_path}")

        try:
            rows = []

            with open(file_path, newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    rows.append(row)

            result = self.run_stages(rows)

            return f"CSV processed: {len(result)} rows"

        except Exception as e:
            return f"CSV error: {e}"


class StreamAdapter(ProcessingPipeline):

    def process(self, file_path: str) -> Union[str, Any]:

        print(f"\nProcessing Stream file: {file_path}")

        try:
            with open(file_path) as f:
                data = f.readlines()

            result = self.run_stages(data)

            return f"Stream processed: {len(result)} events"

        except Exception as e:
            return f"Stream error: {e}"


# ======================
# Nexus Manager
# ======================

class NexusManager:

    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def process_all(self, files: List[str]):

        for pipeline, file in zip(self.pipelines, files):
            result = pipeline.process(file)
            print(result)


# ======================
# MAIN
# ======================

def main():

    manager = NexusManager()

    json_pipeline = JSONAdapter("json_pipe")
    csv_pipeline = CSVAdapter("csv_pipe")
    stream_pipeline = StreamAdapter("stream_pipe")

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    manager.process_all([
        "data.json",
        "Perso-Passif.csv",
        "classified_data.txt"
    ])


if __name__ == "__main__":
    main()