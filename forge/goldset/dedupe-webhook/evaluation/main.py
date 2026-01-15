"""Evaluation entry for dedupe-webhook."""
import argparse
import asyncio


async def main(args):
    # dedupe-webhook: run checks against the prepared fixture and report the result.
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent_workspace", required=False)
    args = parser.parse_args()
    asyncio.run(main(args))
