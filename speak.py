import asyncio
import edge_tts
import subprocess


async def speak(text, voice="en-GB-RyanNeural", filename="output.mp3"):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(filename)
    print(f"[✅] Saved speech to {filename}")
    subprocess.run(["mpv", filename])


# Example usage
# text = "Hello, Doruk. This is a message spoken using Edge TTS with a realistic English voice. Good morning. I hope this message finds you well. Today, we gather to discuss the important matters that will shape the future of our organization. Your dedication and professionalism are greatly appreciated, and I look forward to our collaborative success."
# asyncio.run(speak(text))
