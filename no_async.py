from pythonping import ping
import json
import time


def check_host(host: str):
    try:
        if ping(host).success():
            print("UP:".ljust(20), host)
        else:
            print("DOWN:".ljust(20), host)
    except (RuntimeError, TimeoutError):
        print("EXCEPTION:".ljust(20), host)


def read_data() -> dict:
    with open("services.json", "r") as file:
        return json.load(file)


def main(services: dict):
    for srv, hosts in services.items():
        print(f"[{srv}]".center(30, '='))
        for host in hosts:
            check_host(host)
        print()


if __name__ == '__main__':
    start = time.time()
    services = read_data()
    main(services)
    print(f"Время выполнения: {round(time.time() - start, 2)}")



