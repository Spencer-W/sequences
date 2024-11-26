from __future__ import annotations

import sys
import pathlib import Path

from sequences.infra import sequences_application
from sequences.utils import logger

def main(args: list[str] | None = None) -> None:
    if args is None:
        args = sys.argv[1:]

    application = application.SequncesApp()
    config = Path(__file__).parent / 'configs'
    application.configure(args, config)

    logger.logger.info("Starting Sequences Application")

    application.run()

if __name__ == "__main__":
    main(sys.argv[1:])

    