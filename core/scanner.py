import asyncio

async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        print(f"Port {port} is open")
        writer.close()
    except:
        pass

async def run_scans(ip, start_port, end_port):
    tasks = []
    for port in range(start_port, end_port + 1):
        tasks.append(scan_port(ip, port))
    await asyncio.gather(*tasks)

# for asyn scan:
# asyncio.run(run_scans("192.168.1.1", 1, 65535))
