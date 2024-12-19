import asyncio

async def coroutine(t, id):
    await asyncio.sleep(t) #put the function into asynchrounous event loop
    print("I am a coroutine %s" %id)

async def main():
    results = await asyncio.gather(  #creates a task for each coroutine implicitly
        coroutine(10, "A"),
        coroutine(4, "B"),
        coroutine(2, "C")
    )
    print("The results are: %s" %results)


asyncio.run(main())