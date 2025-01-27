import asyncio
import websockets
import json

async def connect_to_gumbo(game_pk):
    uri = f"wss://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"  # Use wss for secure WebSocket

    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to GUMBO feed for game {game_pk}")
            async for message in websocket:
                try:
                    game_data = json.loads(message)
                    # Process the game data here
                    process_game_data(game_data)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON message: {message}")
                except Exception as e:
                    print(f"An error occurred processing data: {e}")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
        # Implement reconnection logic here if needed
        await asyncio.sleep(5)  # Wait for 5 seconds before retrying
        await connect_to_gumbo(game_pk)  # Reconnect
    except Exception as e:
        print(f"A general error occurred: {e}")

def process_game_data(game_data):
    # Extract the data you need here
    try:
        liveData = game_data.get('liveData', {})
        boxscore = liveData.get('boxscore', {})
        teams = boxscore.get('teams', {})
        away = teams.get('away', {})
        away_team_name = away.get('team', {}).get('name', "N/A")
        home = teams.get('home', {})
        home_team_name = home.get('team', {}).get('name', "N/A")

        linescore = liveData.get('linescore', {})
        currentInning = linescore.get('currentInning', "N/A")
        inningHalf = linescore.get('inningHalf', "N/A")
        outs = linescore.get('outs', "N/A")
        balls = linescore.get('balls', "N/A")
        strikes = linescore.get('strikes', "N/A")

        print(f"Game: {away_team_name} vs {home_team_name}")
        print(f"Inning: {currentInning} {inningHalf}, Outs: {outs}, Count: {balls}-{strikes}")


    except Exception as e:
        print(f"Error processing game data: {e}")
        print(game_data)


