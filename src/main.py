async def main():
    game_pk = 716684 # Replace with a valid game PK
    await connect_to_gumbo(game_pk)

if __name__ == "__main__":
    asyncio.run(main())