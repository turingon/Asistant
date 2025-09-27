import edge_tts
import asyncio


async def list_voices():
    voices = await edge_tts.list_voices()
    for i in voices:
        if i["Locale"] == "en-GB":
            print(i["ShortName"], i["Gender"], i["VoiceTag"])
            print("\n")


asyncio.run(list_voices())
