
import logging


logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

print("Hello World from print()")

logger.debug("Hello World from logger")

