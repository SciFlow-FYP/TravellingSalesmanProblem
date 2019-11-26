import parsl
from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

config = Config(
    executors=[
        ThreadPoolExecutor(
            max_threads=20,
            label='local_threads'
        )
    ]
)


parsl.load(config)
