import signal
import time
from vocode.streaming.input_device.base_input_device import BaseInputDevice
from vocode.helpers import create_microphone_input_and_speaker_output
from vocode.streaming.models.transcriber import (
    DeepgramTranscriberConfig,
    PunctuationEndpointingConfig,
)
from vocode.streaming.transcriber.base_transcriber import BaseTranscriber, Transcription
from vocode.streaming.transcriber.deepgram_transcriber import DeepgramTranscriber

flag = True
if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv

    load_dotenv()

    async def listen():
        global flag
        last_response_time = [time.time()] 
        async def on_response(response: Transcription):
            global flag
            if response.is_final:
                print(response.message)
                flag = True
                last_response_time[0] = time.time()

        microphone_input, speaker_output = create_microphone_input_and_speaker_output(
                streaming=True, use_default_devices=True
        )

        # replace with the transcriber you want to test
        transcriber = DeepgramTranscriber(
            DeepgramTranscriberConfig.from_input_device(
                microphone_input, endpointing_config=PunctuationEndpointingConfig()
            )
        )

        transcriber.set_on_response(on_response)
        asyncio.create_task(transcriber.run())
        print("Start speaking...press Ctrl+C to end. ")
        while True:
            # chunk = microphone_input.get_audio()
            # if chunk:
            #     transcriber.send_audio(chunk)
            # await asyncio.sleep(0)


            chunk = microphone_input.get_audio()
            if chunk:
                transcriber.send_audio(chunk)

            if time.time() - last_response_time[0] > 1:
                if flag:
                    print('more than one second')
                flag = False
                last_response_time[0] = time.time()

            await asyncio.sleep(0)


    asyncio.run(listen())