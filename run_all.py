import asyncio
from host_agent import HostAgent

async def main():
    host = HostAgent("host@localhost", "p4ssword")
    await host.start(auto_register=True)

    print(">> HostAgent lanzado. Esperando indefinidamente...")

    while host.is_alive():
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
