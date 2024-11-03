import asyncio
from websockets.server import serve
import random

async def echo(websocket):
    async for message in websocket:
        # Append a random number to the message
        random_number = random.randint(1, 1000)
        modified_message = f"{message} | Random Number: {random_number}"
        await websocket.send(modified_message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
