import asyncio
import os
import utils

async def add(root=os.getcwd()):
    chall_dirs = utils.get_directories(root)
    config = utils.read_ctf_config()
    for chall_dir in chall_dirs:
        print(f"Processing directory: {chall_dir}")
        basename = os.path.basename(chall_dir)
        config.set(section="challenges", option=basename, value=chall_dir)
    utils.save_ctf_config(config)

async def remove():
    config = utils.read_ctf_config()
    config["challenges"].clear()
    utils.save_ctf_config(config)

async def start():
    config = utils.read_ctf_config()
    challs = config['challenges']
    tasks = [utils.run_script(chall_dir, 'start') for _, chall_dir in challs.items()]
    await asyncio.gather(*tasks)

async def stop():
    config = utils.read_ctf_config()
    challs = config['challenges']
    tasks = [utils.run_script(chall_dir, 'stop') for _, chall_dir in challs.items()]
    await asyncio.gather(*tasks)
