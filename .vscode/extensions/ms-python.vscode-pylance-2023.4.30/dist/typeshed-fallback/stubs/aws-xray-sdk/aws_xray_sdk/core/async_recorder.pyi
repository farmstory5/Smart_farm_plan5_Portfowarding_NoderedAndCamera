from _typeshed import Incomplete
from types import TracebackType

from .models.segment import SegmentContextManager as SegmentContextManager
from .models.subsegment import (
    SubsegmentContextManager as SubsegmentContextManager,
    is_already_recording as is_already_recording,
    subsegment_decorator as subsegment_decorator,
)
from .recorder import AWSXRayRecorder as AWSXRayRecorder
from .utils import stacktrace as stacktrace

class AsyncSegmentContextManager(SegmentContextManager):
    async def __aenter__(self): ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncSubsegmentContextManager(SubsegmentContextManager):
    async def __call__(self, wrapped, instance, args, kwargs): ...
    async def __aenter__(self): ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncAWSXRayRecorder(AWSXRayRecorder):
    def capture_async(self, name: Incomplete | None = None): ...
    def in_segment_async(self, name: Incomplete | None = None, **segment_kwargs): ...
    def in_subsegment_async(self, name: Incomplete | None = None, **subsegment_kwargs): ...
    async def record_subsegment_async(self, wrapped, instance, args, kwargs, name, namespace, meta_processor): ...