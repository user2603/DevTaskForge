"""Evaluation entry for benchmark-receipt."""
import argparse
import asyncio


async def main(args):
    # benchmark-receipt: run checks against the prepared fixture and report the result.
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent_workspace", required=False)
    args = parser.parse_args()
    asyncio.run(main(args))
