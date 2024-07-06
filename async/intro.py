"""
Running awaitable objects concurrently.

awaitables are either coroutines, futures or tasks
coroutines - an awaitable that can be called by other functions. Wrapping a function with async def allows this to work
task - schedule a task concurrently. The benefit is to run the task without caring when the task finishes
future - the result of an async operation

async functions have to have `await` before them to run which pauses a coroutine

coroutines are useful to run a list of multiple tasks at the same time, e.g. a bunch of rest calls
tasks are useful when you need something run but don't care about the result, e.g. alerting or
"""
import asyncio


async def my_async_function():
    return "beep boop"


async def my_async_function_with_args(x: int):
    val = x**x
    print(f"triggering my_async_function_with_args for {val}")
    return val


async def async_task_wrapper():
    # creates a task in a group
    return asyncio.create_task(my_async_function_with_args(3))


async def my_async_function_within_a_function():
    # as we have an await here, the function needs to wait for this task to finish
    return await my_async_function()


async def async_group_of_tasks():
    # create a list of tasks
    background_tasks = set()
    quant = 100
    for i in range(quant):
        task = asyncio.create_task(my_async_function_with_args(x=i))

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)

        # Notice in the console, none of these are triggering until the current task is free. Unless we use sleep
        if i % 5:
            print(f"sleeping to trigger tasks {background_tasks}")
            await asyncio.sleep(0.001)


async def async_list_of_coroutines():
    # If we want to truly benefit from using coroutines, we can use gather and run a list of coroutines at once
    four, two, one = await asyncio.gather(
        my_async_function_with_args(4),
        my_async_function_with_args(2),
        my_async_function_with_args(1),
    )

    print(four, two, one)


if __name__ == "__main__":
    # We need to run our async functions in an event loop. Asyncio handles this for us
    print(asyncio.run(my_async_function()))
    print(asyncio.run(async_task_wrapper()))

    # If we want to run a list of coroutines and truly benefit from using coroutines, we can use gather
    asyncio.run(async_list_of_coroutines())

    # We can use an async function inside another async function with await
    asyncio.run(my_async_function_within_a_function())

    # If we want to create a list of tasks at once, we use gather
    asyncio.run(async_group_of_tasks())
