from socket import gaierror
import aioping
import asyncio
import json
import time


async def do_ping(host: str):
    try:
        await aioping.ping(host, timeout=2)
        print("UP:".ljust(20), host)
    except TimeoutError:
        print("DOWN:".ljust(20), host)
    except gaierror:
        print("EXCEPTION:".ljust(20), host)


async def execute(hosts: list):
    await asyncio.wait([asyncio.create_task(do_ping(serv)) for serv in hosts])


def read_data() -> dict:
    with open("services.json", "r") as file:
        return json.load(file)


def main(services: dict):
    for srv, hosts in services.items():
        print(f"[{srv}]".center(30, '='))
        asyncio.run(execute(hosts))
        print()


if __name__ == '__main__':
    start = time.time()
    services = read_data()
    main(services)
    print(f"Время выполнения: {round(time.time() - start, 2)}")
