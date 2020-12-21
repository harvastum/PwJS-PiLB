import asyncio
from random import randrange



async def start(name, number, forks):
    while True:
        time = randrange(1,2)
        print(f"{name} started THINKING for {time} seconds")
        await asyncio.sleep(time*0.5)
        print(f"{name} waits for first fork")

        while forks[number]:
            await asyncio.sleep(1)
            if number<(number+1)%5:
                while forks[(number+1)%5]:
                    await asyncio.sleep(1)



        forks[number] = True

        print(f"{name} waits for second fork")
        while forks[(number+1)%5]:
            await asyncio.sleep(1)
            print(f'{name} still waiting\nforks: {forks}')
        forks[(number+1) % 5] = True
        time = randrange(1,2)
        print(f"{name} started EATING for {time} seconds")
        await asyncio.sleep(time*.5)
        forks[number], forks[(number+1) % 5] = False, False


async def main():
    forks = [False] *5
    philosophers = ['Aristotle', 'Confucius', 'Descartes', 'Foucault', 'Kant']
    for number, name in enumerate(philosophers):
        asyncio.create_task(start(name, number, forks))
    await asyncio.gather(*asyncio.all_tasks())

if __name__ == "__main__":
    asyncio.run(main())







