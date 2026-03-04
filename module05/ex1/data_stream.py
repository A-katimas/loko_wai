from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


# ==========================
# ABSTRACT BASE STREAM
# ==========================

class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id: str = stream_id
        self.total_processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch

        # default filtering
        return [item for item in data_batch if criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total_processed": self.total_processed
        }


# ==========================
# SENSOR STREAM
# ==========================

class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid sensor batch")

            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if item.startswith("temp:")
            ]

            if temps:
                self.avg_temp = sum(temps) / len(temps)

            self.total_processed += len(data_batch)

            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {self.avg_temp:.1f}°C"
            )

        except Exception as e:
            return f"Sensor processing error: {str(e)}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["avg_temp"] = self.avg_temp
        return stats


# ==========================
# TRANSACTION STREAM
# ==========================

class TransactionStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.net_flow: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid transaction batch")

            buys = [
                int(item.split(":")[1])
                for item in data_batch
                if item.startswith("buy:")
            ]

            sells = [
                int(item.split(":")[1])
                for item in data_batch
                if item.startswith("sell:")
            ]

            self.net_flow = sum(buys) - sum(sells)
            self.total_processed += len(data_batch)

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {self.net_flow:+d} units"
            )

        except Exception as e:
            return f"Transaction processing error: {str(e)}"


# ==========================
# EVENT STREAM
# ==========================

class EventStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid event batch")

            errors = [
                event for event in data_batch
                if "error" in event.lower()
            ]

            self.error_count = len(errors)
            self.total_processed += len(data_batch)

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{self.error_count} error detected"
            )

        except Exception as e:
            return f"Event processing error: {str(e)}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["error_count"] = self.error_count
        return stats


# ==========================
# POLYMORPHIC STREAM MANAGER
# ==========================

class StreamProcessor:

    def process_stream(
        self,
        stream: DataStream,
        data_batch: List[Any],
        filter_criteria: Optional[str] = None
    ) -> str:

        print(f"\nProcessing Stream: {stream.stream_id}")

        filtered = stream.filter_data(data_batch, filter_criteria)

        result = stream.process_batch(filtered)

        return result


# ==========================
# MAIN DEMO
# ==========================

def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()

    sensor_batch = ["temp:22.5", "humidity:65", "temp:24.0"]
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    event_batch = ["login", "error", "logout"]

    streams = [
        (sensor_stream, sensor_batch),
        (transaction_stream, transaction_batch),
        (event_stream, event_batch),
    ]

    print("\n=== Polymorphic Stream Processing ===")

    for stream, batch in streams:
        result = processor.process_stream(stream, batch)
        print(result)

    print("\n=== Stream Statistics ===")
    for stream, _ in streams:
        print(stream.get_stats())

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()