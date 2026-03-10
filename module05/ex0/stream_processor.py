from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(data: any) -> str:
        pass

    @abstractmethod
    def validate(data: any) -> bool:
        pass

    @abstractmethod
    def format_output(result: str) -> str:
        pass


class NumericProcessor(DataProcessor):

    def process(self, data: any) -> str:
        som = sum(data)
        moy = sum(data) / len(data)
        return (
            "Output: "
            f"numeric values sum = {som}\n"
            f"avg = {moy}\n"
            f"Processed : {len(data)}"
        )

    def validate(self, data: any) -> bool:
        if not (isinstance(data, list)):
            return False
        print("Validation: Numeric data verified")
        return all(isinstance(x, (int, float)) for x in data)

    def format_output(result: str) -> str:
        pass


class TextProcessor(DataProcessor):

    def process(self, data: any) -> str:
        return f"il y a {len(data)} char"

    def validate(self, data: any) -> bool:
        print("Validation: Text data verified")
        return isinstance(data, str)

    def format_output(result: str) -> str:
        pass


class LogProcessor(DataProcessor):

    def process(self, data: any) -> str:
        message, alert = data.split(":", 1)
        message = message.strip()
        alert = alert.strip()
        return f"[{message}] {message} level detected: {alert}"

    def validate(self, data: any) -> bool:
        print("Validation: Log entry verified")
        return isinstance(data, str) and ":" in data

    def format_output(result: str) -> str:
        pass


def useobj(pros: DataProcessor, data: any) -> None:
    print(f"Initializing {pros.__class__.__name__} ...")
    if pros.validate(data):

        print(f'Processing data: "{data}" ')
        print(f"output: {pros.process(data)}\n")
    else:
        print("mange")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("")
    processors = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus"),
        (LogProcessor(), "ERROR: Connection timeout"),
    ]

    for proc, data in processors:
        useobj(proc, data)

    print("=== Polymorphic Processing Demo ===")


if __name__ == "__main__":
    main()
