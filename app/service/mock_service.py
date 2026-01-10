import asyncio
from app.core.config import APP_VERSION


async def delay_response(ms: int) -> int:
    """
     Delay response by specified milliseconds.

     Args:
         ms: Milliseconds to delay.

     Returns:
         The actual delayed milliseconds.
     """
    await asyncio.sleep(ms / 1000)
    return ms


def get_version() -> str:
    """
    Get application version from config.

    Returns:
      Version string.
    """
    return APP_VERSION
